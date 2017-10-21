from MathOperations import MathOperation

"""
Python file for implementing the solution of the project
"""


class Solution:
    """
    This class is responsible for the calculation of the value of alpha and the length between the two coasters of same
    radius
    """
    alpha_value = float(10)

    @staticmethod
    def alpha():
        """
        This static method calculates the value of alpha
        :return:nothing
        """
        alpha = 2
        precision = 6
        pi = MathOperation.pi()
        calculated_decimal_places = 1
        for itr in range(0, precision):
            original = alpha - MathOperation.sin(alpha) - pi / 2
            prime = 1.0 - MathOperation.cos(alpha)
            alpha = alpha - (original / prime)
            if itr >= 1:
                calculated_decimal_places += 3 * (2 ** (itr - 1))
                if calculated_decimal_places > precision:
                    break
        return alpha

    @staticmethod
    def set_alpha():
        Solution.alpha_value = Solution.alpha()

    @staticmethod
    def get_alpha():
        return Solution.alpha_value

    @staticmethod
    def get_length(radius):
        """
        This static method calculates the length based on the value of alpha
        :param radius:
        :return:float length
        """
        Solution.set_alpha()
        return 2.0 * radius * (1.0 - MathOperation.cos(Solution.get_alpha() / 2))
