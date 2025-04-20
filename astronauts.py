import requests


ASTRONAUTS_ENDPOINT = "http://api.open-notify.org/astros.json"


def get_astronauts() -> dict|None:
    """Returns a dictionary of the astronauts currently in space"""
    try:
        response = requests.get(url = ASTRONAUTS_ENDPOINT)
        content = response.json()
        return content
    except Exception:
        return None