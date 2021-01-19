from mqtt_sub import subscribe


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


subscribe('localhost', 'iot/#', on_message)
