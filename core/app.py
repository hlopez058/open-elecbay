
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json
from datetime import datetime, timedelta

# Example market requests
# Should be managed as a queue by a brokerage thread
#
# MARKET_REQUESTS = {
#     "8c36e86c-13b9-4102-a44f-646015dfd981": {
#         'type': 'INFO',
#         'message': u'Test request',
#         'timestamp': (datetime.today() - timedelta(1)).timestamp()
#     }
# }

# Description:
# connect to the INFO topic and return the message within as a metric from the customer
# this broker should return a payment for the energy of the customer as well
# based on the NRG algorithm
# have the system read messages and then
mqttBroker = "mosquitto"  # "iot.eclipse.org" #"test.mosquitto.org"
mqttPort = 1883  # port for mosquitto broker
client = mqtt.Client("open-elecbay-market-broker")  # create new instance


def main():
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    client.connect(mqttBroker, mqttPort, 60)  # Connect to the broker
    client.loop_forever()  # Start networking daemon


# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    # Print result of connection attempt
    print("Connected with result code {0}".format(str(rc)))
    # Subscribe to the topic “digitest/test1”, receive any messages published on it
    client.subscribe("INFO")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " +
          str(msg.payload))  # Print a received msg
    obj = json.loads(msg.payload)
    client.publish("METRICS", obj['message'])


if __name__ == '__main__':
    main()
