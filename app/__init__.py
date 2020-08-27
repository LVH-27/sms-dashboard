from flask import Flask
from config import Config
from os.path import exists
# from twilio.rest import Client
from csv import DictWriter


webhook_app = Flask(__name__) # ,
                    # static_url_path='',
                    # static_folder='static'
                    # )
webhook_app.config.from_object(Config)
# twilio_client = Client(webhook_app.config)

webhook_app.config['fields'] = ['from', 'body']

# initialize the CSV file
if not exists(webhook_app.config['CSV_PATH']):
    print("creating csv")
    with open(webhook_app.config['CSV_PATH'], 'w', newline='') as f:
        writer = DictWriter(f, fieldnames=webhook_app.config['fields'])
        writer.writeheader()
        print("wrote header")
    print("created csv")
else:
    print("not creating csv")

from app import routes  # noqa
