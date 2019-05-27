import paho.mqtt.client as mqtt
from threading import Thread


def on_publish(client, userdata, result):  # create function for callback
    return True


def publish(broker_address="localhost", port=1883, topic="default_topic", message="test", client_name="default_client",
            on_publish_function=on_publish):
    publisher = mqtt.Client(client_name)  # create client object
    publisher.on_publish = on_publish_function  # assign function to callback
    publisher.connect(broker_address, port)  # establish connection
    publisher.publish(topic, message)
    return True


def basic_publish(topic="default_topic", message="default_message"):
    publisher = mqtt.Client("Basic")
    publisher.connect("localhost", 1883)
    publisher.publish(topic, message)


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)



def subscribe(broker_address="localhost", port=1883, topic="default_topic", client_name="default_client",
              on_message_function=on_message):
    subscriber = mqtt.Client(client_name)
    subscriber.on_message = on_message_function
    subscriber.connect(broker_address, port)
    subscriber.subscribe(topic)
    return subscriber

def basic_subscribe(topic="default_topic", on_message_function=on_message):
    subscriber = mqtt.Client("Basic")
    subscriber.on_message = on_message_function
    subscriber.connect("localhost", 1883)
    subscriber.subscribe(topic)
    return subscriber
