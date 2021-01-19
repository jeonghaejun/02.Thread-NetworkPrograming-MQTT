from mqtt_sub import subscribe
from datetime import datetime
from app_base import Application

FILE_NAME = 'sesorvalues.csv'


def on_message(client, userdata, msg):
    with open(FILE_NAME, 'at') as f:
        f.write(f'{datetime.now()},{msg.topic},{float(msg.payload)}\n')


subscribe('localhost', 'iot/#', on_message)
