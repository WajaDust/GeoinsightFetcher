import time
from api.get_city_info_by_name import get_city_info_by_name
from api.get_city_currencies import get_city_currencies


def log_city_info(cities_l):
    """
    Log City info

    :param cities_l: list of the cities names
    """
    for city_name in cities_l:
        cities_json, requests_amount_exceeded = get_city_info_by_name(city_name)

        if not requests_amount_exceeded:
            cities_response_amount = len(cities_json['data'])

            if cities_response_amount > 1:
                print("We found %s cities starting with the entered name: %s\n" % (cities_response_amount, city_name))

            if cities_response_amount == 0:
                print(city_name)
                print("----------")
                print("Invalid City Name\n")
            else:
                for city_dict in cities_json['data']:
                    city_name = city_dict["name"]
                    city_country = city_dict["country"]
                    city_country_code = city_dict["countryCode"]
                    city_currencies_list = get_city_currencies(city_country_code)

                    print(city_name)
                    print('----------')
                    print('Country: %s' % city_country)
                    print('Currency: %s' % ", ".join(city_currencies_list))
                    print('----------\n')

        # sleep is used because of Geo api Basic plan limitations (1 request per second)
        time.sleep(2)
