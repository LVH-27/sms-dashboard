# sms-dashboard
Example Flask app serving as a Twilio webhook

The app contains two endpoints:
* /list - a GET endpoint, simply listing the SMS messages from a CSV file, and
* /post - a POST endpoint, which receives form data containing the From and Body fields of an SMS, to be used as a Twilio webhook.

Normally, a database would be used, but for simplicity of persistence, a CSV file is being used.
