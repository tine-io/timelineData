import json
from paho.mqtt.client import Client, MQTTMessage
from pymongo import MongoClient
from datetime import datetime
from geojson import Point
from services.owntracks.mqtt_db_connector import MqttDBConnector

class OwntracksMqttClient():
    
    def __init__(self, db_host: str, db_port: int, broker_host: str, broker_port: int, mqtt_username: str, mqtt_password: str) -> None:
        self.client = Client()
        self.client.username_pw_set(username=mqtt_username,password=mqtt_password)
        self.client.connect(broker_host, broker_port, 60)
        self.db_connector = MqttDBConnector( MongoClient(db_host, db_port), "location_DB", "locations")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever()

    def on_connect(self, client: Client, userdata, flags, rc) -> None:
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe("owntracks/+/+")

    # The callback for when a PUBLISH message is received from the server.


    def on_message(self, client: Client, userdata, msg: MQTTMessage) -> None:
        location: dict = json.loads(msg.payload.decode('utf-8'))
        topics: list = msg.topic.split('/')
        
        location['user'] = topics[1]
        location['tracker'] = topics[2]
        location['created_at'] = datetime.utcfromtimestamp(int(location['created_at']))
        location['point'] = Point(float(location['lat'])), (float(location['lon']))
        del location['lon'], location['lat']
        
        self.db_connector.insert_location(location)