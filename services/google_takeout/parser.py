import os
import json
from pathlib import Path
from services.google_takeout.db_connector import ParserDBConnector
from pymongo import MongoClient

class Parser:
    def __init__(self):
        self.db_client = MongoClient('localhost', 27017)
        self.parser_db_connector = ParserDBConnector(self.db_client)

    def parse_googl_semantic_loc_hist(self, file_type=".json"):
        path = Path(os.environ['TAKEOUT'] + '\Semantic Location History')
        if path.is_file() and path.suffix == file_type:
            self.parse_google_json_sem_loc_hist_file(path.open(encoding='utf-8'))
        for val in path.rglob('*'):
            if val.is_dir():
                print(val)
            elif val.suffix == file_type:
                self.parse_google_json_sem_loc_hist_file(
                    val.open(encoding='utf-8'))

    def parse_google_json_sem_loc_hist_file(self, file):
        data = json.load(file)
        visit_places = []
        activity_segments = []
        for location_obj in data['timelineObjects']:
            if 'placeVisit' in location_obj:
                visit_places.append(location_obj['placeVisit'])
            elif 'activitySegment' in location_obj:
                activity_segments.append(location_obj['activitySegment'])
            else:
                print('Type not known: ' + location_obj)
        self.parser_db_connector.insert_visit_places(visit_places)
        self.parser_db_connector.insert_activity_segments(activity_segments)
    
    def parse_google_json_loc_history(self):
        path = Path(os.environ['TAKEOUT'] + '\Locations.json')
        data = json.load(path.open(encoding='utf-8'))
        self.db_client.insert_locations(data['locations'])


if __name__ == '__main__':
    parser = Parser()
    parser.parse_google_json_loc_history()
