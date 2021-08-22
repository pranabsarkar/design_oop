import logging

log = logging.Logger()

class Database:
    def __init__(self) -> None:
        self.load_data()
    
    def load_data(self):
        self.data = {
            1: {"name": "pranab"},
            2: {"name": "john"}
        }
    
    def get_item(self, id):
        """Returns back data for the given id"""
        if id in self.data:
            return {
                "data": self.data[id],
                "message": "Id found"
            }
        else:
            return {
                "message": "Id is not present",
                "data": None
            }
    
    def add_item(self, **params):
        if params['id'] in self.data:
            log.debug(f"[{params['id']}] already present in database")
            if 'force_add' not in params:
                log.debug(f"database not updated")
            elif params["force_add"] is True:
                self.data[params['id']] = params['data']
                log.debug(f"database updated")
        else:
            self.data[params['id']] = params['data']
            log.debug(f"database updated")
