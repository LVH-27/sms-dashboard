import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'please_change-this_secret_key'
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    CSV_PATH = os.environ.get('CSV_PATH') or 'sms_list.csv'
    FIELDS = ['from', 'body']
