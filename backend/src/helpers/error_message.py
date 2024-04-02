from typing import List, Dict

class ErrorMessage():
    """
    A class containing methods to generate error messages.

    Methods:
        not_a_valid_region_code(region_code: str) -> dict:
            Generate an error message for an invalid region code.
        return_error_from_api(response) -> dict:
            Generate an error message from an API response.
        missing_datas() -> dict:
            Generate an error message for missing data.
    """
    def not_a_valid_region_code(self, region_code: str) -> Dict:
        """
        Generate an error message for an invalid region code.

        Args:
            region_code (str): The invalid region code.

        Returns:
            dict: A dictionary containing the error message.
        """
        return { 
            "ValueError": "Region code is not valid",
            "Region_Code": region_code
        }
    
    def return_error_from_api(self, response: List[Dict]) -> Dict:
        """
        Generate an error message from an API response.

        Args:
            response: The API response object.

        Returns:
            dict: A dictionary containing the error message extracted from the response.
        """
        
        return {
            "ACCUWEATHER_ERROR_RESPONSE": {
                "error": { k: v for k, v in response.json().items() if k != "Reference" }
            }
        }
    
    def missing_datas(self) -> Dict:
        """
        Generate an error message for missing data.

        Returns:
            dict: A dictionary containing the error message for missing data.

        """

        return { "InputError": "continent, or country or province data is missing" }