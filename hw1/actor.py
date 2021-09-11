import sys
from typing import List, Union, Dict
import requests

url_base = 'https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/'


def main(argv: str) -> Union[Dict[str, List[dict]], None]:
    # TODO: actor name, title and release years of all films
    orderBy = 'orderBy=' + "\"" + "actor_name" + "\""
    equalTo = 'equalTo=' + "\"" + argv.lower() + "\""
    url = url_base + 'ACTORs' + '.json' + '?' + orderBy + '&' + equalTo
    print(url)
    result = make_result(requests.get(url).json())
    return result


def make_result(response_dict):
    result = {}
    for k, v in response_dict.items():
        result[k] = sorted(v['films'], key=lambda x: x['title'])
    return result


if __name__ == '__main__':
    # example
    # python actor.py 'ed chase'
    print(main(sys.argv[1]))
