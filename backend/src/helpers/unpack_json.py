from typing import List

def unpack_json_response(json_data: List[dict]) -> List:
    """
    Unpacks JSON response data to extract country names.

    Args:
        json_data (List[dict]): A list of dictionaries containing JSON response data.

    Returns:
        List: A list of country names extracted from the JSON data.

    Note:
        This function assumes that each dictionary in json_data contains a key corresponding to
        the target_key for the country name.
    """
    
    target_key = "EnglishName"
    container = []

    for items in json_data:
        country_name = items[target_key]
        container.append(country_name)
    
    return container
