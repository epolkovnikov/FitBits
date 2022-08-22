# 700. Search in a Binary Search Tree
Origin: [https://leetcode.com/problems/search-in-a-binary-search-tree/](https://leetcode.com/problems/search-in-a-binary-search-tree/)

## Description
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

## Notes
Tried iterative and recursive approaches. Both appeared to be pretty fast, but recursive is faster.
* search_bst_iterative.py - beats more than 95% of submissions
* search_bst_recursive.py - beats more than 99% of submissions. Is limited by the stacjk allocation, but seem to be fine fo rthe trees with up to 5000 nodes (on LeetCode at least) 
