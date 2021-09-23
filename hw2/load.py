# package imports
# e.g.
# import pandas as pd
# ...

from lxml import etree
import pandas as pd

film_csv_path = 'film.csv'
film_actor_csv_path = 'film_actor.csv'
film_category_csv_path = 'film_category.csv'
actor_csv_path = 'actor.csv'
category_csv_path = 'category.csv'

file_path_list = ['film.csv', 'film_actor.csv', 'film_category.csv', 'actor.csv', 'category.csv']

global_separator = ';'
cols_film = ['title', 'release_year', 'rating', 'rental_rate', 'rental_duration', 'category']
cols_actor = ['actor_id', 'actor_name', 'films']


def main() -> None:
    root = etree.Element("root")
    for file_path in file_path_list:
        element_type = file_path.split('.')[0]
        root.append(csv_to_element_table(file_path, global_separator, element_type))

    write_to_file_xml(root)


def write_to_file_xml(root):
    et = etree.ElementTree(root)
    et.write('main.xml', pretty_print=True)


def csv_to_element_table(csv_path, separator, element_type):
    df = pd.read_csv(csv_path, sep=separator)
    cols = df.columns
    cur_dict_list = df.to_dict(orient='records')
    table = etree.Element(element_type + "_table")
    for cur_dict in cur_dict_list:
        new_element = etree.Element(element_type)
        for col in cols:
            new_element_property = etree.Element(col)
            new_element_property.text = str(cur_dict[col])
            if col != "title":
                new_element_property.text = new_element_property.text.lower()
            new_element.append(new_element_property)
        table.append(new_element)
    return table


if __name__ == '__main__':
    main()
