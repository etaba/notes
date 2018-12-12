import unittest
from tempoAutomationTest import parse_bom_line

class TestMPN(unittest.TestCase):

    def test_format_1(self):
        bom_line = "TSR-1002:Panasonic:A1,D2"
        self.assertEqual(parse_bom_line(bom_line, {"MPN":'TSR-1002','Manufacturer':'Panasonic','ReferenceDesignators':['A1','D2']}))

if __name__ == '__main__':
    unittest.main()