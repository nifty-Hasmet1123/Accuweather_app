from typing import List, Dict

class Storage():
    """
    A class for storing response data related to countries and provinces.

    Attributes:
        _response_countries (List[Dict]): A list of dictionaries representing country data.
        _response_provinces (List[Dict]): A list of dictionaries representing province data.
    """

    def __init__(
        self,
        response_countries: List = None,
        response_provinces: List = None
    ) -> None:
        """
        Initialize the Storage instance.

        Args:
            response_countries (List[Dict], optional): List of dictionaries representing country data.
            response_provinces (List[Dict], optional): List of dictionaries representing province data.
        """
        self._response_countries = response_countries
        self._response_provinces = response_provinces

    def get_countries(self) -> List[Dict]:
        """
        Get the list of countries.

        Returns:
            List[Dict]: A list of dictionaries representing country data.
        """
        if self._response_countries:
            return self._response_countries

    def set_countries(self, value: List[Dict]) -> None:
        """
        Set the list of countries.

        Args:
            value (List[Dict]): A list of dictionaries representing country data.
        """
        self._response_countries = value

    def get_provinces(self) -> List[Dict]:
        """
        Get the list of provinces.

        Returns:
            List[Dict]: A list of dictionaries representing province data.
        """
        if self._response_provinces:
            return self._response_provinces
    
    def set_provinces(self, value: List[Dict]) -> None:
        """
        Set the list of provinces.

        Args:
            value (List[Dict]): A list of dictionaries representing province data.
        """
        self._response_provinces = value
