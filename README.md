# ISS Overhead Notifier

A Python application that tracks the International Space Station (ISS) and notifies you when it's visible in your night sky. This tool helps astronomy enthusiasts and space lovers know exactly when to look up and spot the ISS passing overhead.

## Features

- Real-time ISS position tracking using the Open Notify API
- Automatic night detection using the Sunrise-Sunset API
- Email notifications when the ISS is overhead during nighttime
- Environment variable configuration for secure credential management
- Comprehensive error handling for API and email operations
- Easy to automate with task schedulers or continuous monitoring

## Requirements

- Python 3.x
- Gmail account with App Password enabled
- API access (Open Notify API and Sunrise-Sunset API)
- Required Python packages (see `requirements.txt`):
  - `python-dotenv` - For loading environment variables
  - `requests` - For making API calls to fetch ISS position and sunrise/sunset data
  - `smtplib` - Built into Python standard library for email sending

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/ISS_overhead.git
cd ISS_overhead
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
LATITUDE=your_latitude_here
LONGITUDE=your_longitude_here
SUNRISE_SUNSET_API_KEY=your_api_key_here
OPEN_NOTIFY_API_ENDPOINT=http://api.open-notify.org/iss-now.json
SUNRISE_SUNSET_API_ENDPOINT=https://api.sunrise-sunset.org/json
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=recipient@example.com
SENDER_PASSWORD=your_gmail_app_password
```

**Important:**

- Replace all placeholder values with your actual credentials
- Never commit the `.env` file to version control
- For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password
- You can get a free API key from [Sunrise-Sunset API](https://sunrise-sunset.org/api) if required
- The Open Notify API endpoint is public and doesn't require an API key

## Usage

To run the script:

```bash
python main.py
```

### How It Works

1. The script loads environment variables from `.env` file
2. Validates that all required environment variables are present
3. Checks the current ISS position using the Open Notify API
4. Determines if it's nighttime at your location using the Sunrise-Sunset API
5. If the ISS is overhead (within ±5 degrees of your location) and it's nighttime, sends an email notification
6. The email includes:
   - Subject: "Look Up👆"
   - Body: "The ISS is above you in the sky."

### Error Handling

The script includes comprehensive error handling for:

- Missing environment variables
- API request failures (network errors, timeouts, HTTP errors)
- JSON parsing errors
- SMTP authentication failures
- General SMTP errors
- Unexpected exceptions

## Setting Up Automated Execution

To run this script automatically on a schedule, you can:

1. **Windows Task Scheduler**: Create a scheduled task to run the script at specified intervals (e.g., every 60 seconds or every minute)
2. **Linux/Mac Cron Jobs**: Add a cron job to execute the script at specified intervals
3. **Cloud Services**: Deploy to AWS Lambda, Google Cloud Functions, or similar services with scheduled triggers
4. **GitHub Actions**: Set up a scheduled workflow to run the script
5. **Continuous Loop**: Modify the script to run in a continuous loop with a sleep interval

Example cron job (runs every minute):

```bash
* * * * * /usr/bin/python3 /path/to/ISS_overhead/main.py
```

## Security Notes

- **Never commit your `.env` file** to version control - it contains sensitive credentials
- Use Gmail's App Passwords instead of your main account password
- Keep your API keys secure and rotate them periodically if compromised
- Consider using a secrets management service for production deployments
- The `.env` file is already included in `.gitignore` to prevent accidental commits

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
