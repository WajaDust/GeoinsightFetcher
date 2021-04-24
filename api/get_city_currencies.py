import time
import requests

from api.conf import API_URL, HEADERS


def get_city_currencies(city_country_code):
    """
    Get City currencies list

    :param city_country_code: Country code of the city, located in it
    :return: List of country currencies
    """

    # sleep is used because of Geo api Basic plan limitations (1 request per second)
    time.sleep(2)
    url = API_URL + "countries/%s" % city_country_code
    response = requests.request("GET", url, headers=HEADERS)
    currencies_list = response.json()['data']['currencyCodes']
    return currencies_list
