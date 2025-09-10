import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/")
USERNAME = os.getenv("USERNAME", "Admin")
PASSWORD = os.getenv("PASSWORD", "admin123")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
CHROME_BINARY = os.getenv("CHROME_BIN")  # CI có thể set path chrome
