import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class StockDataService:

    def get_batch_quotes(self, symbol_string):
        response = requests.get(
            'https://sandbox.iexapis.com'
            '/stable/stock/market/batch'
            f'?symbols={symbol_string}'
            '&types=quote'
            f"&token={os.getenv('IEX_CLOUD_TOKEN')}"
        )

        if response.status_code == 200:
            return response
        else:
            raise requests.RequestException
