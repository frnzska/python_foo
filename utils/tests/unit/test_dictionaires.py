import unittest
from utils.src.dictionaires import flatten, get_val_by_key

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

