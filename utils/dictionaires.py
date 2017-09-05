
def get_val_by_key(nested_dict, key, delimiter='.'):
    """
    Traverse recursively nested dict to get nested value
    :param nested_dict: dictionary to be searched. 
    :param key: search key
    :param delimiter: if nested key used delimiter to infer nesting
    :return: value for key
    """
    partial_keys = key.split(delimiter)
    for k in partial_keys:
        nested_dict = nested_dict[k]
    return nested_dict

def flatten():
    pass

### Tests ###
import unittest

d2 = { 'a': 'abc',
       'b': {'c': 1,
             'd': 2}
      }

d1 = { 'a': 'abc'}

d3 = { 'meta': { 'partial': {'key': 'abc'} } }

class Test(unittest.TestCase):
    def test_get_val_by_key(self):
        self.assertEqual(get_val_by_key(d1, 'a'), 'abc')
        self.assertEqual(get_val_by_key(d2, 'b.c'), 1)
        self.assertEqual(get_val_by_key(d3, 'meta-partial-key', delimiter='-'), 'abc')

if __name__ == '__main__':
    unittest.main()
