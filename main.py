import time
from datetime import datetime
from tuya_iot import TuyaOpenAPI
from dotenv import load_dotenv
from colorama import Fore, Style
import os

# Load environment variables from .env file
load_dotenv()

# Tuya Cloud Configuration
ACCESS_ID = os.getenv("ACCESS_ID")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
ENDPOINT = os.getenv("ENDPOINT")
DEVICE_ID = os.getenv("DEVICE_ID")

# Tuya App Credentials
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")

# Initialize Tuya OpenAPI
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_SECRET)

try:
    response = openapi.connect(USERNAME, PASSWORD, COUNTRY_CODE, "tuyaSmart")
    print(f"Token Response: {response}")
except Exception as e:
    print(f"Error during connection: {e}")

# Continuous acquisition of sensor data
while True:
    try:
        # Get the device state from the cloud performing a GET request
        response = openapi.get(f"/v1.0/iot-03/devices/{DEVICE_ID}/status")
        print(f"{datetime.now()} - Device response: {response}")

        # Check if the response is successful
        if response.get('success'):
            for status in response['result']:
                if status['code'] == 'pir':  # Replace 'pir' with the correct code for motion detection
                    motion_status = status['value']
                    if motion_status == 'none':
                        print(Fore.RED + f"No motion detected." + Style.RESET_ALL)
                    elif motion_status == 'pir':
                        print(Fore.GREEN + f"Motion detected!" + Style.RESET_ALL)
                    else:
                        print(f"Unknown motion status: {motion_status}")
        else:
            print(f"Failed to fetch device status: {response}")

        # Sleep for one second
        time.sleep(1)

    except Exception as e:
        print(f"{datetime.now()} - Error: {e}")
        # Wait and retry in case of an error
        time.sleep(5)
