import unittest
from bomdotcom import *

class TestBomDotCom(unittest.TestCase):

    def test_format_1(self):
        bom_line = 'TSR-1002:Panasonic:A1,D2'
        self.assertEqual(parse_bom_line(bom_line), 
                         {  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Panasonic',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'D2'
                                ]
                         })

    def test_format_2(self):
        bom_line = 'Panasonic -- TSR-1002:A1'
        self.assertEqual(parse_bom_line(bom_line), 
                 {  
                    'MPN':'TSR-1002',
                    'Manufacturer':'Panasonic',
                    'ReferenceDesignators':
                        [
                            'A1'
                        ]
                 })

    def test_format_3(self):
        bom_line = 'A1,B2,C8;TSR-1002;Keystone'
        self.assertEqual(parse_bom_line(bom_line), 
                 {  
                    'MPN':'TSR-1002',
                    'Manufacturer':'Keystone',
                    'ReferenceDesignators':
                        [
                            'A1',
                            'B2',
                            'C8'
                        ]
                 })

    def test_organize_mpns(self):
        test_mpns = [{  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Panasonic',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'D2'
                                ]
                         },
                         {  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Panasonic',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'B2'
                                ]
                         },
                         {  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Keystone',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'B2',
                                    'C8'
                                ]
                         }]
        organize_mpns(test_mpns)

        desired = [{  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Panasonic',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'B2',
                                    'D2'
                                ],
                            'NumOccurences':2
                         },
                         {  
                            'MPN':'TSR-1002',
                            'Manufacturer':'Keystone',
                            'ReferenceDesignators':
                                [
                                    'A1',
                                    'B2',
                                    'C8'
                                ],
                            'NumOccurences':1
                         }]
        #output mpn reference designator lists need to be sorted to avoid false negative test result
        for mpn in test_mpns:
            mpn['ReferenceDesignators'].sort()
        self.assertEqual(test_mpns,desired)

if __name__ == '__main__':
    unittest.main()