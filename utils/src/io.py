import argparse
import json
import yaml
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def arguments_parser():
    """
    :return: dictionary with argument and value 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--argument1', required=True, help='some required argument')
    parser.add_argument("--x", default = 0, type=int, help="coordinate of x-axis")
    parser.add_argument("--y", default = 0, type=int, help="coordinate of y-axis")
    parser.add_argument("--c", type=int, help="something else, no default, becomes None if nothing assigned")
    return vars(parser.parse_args())


def get_spec_file(*, path:str, format:str) -> dict:
    """
    Get content of yaml or json file
    :param path: path to file
    :param format: possible values are'json' or 'yaml'
    :return: file content
    """
    ext ={'json': json,
          'yaml': yaml}
    try:
        with open(path, 'r') as f:
            return ext[format].load(f)
    except Exception as e:
        logger.error(f'file could not be loaded {path}')
        raise

if __name__ == "__main__":
    #arguments = arguments_parser()
    #arg1 = arguments['argument1']
    #x, y, c = arguments['x'], arguments['y'], arguments['c']
    pass

