import unittest
from questions.question_1 import check_str_characters


class TestQuestion1(unittest.TestCase):

    def test_valid_string(self):
        """testa sucesso"""
        self.assertTrue(check_str_characters("Bola"))
        self.assertTrue(check_str_characters("banana"))

    def test_invalid_start(self):
        """testa erro"""
        self.assertFalse(check_str_characters("Cola"))

    def test_invalid_end(self):
        """testa começo correto e final incorreto"""
        self.assertFalse(check_str_characters("Bolo"))

    def test_empty_string(self):
        """testa erro string vazia"""
        with self.assertRaises(Exception):
            check_str_characters("")

    def test_case_insensitivity(self):
        """testa conversão para lowercase"""
        self.assertTrue(check_str_characters("bOLA"))


if __name__ == "__main__":
    unittest.main()
