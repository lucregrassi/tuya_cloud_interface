# Tuya Cloud Interface: Real-Time PIR Motion Sensor Monitoring

This guide explains how to set up and use a PIR Motion Sensor with the Tuya IoT Cloud platform and interact with it using the Tuya Cloud Interface Python project. Following these steps, you can link the sensor to the cloud, retrieve its data, and monitor real-time motion detection.

## Prerequisites
- Python 3.7 or higher.
- A Tuya Cloud Developer account (register at Tuya IoT Platform).
- PIR Motion Sensor or other Tuya-supported device linked to the Tuya Smart app (available for Android and iOS).

## Step 1: Download the Tuya Smart App
To manage your Tuya-compatible devices, download the Tuya Smart app:
- For Android devices: Download from the [Google Play Store](https://play.google.com/store/apps/details?id=com.tuya.smart&hl=it).
-	For iOS devices: Download from the [App Store](https://apps.apple.com/us/app/tuya-smart/id1034649547).

## Step 2: Create a Tuya IoT Account
1.	Visit the [Tuya Developer Platform website](https://iot.tuya.com).
2.	Create an account or log in if you already have one.
3.	Create a new cloud project with the following details:
    - Name: Your project name.
    - Description: A brief description of your project.
    - Industry: Education/Campus.
    - Development Method: Smart Home.
    - Data Center: Central Europe (to match the App Data Center).

## Step 3: Authorize API Services
In your cloud project, authorize the following API services:
- IoT Core: Provides basic functionalities such as device management, real-time communication, and data collection.
- Authorization Token Management: Manages authentication and authorization for accessing other APIs.
- Smart Home Basic Service: Offers essential functionalities for managing smart home devices.
- Data Status Notification: Sends real-time notifications on device status updates.
- Device Pool Management: Allows obtaining information about devices, including current status and properties.


## Step 4: Set Up the PIR Motion Sensor
1.	Open the Tuya Smart app on your phone and create an account (or log in to an existing one).
2.	Connect the PIR Motion Sensor to a power source and turn it on.
3.	Press and hold the side button until the green light blinks, indicating pairing mode.
4.	Add the sensor as a new device in the app, connecting it to a 2.4GHz Wi-Fi network.
5.	Set the work mode to “OnlyLight” to prevent it from sounding.

## Step 5: Link the Sensor to the Cloud Project
1.	In the [Tuya Developer Platform](https://platform.tuya.com), go to your project and navigate to Devices → Link App Account → Add App Account.
2.	In the Tuya Smart app, go to “Me” at the bottom right of the screen and tap the QR code icon at the top.
3.	Scan the QR code displayed on the Tuya Developer Platform to link the app with the cloud project.
4.	Verify that the sensor is visible in the cloud project and has been assigned an ID.

## Step 6: Set Up the Tuya Cloud Interface Project
### Clone the Repository
Clone this repository in a folder of your choice by navigating to the folder and executing the following command in a terminal:
```bash
git clone https://github.com/yourusername/tuya_cloud_interface.git
cd tuya_cloud_interface
```
### Create a .env file
In the root directory of the project, create a file named .env and add the following content:
```bash
ACCESS_ID=your_access_id
ACCESS_SECRET=your_access_secret
ENDPOINT=https://openapi.tuyaeu.com  # Adjust based on your data center
DEVICE_ID=your_device_id
USERNAME=your_tuya_app_email
PASSWORD=your_tuya_app_password
COUNTRY_CODE=+XX  # Your country code (e.g., +39 for Italy)
```
Make sure to replace the placeholders with your actual data:
 ```bash
ACCESS_ID and ACCESS_SECRET: Retrieve these from the Overview tab in your Tuya Cloud project.
ENDPOINT: Use https://openapi.tuyaeu.com for Central Europe. Adjust if your data center is different.
DEVICE_ID: Visible in the Devices section of your Cloud Project.
USERNAME, PASSWORD, COUNTRY_CODE: Credentials for your Tuya Smart app account.
 ```
### Install the Dependencies
To install the libraries required to run the script, execute the following command in a terminal:
```bash
pip install -r requirements.txt
```

## Step 7: Test the Script
1.	Run the script to verify if the sensor data is successfully retrieved:
    ```bash
    python3 main.py
    ```

2.	If successful, the script will return a message similar to the following:
    ```bash
    {
    "result": [
      {"code": "pir", "value": "pir"},
      {"code": "battery_percentage", "value": 0}
    ],
    "success": true,
    "t": 1733318804621,
    "tid": "67c94acbb24311ef828e8aa4893defa6"
    }
    ```

    The "result" field contains the key information from the PIR motion sensor:
    - "code": "pir", "value": "pir" indicates that motion has been detected.
	  - "code": "pir", "value": "none" indicates no motion detected.
	  - "code": "battery_percentage", "value": 0 reflects the current battery level of the sensor (in this case, 0%).
    This output confirms that the sensor is operational and able to detect motion in real-time. The script can now be expanded to process this data in a way that meets your specific requirements.

## Conclusion 
The data retrieved from the sensor opens up a variety of possibilities for practical applications, such as:
- Storing Data in a Database: Log motion detection events with timestamps for analysis, reporting, or compliance tracking.
- Triggering Notifications: Set up real-time alerts (e.g., push notifications, SMS, or emails) to notify users when motion is detected.
- Home Automation: Use motion detection to automate smart home actions, such as turning on lights, adjusting thermostats, or activating security cameras.
- Behavioral Analytics: Analyze motion trends over time to gain insights into space usage, identify potential security risks, or optimize facility management.
- Machine Learning Applications: Leverage the data to train predictive models for tasks like anomaly detection, predictive maintenance, or optimizing smart environment responses.

Feel free to extend the script to incorporate these functionalities or adapt it to your specific use case. For further support and inspiration, explore the [Tuya Developer Documentation](https://developer.tuya.com/en/docs/iot).

Happy coding! 🚀

