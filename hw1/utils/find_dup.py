import pandas as pd
import requests
import json
from collections import defaultdict

film_csv_path = 'film.csv'
film_actor_csv_path = 'film_actor.csv'
film_category_csv_path = 'film_category.csv'
actor_csv_path = 'actor.csv'
category_csv_path = 'category.csv'
global_separator = ';'
url_base = 'https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/'


def main():
    actor_dict_list = load_csv_as_dict_list(actor_csv_path, global_separator, ['actor_id', 'first_name', 'last_name'])
    actor_dicts_indexed = add_index(actor_dict_list, 'actor_id')
    actor_dicts_indexed = {k: {
        'actor_id': v['actor_id'],
        'actor_name': (v['first_name'] + ' ' + v['last_name']).lower(),
        'films': []
    } for k, v in actor_dicts_indexed.items()}
    name_dict = defaultdict(lambda: 0)
    for k, v in actor_dicts_indexed.items():
        name_dict[v['actor_name']] += 1
        if name_dict[v['actor_name']] > 1:
            print(v['actor_name'])


def load_csv_as_dict_list(csv_path, separator, cols):
    df = pd.read_csv(csv_path, sep=separator, usecols=cols)
    return df.to_dict(orient='records')


def add_index(dict_list, key):
    dicts_indexed = {}
    for cur_dict in dict_list:
        dicts_indexed[cur_dict[key]] = cur_dict
    return dicts_indexed


if __name__ == '__main__':
    main()
