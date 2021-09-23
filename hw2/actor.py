# package imports
# e.g.
# import pandas as pd
# ...
import sys
from typing import List, Union, Dict
from lxml import etree

database_path = 'main.xml'


def main(argv: str) -> Union[Dict[str, List[dict]], None]:
    tree = etree.parse(database_path)
    root = tree.getroot()
    actor_ids = find_all_actor_ids(root, argv.split(' '))
    actor_films_dict = find_actor_films_dict(root, actor_ids)
    return None if len(actor_films_dict) == 0 else actor_films_dict


def find_all_actor_ids(root, first_last_name):
    first_name = first_last_name[0]
    last_name = first_last_name[1]
    query = "//actor_table/actor" + \
            "[" + \
            "first_name=" + "\'" + first_name + "\'" + \
            " and " + \
            "last_name=" + "\'" + last_name + "\'" + \
            "]"
    actor_ids = [element.find('./actor_id').text for element in root.xpath(query)]
    return actor_ids


def find_actor_films_dict(root, actor_ids):
    actor_films_dict = {}
    for actor_id in actor_ids:
        query = "//film_actor_table/film_actor" + "[" + "actor_id=" + "\'" + actor_id + "\'" + "]"
        film_ids = [element.xpath('film_id')[0].text for element in root.xpath(query)]
        film_infos = []
        for film_id in film_ids:
            query = "//film_table/film" + "[" + "film_id=" + "\'" + film_id + "\'" + "]"
            film_element = root.xpath(query)[0]
            film_info = {
                'title': film_element.xpath('title')[0].text,
                'release_year': film_element.xpath('release_year')[0].text
            }
            film_infos.append(film_info)
        actor_films_dict[actor_id] = film_infos
    return actor_films_dict


if __name__ == '__main__':
    # example
    # python actor.py 'ed chase'
    print(main(sys.argv[1]))
