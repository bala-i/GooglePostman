import sys
from utils.googlepostman import GooglePostman
from utils.twilio import Twilio
from utils.parcer import *
import csv
import datetime as dt


try:
    this_moment = dt.datetime.today().strftime(' %H:%M %m/%d/%Y')
    postman = GooglePostman()
    date = str(dt.date.today())
    querry = f"newer: {date}" + " " + additional_query

    # get the Gmail API service
    res = postman.search_messages(postman.service, f"{querry}")
    print(res)

    # check Gmail API service response and do some logic with Twilio API
    if res:
        twilio = Twilio()
        twilio.send_message("Are we there yet? Check email")
        status = "Twilio alert triggerd"
    else:
        status = "We're not there yet"
except Exception as e:
    twilio = Twilio()
    status = "An exception occurred:" + str(e)
    twilio.send_message(f"{status}, check code")
    print(status)
finally:
    with open('log.csv', 'a', newline='') as log:
        writer_object = csv.writer(log)
        writer_object.writerow([status, this_moment])

