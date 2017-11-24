import argparse

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

if __name__ == "__main__":
    arguments = arguments_parser()
    arg1 = arguments['argument1']
    x, y, c = arguments['x'], arguments['y'], arguments['c']
