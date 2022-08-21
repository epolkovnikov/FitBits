import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        #     4
        #    / \
        #   2   7
        #  / \
        # 1   3
        bst = [4,2,7,1,3]
        rr = 2
        expected = [2, 1, 3]
        tn1 = TreeNode(1)
        tn3 = TreeNode(3)
        tn2 = TreeNode(2, tn1, tn3)
        tn7 = TreeNode(7)
        tnr = TreeNode(4, tn2, tn7)
        s = Solution()
        r = s.searchBST(tnr, rr)
        self.assertEqual(s.print_subtree(r), expected)

    def test_2(self):
        #     4
        #    / \
        #   2   7
        #  / \
        # 1   3
        bst = [4,2,7,1,3]
        rr = 8
        expected = []
        tn1 = TreeNode(1)
        tn3 = TreeNode(3)
        tn2 = TreeNode(2, tn1, tn3)
        tn7 = TreeNode(7)
        tnr = TreeNode(4, tn2, tn7)
        s = Solution()
        r = s.searchBST(tnr, rr)
        self.assertEqual(s.print_subtree(r), expected)

if __name__ == '__main__':
    unittest.main()
