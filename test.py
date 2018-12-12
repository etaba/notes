from solutions import *
import unittest

class Test(unittest.TestCase):

    def test_find_subsets_recursive(self):
        l = [1,2,3]
        self.assertEqual(sorted(find_subsets_recursive(l)), [[1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]])

    def test_find_subsets_binary(self):
        l = [1,2,3]
        self.assertEqual(sorted(find_subsets_binary(l)), [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

    def test_is_rotated(self):
        l1 = [1,2,3,4,5]
        l2 = [4,5,1,2,3]
        l3 = [5,6,7,8,4]
        self.assertTrue(is_rotated(l1,l1))
        self.assertTrue(is_rotated(l1,l2))
        self.assertTrue(is_rotated(l2,l1))
        self.assertFalse(is_rotated(l1,l3))

    def test_find_only_unique(self):
        l = [1,1,2,2,2,3,4,4]
        self.assertEqual(3,find_only_unique(l))

    def test_find_common(self):
        l1 = [1,2,3,4,5,5,5,6,7]
        l2 = [3,5,8]
        self.assertEqual(find_common_set(l1,l2),{3,5})
        self.assertEqual(find_common(l1,l2),{3,5})

    def test_fib(self):
        self.assertEqual(fibonaci_iterative(5),5)
        self.assertEqual(fibonaci_recursive(5),5)

    def test_to_binary(self):
        self.assertEqual(to_binary(6),'110')
        self.assertEqual(to_binary(0),'0')
        self.assertEqual(to_binary(15),'1111')

    def test_parse_int(self):
        self.assertEqual(parse_int(0),'0')
        self.assertEqual(parse_int(1234),'1234')
        self.assertEqual(parse_int(1010100),'1010100')

    def test_exponent(self):
        self.assertEqual(exponent(2,6),64)
        self.assertEqual(exponent(2,0),1)
        self.assertEqual(exponent(2,1),2)
        self.assertEqual(exponent(2,2),4)

    def test_is_anagram(self):
        self.assertTrue(is_anagram_2("tokyo","kyoto"))

    def test_first_not_repeated(self):
        self.assertEqual(first_not_repeated("eerie"),'r')
        self.assertEqual(first_not_repeated("abot"),'a')

    def test_reverse_str(self):
        self.assertEqual(reverse_str("this is a test"),"test a is this")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("boob"))
        self.assertFalse(is_palindrome("boobs"))

    def test_ff_week(self):
        import datetime
        self.assertEqual(get_ff_week(datetime.date(2018,10,2)),5)
        self.assertEqual(get_ff_week(datetime.date(2018,10,3)),5)
        self.assertEqual(get_ff_week(datetime.date(2018,10,1)),4)

    def test_reverse_recursive(self):
        self.assertEqual(recursive_reverse("abcdef"),"fedcba")

    def test_longest_common_sequence(self):
        t1 = [1,4,8,6,3,7,4,9]
        t2 = [8,3,7,4,9,6,1,3]
        self.assertEqual(find_longest_sequence_common(t1,t2),[3,7,4,9])

    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("abcdefracecarzys"),"racecar")
        self.assertEqual(longest_palindrome("abcdefracescarzys"),"")

    def test_optimal_schedule(self):
        self.assertEqual(optimal_schedule([(1,3),(2,5),(3,9),(6,8)]),[(1,3),(6,8)])

    def test_largest_path_through_grid(self):
        grid =   [[3,7,9,2,7],
                  [9,8,3,5,5],
                  [1,7,9,8,5],
                  [3,8,6,4,10],
                  [6,3,9,7,8]]
        self.assertEqual(largest_path_across_grid(grid,(0,0)),[3,9,8,7,9,8,5,10,8])

    #tree shit
    def test_is_bst(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10)
        self.assertTrue(bst.is_bst())

    def test_in_order(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10)
        self.assertEqual(bst.print_in_order_traversal(),[2,3,4,5,6,8,10,15])
    
    def test_post_order(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10)
        self.assertEqual(bst.print_postorder_traversal(),[2,3,4,6,10,15,8,5])

    def test_pre_order(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10)
        self.assertEqual(bst.print_preorder_traversal(),[5,4,3,2,8,6,15,10])

    def test_print_levels(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10)
        self.assertEqual(bst.print_levels(),[5,4,8,3,6,15,2,10])    

    def test_longest(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10,12)
        self.assertEqual(bst.longest_path(),[5,8,15,10,12])

    def test_make_tree(self):
        bst = BinaryTree(5,8,15,4,3,6,2,10,12)
        po = bst.print_preorder_traversal()
        io = bst.print_in_order_traversal()
        bst2 = BinaryTree.make_tree(po,io)
        self.assertEqual(po,bst2.print_preorder_traversal())

    def test_is_sum_tree(self):
        po = [100,40,10,30,60,23,37,37]
        io = [10,40,30,100,23,60,37,37]
        sum_tree = BinaryTree.make_tree(po,io)
        self.assertTrue(sum_tree.is_sum_tree())



if __name__ == '__main__':
    unittest.main()