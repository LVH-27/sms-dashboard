from flask import render_template, request
from app import webhook_app
from csv import DictReader, DictWriter
from twilio.twiml.messaging_response import MessagingResponse


@webhook_app.route('/')
@webhook_app.route('/list/')
def list():
    data = []
    with open(webhook_app.config['CSV_PATH'], 'r', newline='') as f:
        for row in DictReader(f):
            print(row)
            data.append(row)
    return render_template("index.html", title='SMS List', data=data, fields=webhook_app.config['FIELDS'])


@webhook_app.route('/post/', methods=['POST'])
def post():
    print("received sms")
    sms = request.values
    print(sms)
    with open(webhook_app.config['CSV_PATH'], 'a', newline='') as f:
        writer = DictWriter(f, fieldnames=webhook_app.config['FIELDS'])
        writer.writerow({'from': sms['From'], 'body': sms['Body']})
    print("written")
    return str(MessagingResponse())  # send empty response, meaning "do nothing"
