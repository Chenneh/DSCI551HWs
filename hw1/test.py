import pandas as pd
import requests
import json
import sys

actor_csv_path = 'actor.csv'
film_csv_path = 'film.csv'
url_base = 'https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/'
seperator = '/'

if __name__ == '__main__':
    # actor_df = pd.read_csv(actor_csv_path, nrows=3, sep=";")
    # print(actor_df)
    #
    # print(actor_df['last_name'][0:2])
    #
    # actor_json = actor_df.to_json(orient='records')
    # output_json = {'Actors': json.loads(actor_json)}
    # with open('test_res.json', 'w', encoding='utf-8') as outfile:
    #     json.dump(output_json, outfile)
    #     outfile.close()
    # with open('test_res.json', 'r') as json_file:
    #     json_back = json.load(json_file)
    #     json_file.close()
    # print(json_back)

    film_df = pd.read_csv(film_csv_path, nrows=3, sep=";")
    film_dict_list = film_df.to_dict(orient='records')
    print(film_dict_list[0]['title'])

    film_id = film_dict_list[0]['film_id']
    url = url_base + "FILMs/" + str(film_id) + '.json'
    film_0_json_str = json.dumps(film_dict_list[0], indent=4)

    res = requests.put(url, film_0_json_str)

    print(res)
    # url = url_base + 'FILMs' + '.json'
    # url = url_base + 'FILMs' + '.json' + '?' + orderBy
    # url = url_base + 'FILMs' + '.json' + '?' + orderBy + '&' + "startAt=" + '\"' + "0" + '\"'