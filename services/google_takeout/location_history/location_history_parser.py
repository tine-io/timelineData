import os
import json
from pathlib import Path
from datetime import datetime
from services.database.db_connector import DBConnector
from pymongo import MongoClient
from geojson import Point


class LocationHistoryParser:
    def __init__(self, db_host: str, db_port: int, user: str) -> None:
        self.db_client = MongoClient(db_host, db_port)
        self.db_connector = DBConnector(self.db_client)
        self.user = user

    def parse_json_location_history(self, path: str, user: str):
        file: Path = self.get_loc_history_file(path)
        loc_hist_data: dict = json.load(file)
        locations_counter: int = 0
        for google_location in loc_hist_data["locations"]:
            location = self.create_location(google_location)
            self.db_connector.insert_location(location)
            locations_counter=+1
        print("Succesfuly added " + locations_counter + " locations to the database")


    def get_loc_history_file(self, path: str):
        file_path = Path(path)
        if not file_path.is_file:
            raise RuntimeError('The specified path: "' + path +
                               '" is not a file. Please provide a path to a google location history json file!')
        elif file_path.suffix != '.json':
            raise RuntimeError('Only Json files are accpeted')
        return file_path.open(encoding='utf-8')
    
    def create_location(self, google_location: dict):
        location: dict = {}
        location['type'] = 'location'
        location['tst'] = datetime.utcfromtimestamp(
            int(google_location['timestampMs']))
        location['tracker'] = 'google_takeout'
        location['point'] = Point(
            float(google_location['latitudeE7'])), (float(google_location['longitudeE7']))
        location['acc'] = google_location['accuracy']
        location['tid'] = google_location['deviceTag']
        location['activity'] = google_location['activity']
        location['user'] = self.user
        location['conn'] = (lambda x: 'w' if x == "WIFI" else ('c' if x == "CELL" else "o"))(google_location['source'])
        