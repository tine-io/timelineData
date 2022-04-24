#from services.owntracks.owntracks_mqtt_client import OwntracksMqttClient

from services.google_takeout.location_history.location_parser import LocationHistoryParser

if __name__ == '__main__':
    # connection = OwntracksMqttClient('localhost', 27017, '192.168.178.81', 1883, 'p2w2', 'pocoLoco!300')
    parser: LocationHistoryParser = LocationHistoryParser(
        'localhost', 27017, "location_DB", "locations", 'p2w2')
    parser.parse_json_location_history(
        "Takeout\Location History\Location History.json")