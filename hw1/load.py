import pandas as pd
import requests
import json
import sys

film_csv_path = 'film.csv'
film_actor_csv_path = 'film_actor.csv'
film_category_csv_path = 'film_category.csv'
actor_csv_path = 'actor.csv'
category_csv_path = 'category.csv'
global_separator = ';'
url_base = 'https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/'


def main() -> None:

    # TODO: actor name, title and release years of all films
    cols_film_df = ['film_id', 'title', 'release_year', 'rating', 'rental_rate', 'rental_duration']
    film_dict_list = load_csv_as_dict_list(film_csv_path, global_separator, cols_film_df)

    # Add index
    film_dicts_indexed = add_index(film_dict_list, 'film_id')

    # Add category
    add_category(film_dicts_indexed)

    # Add actor
    add_actor(film_dicts_indexed)

    # Load to firebase
    load_to_firebase(film_dicts_indexed)


def load_to_firebase(film_dicts_indexed):
    for film_id, film_dict in film_dicts_indexed.items():
        url = url_base + "FILMs/" + str(film_id) + '.json'
        json_str = json.dumps(film_dict, indent=4)
        res = requests.put(url, json_str)


def load_csv_as_dict_list(csv_path, separator, cols):
    df = pd.read_csv(csv_path, sep=separator, usecols=cols)
    return df.to_dict(orient='records')


def add_index(dict_list, key):
    dicts_indexed = {}
    for cur_dict in dict_list:
        dicts_indexed[cur_dict[key]] = cur_dict
    return dicts_indexed


def add_category(film_dicts_indexed):
    film_category_dict_list = load_csv_as_dict_list(
        film_category_csv_path,
        global_separator,
        ['film_id', 'category_id']
    )
    category_dict_list = load_csv_as_dict_list(category_csv_path, global_separator, ['category_id', 'name'])
    category_dicts_indexed = add_index(category_dict_list, 'category_id')
    for film_category_dict in film_category_dict_list:
        category_name = category_dicts_indexed[film_category_dict['category_id']]['name']
        film_dicts_indexed[film_category_dict['film_id']]['category'] = category_name


def add_actor(film_dicts_indexed):
    film_actor_dict_list = load_csv_as_dict_list(film_actor_csv_path, global_separator, ['film_id', 'actor_id'])
    actor_dict_list = load_csv_as_dict_list(actor_csv_path, global_separator, ['actor_id', 'first_name', 'last_name'])
    actor_dicts_indexed = add_index(actor_dict_list, 'actor_id')
    for film_actor_dict in film_actor_dict_list:
        actor_name = actor_dicts_indexed[film_actor_dict['actor_id']]['first_name'] + ' ' + \
                     actor_dicts_indexed[film_actor_dict['actor_id']]['last_name']
        film_dicts_indexed[film_actor_dict['film_id']]['actor'] = actor_name


if __name__ == '__main__':
    main()
