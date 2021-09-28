# package imports
# e.g.
# import pandas as pd
# ...
import sys
from typing import List, Union
from lxml import etree

database_path = 'main.xml'
cols_film = ['title', 'release_year', 'rating', 'rental_rate', 'rental_duration']


def main(argv: str) -> Union[List[dict], None]:
    tree = etree.parse(database_path)
    root = tree.getroot()
    film_ids = find_all_film_ids(root, argv.lower())
    result = find_films(root, film_ids)
    return None if len(result) == 0 else result


def find_all_film_ids(root, category):
    query = "./category_table/category/" + "[" + "name=" + "\'" + category + "\'" + "]"
    query_result = root.findall(query)
    if len(query_result) == 0:
        return []
    category_id = query_result[0].find('./category_id').text
    query = "./film_category_table/film_category/" + "[" + "category_id=" + "\'" + category_id + "\'" + "]"
    film_ids = [element.find('./film_id').text for element in root.findall(query)]
    return film_ids


def find_films(root, film_ids):
    result = []
    for film_id in film_ids:
        query = "./film_table/film/" + "[" + "film_id=" + "\'" + film_id + "\'" + "]"
        film_element = root.find(query)
        to_res = {
            'title': film_element.find('./title').text,
            'release_year': film_element.find('./release_year').text,
            'rental_duration': film_element.find('./rental_duration').text,
            'rental_rate': film_element.find('./rental_rate').text,
            'rating': film_element.find('./rating').text,
        }
        result.append(to_res)
    return sorted(result, key=lambda x: x['title'])


if __name__ == '__main__':
    # example
    # python actor.py action
    print(main(sys.argv[1]))
