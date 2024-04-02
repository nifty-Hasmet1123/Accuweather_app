from src.credential_class import SetConfigs
from src.helpers.error_message import ErrorMessage
from typing import List, Dict, Union
import requests

error_message = ErrorMessage()

class LocationController(SetConfigs):
    def __init__(self) -> None:
        super().__init__()
        self.params = { "apikey": self.API_KEY }
        self.valid_region_code = [ "AFR", "ANT", "ARC", "ASI", "CAC", "EUR", "MEA", "NAM", "OCN", "SAM" ]
        self.country_code = None

    def weather_forecast_router(self, data: dict) -> Union[List[Dict], Dict]:
        ### this weather_forecast_router is for submit the end output should be the daily weather report
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
        if location_key:
            api_uri = f"http://dataservice.accuweather.com/forecasts/v1/daily/{self.PERIOD}/{location_key}"
            response = requests.get(api_uri, params = self.params, timeout = 60)

            if response.ok:
                return response.json()
            else:
                return error_message.return_error_from_api(response)

    def api_continent_response(self, continent: str) -> Union[List[Dict], Dict]:
        continent_response = self.api_call_region_continent(continent)

        if isinstance(continent_response, dict):
            if continent_response.get("ACCUWEATHER_ERROR_RESPONSE") or continent_response.get("ValueError"):
                return continent_response

        return continent_response
        

    def api_country_response(self, collection_countries: list, target_country: str) -> Union[List[Dict], Dict]:
        # returns a list of available province in a country
        country_details = self.api_call_if_country_code_on_continent(collection_countries, target_country)

        if isinstance(country_details, str):
            # assign the attribute of country code to this call here.
            # index position of tuple
            self.country_code = country_details
          
            api_uri = "http://dataservice.accuweather.com/locations/v1/adminareas/{}".format(self.country_code)
            response = requests.get(api_uri, params = self.params, timeout = 60)

            if response.ok:
                # returns a list of dictionaries
                return response.json()
            else:
                return error_message.return_error_from_api(response)
            
    def api_province_key(self, province_name: str) -> str:
        ## still not working I need the user to enter the name of the province instead ##
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

    ### helper methods
    def api_call_region_continent(self, region_code: str) -> Union[List[Dict], Dict]:
        # returns a list of countries
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
        for entry in collection_of_countries:
            try:
                if target_country == entry.get("EnglishName") or target_country == entry.get("LocalizedName"):
                    # fetch the country code here
                    return entry["ID"]
                
            except AttributeError as e:
                # jsonify this to bad request
                return error_message.return_error_from_api(e)
