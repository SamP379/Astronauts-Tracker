import requests
import nlp_utils
import scraper_utils


class Astronauts:
    """A class to represent the astronauts currently in space"""

    ENDPOINT = "http://api.open-notify.org/astros.json"
    WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
    
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
    

    def were_found(self):
        """Returns True if the dictionary of astronauts was successfully loaded"""
        if self.astronauts is not None:
            return True
        return False
    

    def display(self):
        """Displays the names of the astronauts currently in space"""
        print(f"\nNumber of people in space: {self.astronauts["number"]}")
        print("\n\nAstronauts:\n")
        for astronaut in self.astronauts["people"]:
            current_astronaut = astronaut["name"]
            print(current_astronaut)
    

    def check_astronaut(self, astronaut_name : str) -> bool:
        """Checks if an astronaut name is in the dict of astronauts in space"""
        for astronaut in self.astronauts["people"]:
            current_astronaut = astronaut["name"].lower()
            if astronaut_name.lower() == current_astronaut:
                return True
        return False
    
 
    def get_description(self, astronaut_name : str) -> str|None:
        """Gets a description of a given astronaut from their Wikipedia article"""
        if self.check_astronaut(astronaut_name):
            astronaut_name = astronaut_name.title()
            split_name = astronaut_name.split(" ")
            formatted_name = "_".join(split_name)
            url = Astronauts.WIKIPEDIA_URL + formatted_name
            astronaut_article = scraper_utils.article_text(url)
            if astronaut_article is not None:
                article_summary = nlp_utils.summarize_text(astronaut_article)
                return article_summary
            else:
                return None
        else:
            return None