import { useState, useEffect } from "react";


/**
 * Renders the container for displaying response data including forecast and headline.
 * Manages state for empty response, processed forecast, and processed headline.
 * @param {Object} props - The props object containing forecastData.
 * @param {Object} props.forecastData - The forecast data to be displayed.
 * @returns {JSX.Element} The JSX element representing the response container.
 */
function ResponseContainer({ forecastData }) {
    const [ isEmpty, setIsEmpty ] = useState(true);
    const [ processForecast, setProcessForecast ] = useState([]);
    const [ processHeadline, setProcessHeadline ] = useState({});

    useEffect(() => {
        if (forecastData) {
            setIsEmpty(false);
            displayForecast();
        } else {
            setIsEmpty(true);
            setProcessForecast([]);
            setProcessHeadline({});
        }
    }, [forecastData]);

    /**
     * Determines the class name for the response container based on whether the response is empty.
     * @returns {string} The class name for the response container.
     */
    const responseName = () => {
        return !isEmpty ? "response-container": "no-content";
    }
    
    /**
     * Processes the forecast data and sets the state for processed forecast and headline.
     */
    const displayForecast = () => {
        const processForecastData = [];
        
        if (!forecastData) return null;

        if (forecastData instanceof Object) {
            const dailyForecastArrayObject = forecastData?.DailyForecasts;
            const headlineObject = forecastData?.Headline;
            
            // iterate through the day(maximum of 5) then store it in a state
            if (dailyForecastArrayObject instanceof Array) {
                for (let index = 0; index < dailyForecastArrayObject.length; index++) {

                    const forecast = dailyForecastArrayObject[index];
                    const processDate = new Date(forecast.Date).toDateString();
                    const processDayIconPhrase = forecast?.Day?.IconPhrase;
                    const processNightIconPhrase = forecast?.Night?.IconPhrase;
                    const processTemperatureValueMaximum = forecast?.Temperature?.Maximum?.Value;
                    const processTemperatureValueMinimum = forecast?.Temperature?.Minimum?.Value;
        
                    processForecastData.push(
                        <div key={index}>
                            <h3>Day {index + 1}</h3>
                            <p>Date: {processDate}</p>
                            <p>Day Icon Phrase: {processDayIconPhrase}</p>
                            <p>Night Icon Phrase: {processNightIconPhrase}</p>
                            <p>Temperature value maximum: {processTemperatureValueMaximum}</p>
                            <p>Temperature value minimum: {processTemperatureValueMinimum}</p>
                            <br />
                        </div>
                    );
                };
            }
            
            if (headlineObject instanceof Object) {
                setProcessHeadline(headlineObject);
            }
            
            setProcessForecast(processForecastData);
        }
    }

    /**
     * Displays the headline data.
     * @returns {JSX.Element|null} The JSX element representing the headline.
     */
    const displayHeadline = () => {
        if (processHeadline) {
            const { EffectiveDate, EndDate, Category, Severity, Text } = processHeadline;

            try {
                const modifiedEffectiveDate = new Date(EffectiveDate).toDateString();
                const modifiedEndDate = new Date(EndDate).toDateString();

                return (
                    <div>
                        <p>Category: { Category }</p>
                        <p>Effective Date: { modifiedEffectiveDate }</p>
                        <p>End Date: { modifiedEndDate }</p>
                        <p>Severity: { Severity }</p>
                        <p>Text: { Text }</p>
                    </div>
                );
            } catch (error) {
                console.error(error);
                return <p>Error in displaying headline</p>;
            }
        }
        return null;
    };

    return (
        <div className={ responseName() }>
            <div className="text-container">
                <h2>Daily Temperature: </h2>
                <br />
                { processForecast }
                <br />
                <h2>Headline: </h2>                
                { displayHeadline() }
            </div>
        </div>
    );
}

export default ResponseContainer;