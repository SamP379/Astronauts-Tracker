import requests


class Astronauts:
    """A class to represent the astronauts currently in space"""

    ENDPOINT = "http://api.open-notify.org/astros.json"
    
    def __init__(self):
        self.astronauts = self.get_astronauts()


    def get_astronauts(self) -> dict|None:
        """Returns a dictionary of the astronauts currently in space"""
        try:
            response = requests.get(url = Astronauts.ENDPOINT)
            content = response.json()
            return content
        except Exception:
            return None
    

    def was_found(self):
        """Returns True if the dictionary of astronauts was successfully loaded"""
        if self.astronauts is not None:
            return True
        return False