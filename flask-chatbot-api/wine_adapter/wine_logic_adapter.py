"""
    A logic adapter that returns information regarding the wine and breweries.Currently, only basic information
    about wine is returned, but additional features are planned in the future.
"""
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import requests


class WineLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):

        super().__init__(chatbot, **kwargs)

    def process(self, statement, additional_response_selection_parameters=None):
        """
        Returns the detail of wine form api call.
        """
        user_input = statement.text
        winery_word = ['Brewing', 'Brewery', 'Brewers']
        if any(x in user_input for x in winery_word):
            url = "https://brianiswu-open-brewery-db-v1.p.rapidapi.com/breweries"

            headers = {
                'x-rapidapi-host': "brianiswu-open-brewery-db-v1.p.rapidapi.com",
                'x-rapidapi-key': "ebc6229d48mshff261bbd67ecb2fp13a1d8jsn7469f7db79dc"
            }

            response = requests.request("GET", url, headers=headers)
            data = response.json()

            brew_result = ''

            if response.status_code == 200:
                confi = 1
            else:
                confi = 0
            for brew in data:

                if brew['name'].lower() == user_input.lower():
                    brew_result = brew
                    break
            response_statement = Statement(brew_result)
            response_statement.confidence = confi

            return response_statement
        else:
            response_statement = Statement('')
            response_statement.confidence = 0

            return response_statement
