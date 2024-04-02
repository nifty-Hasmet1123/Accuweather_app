/**
 * Renders the footer component displaying the copyright year and attribution.
 * @returns {JSX.Element} The JSX element representing the footer.
 */

function Footer() {
    return (
        <footer className="footer">
            &copy; { new Date().getFullYear() } Maxi • Built with Flask & React
        </footer>
    )
}

export default Footer;