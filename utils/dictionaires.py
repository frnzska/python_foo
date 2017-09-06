
def get_val_by_key(nested_dict, key, delimiter='.'):
    """
    Traverse nested dict, get value by 'nested key' (e.g. meta.created_at)
    :param nested_dict: dictionary to be searched. 
    :param key: search key
    :param delimiter: if nested key used delimiter to infer nesting
    :return: value for key
    """
    partial_keys = key.split(delimiter)
    for k in partial_keys:
        nested_dict = nested_dict[k]
    return nested_dict

def flatten(nested_dict, delimiter='.'):
    """
    Flatten nested dict
    :param nested_dict: dictionary
    :param delimiter: nested keys connector
    :return: flat dictionary
    """
    result = {}
    def _f(d, result=result, keys=[]): # TODO find better solution without
        for k, val in d.items():
            if not isinstance(val, dict):
                key = delimiter.join(keys + [k]) if keys else k
                result[key] = val
            else:
                _f(val, result, keys + [k])
    _f(nested_dict)
    return result






### Tests ###
import unittest

class Test(unittest.TestCase):
    d1 = {'a': 'abc'}
    d2 = {'a': 'abc',
          'b': {'c': 1,
                'd': 2} }
    d3 = {'meta': {'partial': {'key': 'abc'}}}

    def test_get_val_by_key(self, d1=d1, d2=d2, d3=d3):
        self.assertEqual(get_val_by_key(d1, 'a'), 'abc')
        self.assertEqual(get_val_by_key(d2, 'b.c'), 1)
        self.assertEqual(get_val_by_key(d3, 'meta-partial-key', delimiter='-'), 'abc')

    def test_flatten(self, d1=d1, d2=d2, d3=d3):
        flat_d2 = {'a': 'abc',
                   'b.c': 1,
                   'b.d': 2}
        flat_d3 = {'meta.partial.key': 'abc'}

        self.assertEqual(flatten(d1), d1)
        assert flatten(d2) == flat_d2
        assert flatten(d3) == flat_d3
        assert flatten(d3, delimiter='#') == {'meta#partial#key': 'abc'}
        assert flatten({}) == {}

if __name__ == '__main__':
    unittest.main()

