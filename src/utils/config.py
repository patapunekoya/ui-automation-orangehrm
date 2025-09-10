import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL="https://opensource-demo.orangehrmlive.com/"
USERNAME="Admin"    
PASSWORD="admin123"

HEADLESS = True  # để thấy trình duyệt đang làm gì

CHROME_BINARY = None  # CI có thể set path chrome
