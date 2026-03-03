import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    """reads from .env file"""
    BASE_URL = os.getenv("BASE_URL", "https://www.automationexercise.com")
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    TEST_USERNAME = os.getenv("TEST_USERNAME")
