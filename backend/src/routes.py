from flask import request as flask_request
from flask import jsonify
from src import app
from src.controller import location_controller
from src.data.datas import Storage
from src.helpers.unpack_json import unpack_json_response

# global variable instance for the data to persist
collection_of_countries = Storage()
# set the router instance globally
router = location_controller.LocationController()

@app.route("/weather-forecast", methods=["POST"])
def display_forecast_router():
    """
    Route for handling weather forecast requests.

    This route is triggered when a POST request is made to "/weather-forecast".
    It expects JSON data containing weather forecast parameters. The data is processed
    by the LocationController class and the response is returned as JSON.

    Returns:
        Response: JSON response containing weather forecast data.
    """
    data = flask_request.get_json()

    return jsonify(router.weather_forecast_router(data))

@app.route("/country_response", methods=["POST"])
def continent_router():
    """
    Route for handling continent-based response requests.

    This route is triggered when a POST request is made to "/country_response".
    It expects JSON data containing a continent. The LocationController class is used
    to fetch the response data. If the response is successful (a list of countries),
    it is unpacked and returned as JSON. Otherwise, an error message is returned.

    Returns:
        Response: JSON response containing country data or an error message.
    """
    data = flask_request.get_json()
    continent = data.get("continent")

    # call the response data here
    response = router.api_continent_response(continent = continent)

    # check the response if it is a list(succesful call) or a dict(error call)

    if isinstance(response, list):
        # unpacked the response
        unpacked_country_response = unpack_json_response(response)
        
        # assign the original response to the Storage class
        collection_of_countries.set_countries(response)

        return jsonify(unpacked_country_response)

    else:
        return jsonify(response)

@app.route("/province_response", methods=["POST"])
def country_router():
    """
    Route for handling province-based response requests.

    This route is triggered when a POST request is made to "/province_response".
    It expects JSON data containing a country. The LocationController class is used
    along with data fetched from the Storage class (list of countries) to fetch
    the response data. If the response is successful (a list of provinces),
    it is unpacked and returned as JSON. Otherwise, an error message is returned.

    Returns:
        Response: JSON response containing province data or an error message.
    """

    data = flask_request.get_json()
    country = data.get("country")
    
    # fetch the list of countries in the Storage class
    countries = collection_of_countries.get_countries()

    # call the response data here
    response = router.api_country_response(countries, country)
    
    if isinstance(response, list):
        # unpack here
        unpacked_province_response = unpack_json_response(response)

        # assign the original response to the Storage class
        collection_of_countries.set_provinces(response)

        return jsonify(unpacked_province_response)
    
    else:
        return jsonify(response)
    
