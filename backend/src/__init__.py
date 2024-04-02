from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

# environmental variables
app.config["KEY"] = os.getenv("ACCUWEATHER_API_KEY")
app.config["LOCATION"] = os.getenv("ACCUWEATHER_LOCATION_KEY")
app.config["PERIOD"] = os.getenv("ACCUWEATHER_PERIOD")

from src import routes