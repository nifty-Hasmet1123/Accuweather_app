/**
 * The main component of the application.
 * Renders the main container and footer components.
 * @returns {JSX.Element} The JSX element representing the main application.
 */

import './App.css';
import './css/styles.css';
import MainContainer from './components/MainContainer.jsx';
import Footer from './components/Footer.jsx';

function App() {
    return (
        <>
            <MainContainer />
            <Footer />
        </>
    )
}

export default App
