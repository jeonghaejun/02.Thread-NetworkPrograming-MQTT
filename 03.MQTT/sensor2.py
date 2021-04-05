from threading import Thread
import paho.mqtt.client as mqtt
import random
import time

HOST = 'localhost'

class Sensor(Thread):
    def __init__(self, topic):
        super().__init__()
        
        self.topic = topic
        self.client = mqtt.Client()

    def run(self):
        self.client.connect(HOST)
        while True:
            time.sleep(1)
            value = "on"
            # 토픽발행
            print(self.topic, value)
            self.client.publish(self.topic, value)
            value = "off"
            # 토픽발행
            print(self.topic, value)
            self.client.publish(self.topic, value)
            self.client.loop(2)


if __name__ == "__main__":
    temp_sensor = Sensor('iot/pir')
    temp_sensor.start()
