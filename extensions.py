import requests
import json

class APIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CurrencyConverter:
    @staticmethod
    def get_data(api_url):
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise APIException(f"Error when requesting currency rates. Status code: {response.status_code}")

    @staticmethod
    def get_exchange_rate(api_url, source_currency, target_currency, amount):
        data = CurrencyConverter.get_data(api_url)

        if source_currency in data['data'] and target_currency in data['data']:
            source_exchange_rate = data['data'][source_currency]
            target_exchange_rate = data['data'][target_currency]
            converted_amount = (amount / source_exchange_rate) * target_exchange_rate
            return converted_amount
        else:
            raise APIException("Source or target currency not found in the data.")