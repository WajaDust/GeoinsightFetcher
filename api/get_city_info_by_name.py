import requests

from api.conf import API_URL, HEADERS


def get_city_info_by_name(city_name):
    """
    Getting city info

    :param city_name: Name of the city
    :return: Cities response (type=json) and requests_amount_exceeded (type=bool)

    requests_amount_exceeded is returned True if api Basic plan is exceeded
    """
    url = API_URL + "cities"
    querystring = {"namePrefix": city_name}
    cities_response = requests.request("GET", url, headers=HEADERS, params=querystring).json()
    requests_amount_exceeded = False
    try:
        print(cities_response['message'])
        requests_amount_exceeded = True
    except KeyError:
        pass
    return cities_response, requests_amount_exceeded
