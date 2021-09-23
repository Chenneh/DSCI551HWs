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
    query = "./actor_table/actor/" + "[" + "actor_name=" + "\'" + argv + "\'" + "]"
    result = root.findall(query)
    result = {element.get('id'): eval(element.find('./films').text) for element in result}

    return result


if __name__ == '__main__':
    # example
    # python actor.py 'ed chase'
    print(main(sys.argv[1]))
