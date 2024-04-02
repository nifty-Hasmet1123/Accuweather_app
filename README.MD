# AccuWeather Application

This repository contains an AccuWeather application with both frontend and backend components.

## About the Application

The AccuWeather application is a weather forecast application that allows users to view weather forecasts for different continents, countries, and provinces. Users can select their desired location and view the daily temperature forecast along with headline information.

## Installation

1. Clone this repository:
    ```
    git clone <repository_url>
    ```

2. Install Python 3.11.5 or higher.

3. Create a virtual environment inside the backend repository:
    ```
    python -m venv .venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        .venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source .venv/bin/activate
        ```

5. Install backend dependencies:
    ```
    pip install -r requirements.txt
    ```

6. Set up the `.env` file:
    - Create a file named `.env` in the backend directory.
    - Add your AccuWeather API key and desired forecast format (e.g., "5day") in the `.env` file:
    - Reference in the .env.example
        ```
        ACCUWEATHER_API_KEY=<your_api_key>
        FORECAST_FORMAT=5day
        ```

7. Run the backend server:
    ```
    python run.py
    ```

8. Navigate to the frontend directory:
    ```
    cd frontend/accuweather_front_end
    ```

9. Install frontend dependencies:
    ```
    npm install
    ```

10. Start the frontend server:
    ```
    npm run dev
    ```

Now, you can access the application and start using it.

## Features

- Select first the continent, country, and province to view weather forecasts.
- View daily temperature forecast.
- Display headline information.

## Contributing

Contributions to the AccuWeather application are welcome! If you encounter any issues, have feature requests, or would like to contribute code, please feel free to open an issue or submit a pull request on the GitHub repository.

