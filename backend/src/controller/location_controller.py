from src.credential_class import SetConfigs
from src.helpers.error_message import ErrorMessage
from typing import List, Dict, Union
import requests

error_message = ErrorMessage()

class LocationController(SetConfigs):
    """
    Controller class for handling location-based operations and API calls.
    """
    def __init__(self) -> None:
        """
        Initializes the LocationController class.
        """
        super().__init__()
        self.params = { "apikey": self.API_KEY }
        self.valid_region_code = [ "AFR", "ANT", "ARC", "ASI", "CAC", "EUR", "MEA", "NAM", "OCN", "SAM" ]
        self.country_code = None

    def weather_forecast_router(self, data: dict) -> Union[List[Dict], Dict]:
        """
        Determines the appropriate weather forecast route based on provided data.

        Args:
            data (dict): Dictionary containing continent, country, and province information.

        Returns:
            Union[List[Dict], Dict]: Either a list of daily weather reports or an error message.
        """
        
        continent = data.get("continent")
        country = data.get("country")
        province = data.get("province")

        if continent and country and province:
            # fetch the Location_key_here
            location_key = self.api_province_key(province)

            return self.api_get_daily_weather_forecast(location_key=location_key)

        else:
            return error_message.missing_datas()
        
    ### responses ###
    def api_get_daily_weather_forecast(self, location_key: str):
        """
        Retrieves daily weather forecast data from the API based on the provided location key.

        Args:
            location_key (str): The location key used to fetch weather data.

        Returns:
            dict: Daily weather forecast data.
        """
        if location_key:
            api_uri = f"http://dataservice.accuweather.com/forecasts/v1/daily/{self.PERIOD}/{location_key}"
            response = requests.get(api_uri, params = self.params, timeout = 60)

            if response.ok:
                return response.json()
            else:
                return error_message.return_error_from_api(response)

    def api_continent_response(self, continent: str) -> Union[List[Dict], Dict]:
        """
        Retrieves response data from the API based on the specified continent.

        Args:
            continent (str): The continent for which data is to be retrieved.

        Returns:
            Union[List[Dict], Dict]: Response data from the API.
        """
        continent_response = self.api_call_region_continent(continent)

        if isinstance(continent_response, dict):
            if continent_response.get("ACCUWEATHER_ERROR_RESPONSE") or continent_response.get("ValueError"):
                return continent_response

        return continent_response
        

    def api_country_response(self, collection_countries: list, target_country: str) -> Union[List[Dict], Dict]:
        """
        Retrieves response data from the API based on the specified country.

        Args:
            collection_countries (list): List of countries.
            target_country (str): The country for which data is to be retrieved.

        Returns:
            Union[List[Dict], Dict]: Response data from the API.
        """
        country_details = self.api_call_if_country_code_on_continent(collection_countries, target_country)

        if isinstance(country_details, str):
            self.country_code = country_details
          
            api_uri = "http://dataservice.accuweather.com/locations/v1/adminareas/{}".format(self.country_code)
            response = requests.get(api_uri, params = self.params, timeout = 60)

            if response.ok:
                # returns a list of dictionaries
                return response.json()
            else:
                return error_message.return_error_from_api(response)
            
    def api_province_key(self, province_name: str) -> str:
        """
        Retrieves the location key for the specified province.

        Args:
            province_name (str): The name of the province.

        Returns:
            str: The location key.
        """
        if self.country_code and province_name:
            # create a copy of the params
            copy_params = self.params.copy()
            copy_params["q"] = province_name
            
            api_uri = "http://dataservice.accuweather.com/locations/v1/cities/{}/search".format(self.country_code)
            response = requests.get(api_uri, params = copy_params, timeout = 60)
            
            if response.ok:
                data = response.json()
                
                for dictionary_items in data:
                    for k, v in dictionary_items.items():
                        if k == "Key":
                            # fetch only the first Key
                            return v

            else:
                return error_message.return_error_from_api(response)

    ### helper methods ###
    def api_call_region_continent(self, region_code: str) -> Union[List[Dict], Dict]:
        """
        Retrieves response data from the API based on the specified region code.

        Args:
            region_code (str): The region code for which data is to be retrieved.

        Returns:
            Union[List[Dict], Dict]: Response data from the API.
        """
        if region_code in self.valid_region_code:
            # call the api here
            api_uri = "http://dataservice.accuweather.com/locations/v1/countries/{}".format(region_code)
            response = requests.get(api_uri, params = self.params, timeout = 60)

            if response.ok:
                # returns a list of dictionaries
                return response.json()
            else:
                return error_message.return_error_from_api(response)
        
        return error_message.not_a_valid_region_code(region_code)
    

    def api_call_if_country_code_on_continent(self, collection_of_countries: list, target_country: str) -> Union[str, Dict]:
        """
        Retrieves response data from the API based on the specified country code.

        Args:
            collection_of_countries (list): List of countries.
            target_country (str): The country for which data is to be retrieved.

        Returns:
            Union[str, Dict]: Either the country code or an error message.
        """
        
        for entry in collection_of_countries:
            try:
                if target_country == entry.get("EnglishName") or target_country == entry.get("LocalizedName"):
                    # fetch the country code here
                    return entry["ID"]
                
            except AttributeError as e:
                # jsonify this to bad request
                return error_message.return_error_from_api(e)
