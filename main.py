import os
import time
import requests
import smtplib
from dotenv import load_dotenv
from datetime import datetime


# Load environment variables
load_dotenv()

# Environment variables
latitude = os.getenv("LATITUDE")
longitude = os.getenv("LONGITUDE")
sunrise_sunset_api_key = os.getenv("SUNRISE_SUNSET_API_KEY")
open_notify_api_endpoint = os.getenv("OPEN_NOTIFY_API_ENDPOINT")
sunrise_sunset_api_endpoint = os.getenv("SUNRISE_SUNSET_API_ENDPOINT")
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")


# Validate all required environment variables
required_vars = {
    "LATITUDE": latitude,
    "LONGITUDE": longitude,
    "SUNRISE_SUNSET_API_KEY": sunrise_sunset_api_key,
    "OPEN_NOTIFY_API_ENDPOINT": open_notify_api_endpoint,
    "SUNRISE_SUNSET_API_ENDPOINT": sunrise_sunset_api_endpoint,
    "SENDER_EMAIL": sender_email,
    "RECEIVER_EMAIL": receiver_email,
    "SENDER_PASSWORD": sender_password,
}

missing_vars = [var for var, value in required_vars.items() if value is None]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")


def is_iss_overhead():
    try:
        response = requests.get(url=open_notify_api_endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS position: {e}")
        return False
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return False
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if latitude - 5 <= iss_latitude <= latitude + 5 and longitude - 5 <= iss_longitude <= longitude + 5:
        return True


def is_night():
    sunrise_sunset_params = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
    }
    try:
        response = requests.get(url=sunrise_sunset_api_endpoint, params=sunrise_sunset_params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sunrise/sunset data: {e}")
        return False
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return False

    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else: 
        return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=sender_email, password=sender_password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=receiver_email,
                    msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
                )
        except smtplib.SMTPAuthenticationError as e:
            print(f"SMTP authentication failed: {e}")
            exit(1)
        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
            exit(1)
        except Exception as e:
            print(f"Unexpected error sending email: {e}")
            exit(1)
    else:
        print("The ISS is not overhead and it is not nighttime.")