from services.owntracks.owntracks_mqtt_client import OwntracksMqttClient

if __name__ == '__main__':
    connection = OwntracksMqttClient(host, port, ip, port, user, secret)
