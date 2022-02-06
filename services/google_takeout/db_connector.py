class ParserDBConnector:
    def __init__(self, client) -> None:
        self.client = client
        self.db = client['test_database']

    def insert_activity_segments(self, segment):
        print('insert activties')
        collection = self.db['activity_segments']
        collection.insert_many(segment)

    def insert_visit_places(self, places):
        print('insert places')
        collection = self.db['places_visit']
        collection.insert_many(places)

    def insert_locations(self, locations):
        print('insert location')
        collection = self.db['locations']
        collection.insert_many(locations)