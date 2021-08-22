from database import Database


class Singleton:
    def __init__(self) -> None:
        self.db = Database()
    
    def get_records(self, id):
        return self.db.get_item(id=id)
    
    def add_record(self, id):
        self.db.add_item(
            id=3,
            data={
                "name": "ramesh"
            }
        )