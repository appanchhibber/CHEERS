from unittest import TestCase

from Solution import Solution

"""
Python file for testing the method of solution python file
"""


class TestSolution(TestCase):
    """
    This class is responsible for testing various method of Solution class
    """

    def test_alpha(self):
        """
        Test case for testing method for computing alpha
        :return:nothing
        """
        self.assertEqual(2.3098814673407273, Solution.alpha())

    def test_getLength(self):
        """
        Test case for testing method for computing Length
        :return:nothing
        """
        self.assertEqual(2.3841090002136918, Solution.get_length(2))
