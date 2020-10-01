from flask import Flask
from config import Config
from os.path import exists
from csv import DictWriter


webhook_app = Flask(__name__)
webhook_app.config.from_object(Config)

# initialize the CSV file
if not exists(webhook_app.config['CSV_PATH']):
    print("creating csv")
    with open(webhook_app.config['CSV_PATH'], 'w', newline='') as f:
        writer = DictWriter(f, fieldnames=webhook_app.config['FIELDS'])
        writer.writeheader()
        print("wrote header")
    print("created csv")
else:
    print("not creating csv")

from app import routes  # noqa
