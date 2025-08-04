class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers and prints the calculation type.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The product of a and b.
  """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

