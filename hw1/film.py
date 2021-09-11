import sys
from typing import List, Union
import requests

url_base = 'https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/'


def main(argv: str) -> Union[List[dict], None]:
    # TODO: category, titles, release_year, rating(e.g., PG - 13), rental_rate, and rental_duration
    orderBy = 'orderBy=' + "\"" + "category" + "\""
    equalTo = 'equalTo=' + "\"" + argv.lower() + "\""
    url = url_base + 'FILMs' + '.json' + '?' + orderBy + '&' + equalTo
    result = [
        {
            "rating": v['rating'],
            "release_year": v['release_year'],
            "rental_duration": v['rental_duration'],
            "rental_rate": v['rental_rate'],
            "title": v['title'],
        } for k, v in requests.get(url).json().items()]
    result = sorted(result, key=lambda x: x['title'])
    return result


if __name__ == '__main__':
    # example
    # python cat.py action
    print(main(sys.argv[1]))
