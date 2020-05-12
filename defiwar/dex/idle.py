from .common import append_params
from .common import execute_request


class Idle(object):

    base_endpoint = 'https://api.idle.finance/'

    aprs = 'aprs'
    rates = 'rates'

    def get_current_aprs(self, *args):
        url = self.base_endpoint + self.aprs
        url = append_params(url, *args)
        return execute_request(url)
    
    def get_historical_rates(self, token_address, *args):
        url = self.base_endpoint + self.aprs
        url = append_params(url, *args)