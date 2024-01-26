import configparser
import sys

config = configparser.ConfigParser()
config.read(sys.argv[1])

email = config['google_credentials']['email']
additional_query = config['google_credentials']['additional_query']
account_sid = config['twilio_credentials']['account_sid']
account_token = config['twilio_credentials']['account_token']
twilio_phone_number = config['twilio_credentials']['twilio_phone_number']
to_phone_number = config['twilio_credentials']['to_phone_number']
