# ISS Overhead Notifier

A Python application that tracks the International Space Station (ISS) and notifies you when it's visible in your night sky. This tool helps astronomy enthusiasts and space lovers know exactly when to look up and spot the ISS passing overhead.

## Features

- Real-time ISS position tracking using the Open Notify API
- Automatic night detection using sunrise/sunset data
- Email notifications when the ISS is visible
- Configurable location settings
- Continuous monitoring with automatic checks
- Easy-to-use setup with minimal configuration

## Requirements

- Python 3.x
- Required Python packages (automatically installed via requirements.txt):
  - requests==2.32.3
  - certifi==2024.7.4
  - charset-normalizer==3.3.2
  - idna==3.7
  - urllib3==2.2.2
  - six==1.16.0

## Installation

1. Clone this repository:

```bash
git clone https://github.com/momed-ali01/ISS_overhead.git
cd ISS_overhead
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to configure your settings in `main.py`:

1. Set your email credentials:

   - `MY_EMAIL`: Your Gmail address
   - `MY_PASSWORD`: Your Gmail app password (not your regular password)

2. Set your location coordinates:
   - `MY_LAT`: Your latitude
   - `MY_LONG`: Your longitude

## Usage

Run the application:

```bash
python main.py
```

The program will:

1. Check the ISS position every 60 seconds
2. Verify if it's nighttime at your location
3. Send you an email notification when the ISS is overhead during nighttime

### How It Works

- The application uses the Open Notify API to track the ISS position
- It considers the ISS "overhead" when it's within ±5 degrees of your location
- Nighttime is determined using the sunrise-sunset API
- Email notifications are sent using Gmail's SMTP server

## Email Notifications

When the ISS is visible:

- You'll receive an email with the subject "Look Up👆"
- The email will be sent to the address specified in `MY_EMAIL`
- Make sure to use an App Password if you have 2FA enabled on your Gmail account

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Open Notify API for ISS position data
- Sunrise-Sunset API for day/night information
- Python's built-in libraries for email functionality
