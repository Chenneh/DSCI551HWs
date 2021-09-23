# package imports
# e.g.
# import pandas as pd
# ...

from lxml import etree
from xml.dom import minidom
import pandas as pd

film_csv_path = 'film.csv'
film_actor_csv_path = 'film_actor.csv'
film_category_csv_path = 'film_category.csv'
actor_csv_path = 'actor.csv'
category_csv_path = 'category.csv'
global_separator = ';'
cols_film = ['title', 'release_year', 'rating', 'rental_rate', 'rental_duration', 'category']
cols_actor = ['actor_id', 'actor_name', 'films']


def main() -> None:
    # make root
    root = etree.Element("root")
    # build film table
    film_dicts_indexed = make_film_dicts_indexed()
    film_table = indexed_dicts_to_table(film_dicts_indexed, 'film')
    root.append(film_table)

    # build actor table
    actor_dicts_indexed = make_actor_dicts_indexed(film_dicts_indexed)
    actor_table = indexed_dicts_to_table(actor_dicts_indexed, 'actor')
    root.append(actor_table)

    write_to_file_xml(root)


def indexed_dicts_to_table(indexed_dicts, element_type):
    table = etree.Element(element_type + "_table")
    used_cols = cols_film
    if element_type == 'actor':
        used_cols = cols_actor

    for k, v in indexed_dicts.items():
        new_element = etree.Element(element_type, id=str(k))
        for col in used_cols:
            new_element_property = etree.Element(col)
            new_element_property.text = str(v[col])
            new_element.append(new_element_property)
        table.append(new_element)
    return table


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
        film_dicts_indexed[film_category_dict['film_id']]['category'] = category_name.lower()
    return film_dicts_indexed


def make_film_dicts_indexed():
    cols_film_df = ['film_id', 'title', 'release_year', 'rating', 'rental_rate', 'rental_duration']
    film_dict_list = load_csv_as_dict_list(film_csv_path, global_separator, cols_film_df)
    film_dicts_indexed = add_index(film_dict_list, 'film_id')
    film_dicts_indexed = add_category(film_dicts_indexed)
    return film_dicts_indexed


def make_actor_dicts_indexed(film_dicts_indexed):
    film_actor_dict_list = load_csv_as_dict_list(film_actor_csv_path, global_separator, ['film_id', 'actor_id'])
    actor_dict_list = load_csv_as_dict_list(actor_csv_path, global_separator, ['actor_id', 'first_name', 'last_name'])
    actor_dicts_indexed = add_index(actor_dict_list, 'actor_id')
    actor_dicts_indexed = {k: {
        'actor_id': v['actor_id'],
        'actor_name': (v['first_name'] + ' ' + v['last_name']).lower(),
        'films': []
    } for k, v in actor_dicts_indexed.items()}
    for film_actor_dict in film_actor_dict_list:
        film_id = film_actor_dict['film_id']
        actor_id = film_actor_dict['actor_id']
        film_title = film_dicts_indexed[film_id]['title']
        film_release_year = film_dicts_indexed[film_id]['release_year']
        actor_dicts_indexed[actor_id]['films'].append({'title': film_title, 'release_year': film_release_year})
    return actor_dicts_indexed


def write_to_file_xml(root):
    xml_str = xml_str = minidom.parseString(etree.tostring(root)).toprettyxml(indent="   ")
    with open("main.xml", "w") as file:
        file.write(xml_str)
    file.close()


if __name__ == '__main__':
    main()
