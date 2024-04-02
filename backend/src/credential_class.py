from src import app

class SetConfigs():
    """
    A class for setting configurations from the Flask application.

    Attributes:
        API_KEY (str): The API key retrieved from the Flask application's configuration.
        PERIOD (str): The period retrieved from the Flask application's configuration.
    """

    def __init__(self) -> None:
        """
        Initialize the SetConfigs instance.

        Retrieves configuration values such as API_KEY and PERIOD from the Flask application.
        """
        
        self.API_KEY = app.config["KEY"]
        self.PERIOD = app.config["PERIOD"]