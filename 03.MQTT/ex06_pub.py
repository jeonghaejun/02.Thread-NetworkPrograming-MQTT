from sensor import Sensor


sensors = [
    Sensor(5, (3, 10), 'iot/user1/temp'),
    Sensor(7, (20, 60), 'iot/user1/humi'),
    Sensor(10, (20, 80), 'iot/user1/illu'),
    Sensor(12, (0, 1), 'iot/user1/dust'),
]

for sensor in sensors:
    sensor.start()
