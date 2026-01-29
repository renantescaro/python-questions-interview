import unittest
from questions.question_2 import get_value_from_numerical_sequence


class TestQuestion2(unittest.TestCase):

    def test_first_position(self):
        """testa primeira posição"""
        self.assertEqual(get_value_from_numerical_sequence(1), 11)

    def test_subsequent_positions(self):
        """testa posições 2, 3 e 10"""
        self.assertEqual(get_value_from_numerical_sequence(2), 18)
        self.assertEqual(get_value_from_numerical_sequence(3), 25)
        self.assertEqual(get_value_from_numerical_sequence(10), 74)

    def test_zero_index_exception(self):
        """testa o index vazio"""
        with self.assertRaises(Exception) as context:
            get_value_from_numerical_sequence(0)
        self.assertEqual(str(context.exception), "'index' não pode ser vazio")

    def test_negative_index_exception(self):
        """testa index negativo"""
        with self.assertRaises(Exception) as context:
            get_value_from_numerical_sequence(-5)
        self.assertEqual(
            str(context.exception), "'index' não pode ser negativo ou igual a zero"
        )

    def test_large_index(self):
        """testa index alto"""
        self.assertEqual(get_value_from_numerical_sequence(100), 704)


if __name__ == "__main__":
    unittest.main()
