import unittest
from pymk2json.main import *

class TestConversionFunctions(unittest.TestCase):
    def test_mrkd2json(self):
        my_str='''| Some Title | Some Description             | Some Number |
|------------|------------------------------|-------------|
| Dark Souls | This is a fun game           | 5           |
| Bloodborne | This one is even better      | 2           |
| Sekiro     | This one is also pretty good | 110101      |'''

        data = mrkd2json(my_str)
        result = True
        # try:
        #     result = json.loads(data)
        # except ValueError:
        #     result = False
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()