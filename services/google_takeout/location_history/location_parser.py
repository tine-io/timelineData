import json
from pathlib import Path
from datetime import datetime
from geojson import Point
import time
from services.database.db_connector import DBCollectionConnector

class LocationHistoryParser:
    def __init__(self, db_host: str, db_port: int, db_name, collection_name, user: str) -> None:
        self.db_connector: DBCollectionConnector = DBCollectionConnector(
            db_host, db_port, db_name, collection_name)
        print("DB Connected")
        self.user = user

    def parse_json_location_history(self, path: str):
        file: Path = self.get_loc_history_file(path)
        loc_hist_data: dict = json.load(file)
        locations_counter: int = 0
        location_hist_size = len(loc_hist_data["locations"])
        for google_location in loc_hist_data["locations"]:
            location: dict = self.create_location(google_location)
            locations_counter += 1
            if locations_counter % 10 == 0:
                print(f'Insert location number {locations_counter} of {location_hist_size} locations')
            self.db_connector.insert_location(location)

    def get_loc_history_file(self, path: str):
        file_path: Path = Path(path)
        if not file_path.is_file:
            raise RuntimeError(
                f'The specified path: {path} is not a file. Please provide a path to a google location history json file!')
        elif file_path.suffix != '.json':
            raise RuntimeError('Only Json files are accpeted')
        return file_path.open(encoding='utf-8')

    def create_location(self, google_location: dict) -> dict:
        location: dict = {}
        location['type'] = 'location'
        location['tst'] = datetime.fromtimestamp(float(google_location['timestampMs'])/1000)
        location['created_at'] = datetime.fromtimestamp(time.time())
        location['tracker'] = 'google_takeout'
        location['point'] = Point((float(google_location['latitudeE7']), float(google_location['longitudeE7'])))
        location['acc'] = google_location['accuracy']
        location['tid'] = google_location['deviceTag']
        if 'activity'  in google_location:
            location['activity'] = google_location['activity']
        location['user'] = self.user
        location['conn'] = (lambda x: 'w' if x == "WIFI" else (
            'c' if x == "CELL" else "o"))(google_location['source'])
        return location


if __name__ == '__main__':
    parser: LocationHistoryParser = LocationHistoryParser(
        'localhost', 27017, 'p2w2', "location_DB", "locations")
    parser.parse_json_location_history(
        "Takeout\Location History\Location History.json")
