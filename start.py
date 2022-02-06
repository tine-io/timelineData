from services.owntracks.owntracks_mqtt_client import OwntracksMqttClient

if __name__ == '__main__':
    connection = OwntracksMqttClient('localhost', 27017, '192.168.178.81', 1883, 'p2w2', 'pocoLoco!300')