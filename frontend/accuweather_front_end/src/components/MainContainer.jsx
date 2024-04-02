import FieldsContainer from "./FieldsContainer.jsx";
import ResponseContainer from "./ResponseContainer.jsx";
import { useState, useEffect } from 'react';


/**
 * Renders the main container of the application.
 * Manages state related to selected continent, country, provinces, countries, and forecast data.
 * Fetches data based on selected continent and country.
 * @returns {JSX.Element} The JSX element representing the main container.
 */
function MainContainer() {
    const [ state, setState ] = useState({
        selectedContinent: "",
        selectedCountry: "",
        provinces: null,
        countries: null,
        forecastData: null,
        selectedProvince: ""
    });
    
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
    
    const { selectedContinent, selectedCountry, provinces, countries, selectedProvince, forecastData } = state;

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Fetch countries based on selected continent
                if (selectedContinent !== "") {
                    const countryResponse = await fetch("http://127.0.0.1:5000/country_response", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ "continent": selectedContinent })
                    });
                    
                    const countryData = await countryResponse.json();
                    consoleLogTheDataForError(countryData);

                    setState(prevState => ({ ...prevState, countries: countryData }));
                }
                
                // Fetch provinces based on selected country
                if (selectedCountry !== "") {
                    const provinceResponse = await fetch("http://127.0.0.1:5000/province_response", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ "country": selectedCountry })
                    });

                    const provinceData = await provinceResponse.json();
                    consoleLogTheDataForError(provinceData);

                    setState(prevState => ({ ...prevState, provinces: provinceData }));
                }

            } catch (error) {
                console.error("Error fetching data", error);
            }
        };

        fetchData();
    }, [selectedContinent, selectedCountry, selectedProvince]); // Trigger useEffect when continent or country changes

    return (
        <main className="main-container">
            <FieldsContainer 
                selectedContinent={ selectedContinent }
                setSelectedContinent= { (value) => setState(prevState => ({ ...prevState, selectedContinent: value })) }
                selectedCountry={ selectedCountry }
                setSelectedCountry={ (value) => setState(prevState => ({ ...prevState, selectedCountry: value })) }
                provinces={provinces}
                setProvinces={ (value) => setState(prevState => ({ ...prevState, provinces: value })) }
                countries={countries}
                setCountries={ (value) => setState(prevState => ({ ...prevState, countries: value })) }
                selectedProvince={selectedProvince}
                setSelectedProvince={ (value) => setState(prevState => ({ ...prevState, selectedProvince: value })) }
                setForecastData={ (value) => setState(prevState => ({ ...prevState, forecastData: value })) }
            />
            
            <ResponseContainer 
                forecastData={forecastData}
            />
            
        </main>
    )
}

export default MainContainer;