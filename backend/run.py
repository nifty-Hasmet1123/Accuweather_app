"""
Entry point for running the Flask application.

This script initializes and runs the Flask application defined in the src __init__ file.

Usage:
    python run.py

Note:
    Ensure that the 'app' module is properly configured with routes and settings.
"""

from src import app

if __name__ == "__main__":
    app.run(debug = True)