/**
 * Renders the fields container including dropdowns for selecting continent, country, and province,
 * and a button to fetch weather forecast data.
 * 
 * @param {Object} props - The props object containing various state variables and setter functions.
 * @param {string} props.selectedContinent - The selected continent.
 * @param {function} props.setSelectedContinent - Setter function for selected continent.
 * @param {string} props.selectedCountry - The selected country.
 * @param {function} props.setSelectedCountry - Setter function for selected country.
 * @param {Array} props.provinces - Array of provinces.
 * @param {Array} props.countries - Array of countries.
 * @param {string} props.selectedProvince - The selected province.
 * @param {function} props.setSelectedProvince - Setter function for selected province.
 * @param {function} props.setForecastData - Setter function for forecast data.
 * @returns {JSX.Element} The JSX element representing the fields container.
 */

function FieldsContainer({ 
    selectedContinent, 
    setSelectedContinent,
    selectedCountry,
    setSelectedCountry,
    provinces,
    countries, 
    selectedProvince,
    setSelectedProvince,
    setForecastData
}) {
    /**
     * Generates continent options.
     * @returns {Object} The continent options object.
     */
    const continentOptions = continents();

    /**
     * Handles continent change event.
     * @param {Object} event - The event object.
     */
    const handleContinentChange = (event) => {
        setSelectedContinent(event.target.value);
    }

    /**
     * Handles country change event.
     * @param {Object} event - The event object.
     */
    const handleCountryChange = (event) => {
        setSelectedCountry(event.target.value);
    }

    /**
     * Handles province change event.
     * @param {Object} event - The event object.
     */
    const handleProvinceChange = (event) => {
        setSelectedProvince(event.target.value);
    }

    /**
     * Logs data to console if there's an error response.
     * @param {Object} data - The data object.
     */
    const consoleLogTheDataForError = (data) => {
        const ACCUWEATHER_ERROR_RESPONSE = data?.ACCUWEATHER_ERROR_RESPONSE;

        if (ACCUWEATHER_ERROR_RESPONSE) {
            alert("Hey bro, look at the console for errors");
            console.log(data);
        }
    }

    /**
     * Fetches weather forecast data.
     */
    const handleOnClickFetchDatas = () => {
        const fetchWeatherForecast = async () => {
            if (selectedContinent && selectedCountry && selectedProvince) {
                try {
                    const dailyForecastResponse = await fetch("http://127.0.0.1:5000/weather-forecast", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({
                            continent: selectedContinent,
                            country: selectedCountry,
                            province: selectedProvince
                        })
                    })

                    const dailyForecastData = await dailyForecastResponse.json();
                    // console.log(dailyForecastData);
                    consoleLogTheDataForError(dailyForecastData);

                    setForecastData(dailyForecastData);
                
                } catch (error) {
                    console.error("Error fetching the data: ", error);
                }
            }
        }

        fetchWeatherForecast();
    }
    /**
     * Renders dropdown options for countries based on selected continent.
     * @returns {JSX.Element[]} Array of JSX elements representing country options.
     */
    const showCountryBasedOnContinent = () => {
        if (countries && countries.length !== 0 && countries instanceof Array) {
            return countries.map(country => {
                return <option key={country} value={country}> {country} </option>
            })
        }
    }

    /**
     * Renders dropdown options for provinces based on selected country.
     * @returns {JSX.Element[]} Array of JSX elements representing province options.
     */
    const showProvincesBasedOnCountry = () => {
        if (provinces && provinces.length !== 0 && provinces instanceof Array) {
            return provinces.map(province => {
                return <option key={province} value={province}> {province} </option>
            })
        }
    }

    return (
        <div className="fields-container">
            <div className="input-container">
                <h1 id="accuweather-txt">
                    AccuWeather App
                </h1>
                
                <select 
                    name="dropdown-continent" 
                    className="dropdown"
                    value={ selectedContinent }
                    onChange={ handleContinentChange }
                >
                    <option value="select-continent">Select Continent</option>

                    {
                        Object.entries(continentOptions).map(([key, value]) => {
                            return <option key={value} value={key}> {value} </option>
                        })
                    }

                </select>

                <select 
                    name="dropdown-country" 
                    className="dropdown"
                    value={ selectedCountry }
                    onChange={ handleCountryChange }
                >
                    <option value="select-country">Select Country</option>
                    { showCountryBasedOnContinent() }
                </select>

                <select 
                    name="dropdown-province"
                    className="dropdown"
                    value={ selectedProvince }
                    onChange={ handleProvinceChange }
                >
                    <option value="select-province">Select Province</option>
                    { showProvincesBasedOnCountry() }
                </select>

                <button 
                    className="button__forecast"
                    onClick={ handleOnClickFetchDatas }
                >
                    Find Forecast
                </button>
            </div>
        </div>
    )
}

/**
 * Returns continent options.
 * @returns {Object} The continent options object.
 */
function continents() {
    return {
        AFR: "Africa",
        ANT: "Antarctica",
        ARC: "Arctic",
        ASI: "Asia",
        CAC: "Central America and the Carribean",
        EUR: "Europe",
        MEA: "Middle East",
        NAM: "North America",
        OCN: "Oceania",
        SAM: "South America"
    };
}

export default FieldsContainer;