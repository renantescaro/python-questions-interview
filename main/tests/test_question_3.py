import unittest
from questions.question_3 import calculate_board_game_stats


class TestQuestion3(unittest.TestCase):

    def test_optimal_path_calculation(self):
        """testa quantidade minima de turnos e a probabilidade de sucesso"""

        board_size = 10
        min_turns, prob, _ = calculate_board_game_stats(board_size)

        self.assertEqual(min_turns, 4)
        self.assertAlmostEqual(prob, 0.012345679, places=7)

    def test_combinations_count(self):
        """testa a quantidade de combinações"""

        board_size = 4
        _, _, combinations = calculate_board_game_stats(board_size)

        self.assertEqual(combinations, 7)

    def test_minimum_size_constraint(self):
        """testa tabuleiro com menos de 3 casas"""

        with self.assertRaises(Exception):
            calculate_board_game_stats(2)


if __name__ == "__main__":
    unittest.main()
