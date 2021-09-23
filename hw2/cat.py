# package imports
# e.g.
# import pandas as pd
# ...
import sys
from typing import List, Union
from lxml import etree
from xml.dom import minidom

database_path = 'main.xml'


# using xpath:
# film_table_prefix = "/root/film_table/film"
# query_content = "[category/text()=" + "\'" + argv + "\'" + "]"
#  query = film_table_prefix + query_content
# query_result = root.xpath(query)

# print(minidom.parseString(ET.tostring(query_result[0])).toprettyxml(indent="   "))

def main(argv: str) -> Union[List[dict], None]:
    tree = etree.parse(database_path)
    root = tree.getroot()
    query = "./film_table/film/" + "[" + "category=" + "\'" + argv + "\'" + "]"
    result = root.findall(query)
    result = [
        {
            'title': film_element.find('./title').text,
            'release_year': film_element.find('./release_year').text,
            'rental_duration': film_element.find('./rental_duration').text,
            'rental_rate': film_element.find('./rental_rate').text,
            'rating': film_element.find('./rating').text,
        } for film_element in result]

    return result


if __name__ == '__main__':
    # example
    # python actor.py action
    print(main(sys.argv[1]))
