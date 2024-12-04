# Tuya Cloud Interface

## Description
**Tuya Cloud Interface** is a Python-based project designed to interact with Tuya Cloud-connected devices using the Tuya Cloud API. It provides real-time monitoring and logging of device statuses, such as PIR motion sensors, and can be extended to support other devices.

## Prerequisites
1. Python 3.7 or higher.
2. A Tuya Cloud Developer account. Register at [Tuya IoT Platform](https://iot.tuya.com/).
3. A PIR Motion Sensor or other Tuya-supported device linked to the Tuya Smart app (available both for [Android](https://play.google.com/store/apps/details?id=com.tuya.smart&hl=it&pli=1) and [iOS](https://apps.apple.com/it/app/tuya-smart/id1034649547) devices)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/tuya_cloud_interface.git
cd tuya_cloud_interface
```

### 2. Create a .env File
Create a .env file in the root directory of the project and add the following:
```bash
ACCESS_ID=your_access_id
ACCESS_SECRET=your_access_secret
ENDPOINT=https://openapi.tuyaeu.com  # Adjust based on your data center
DEVICE_ID=your_device_id
USERNAME=your_tuya_app_email
PASSWORD=your_tuya_app_password
COUNTRY_CODE=+39  # Your country code (e.g., +39 for Italy)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Script
```bash
python3 main.py
```
