import unittest
from api.services.stock_data_service import StockDataService

class StockDataServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = StockDataService()

    def test_get_batch_quotes(self):
        symbols = 'AAPL,IBM,FB'

        results = self.service.get_batch_quotes(symbols).json()

        self.assertIn('AAPL', results)
        self.assertIn('IBM', results)
        self.assertIn('FB', results)
        self.assertIsInstance(results['AAPL']['quote']['latestPrice'], float)
