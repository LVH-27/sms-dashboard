import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'please_change-this_secret_key'
    CSV_PATH = os.environ.get('CSV_PATH') or 'sms_list.csv'
    FIELDS = ['from', 'body']
