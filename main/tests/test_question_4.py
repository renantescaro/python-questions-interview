import unittest
from datetime import date
from questions.question_4 import calculate_resignation_benefits


class TestQuestion4(unittest.TestCase):

    def test_full_months_calculation(self):
        """testa 1 ano de trabalho"""

        salary = 3000.00
        adm_date = date(2023, 1, 10)
        res_date = date(2023, 12, 20)

        thirteenth_salary, total_vacation, _ = calculate_resignation_benefits(
            salary, adm_date, res_date
        )

        self.assertEqual(thirteenth_salary, 3000.00)
        self.assertAlmostEqual(total_vacation, 3666.6666666666665)

    def test_partial_month_less_than_15_days(self):
        """testa menos de 15 dias de trabalho"""

        salary = 1200.00
        adm_date = date(2023, 6, 1)
        res_date = date(2023, 6, 10)

        thirteenth, vacation, _ = calculate_resignation_benefits(
            salary, adm_date, res_date
        )

        self.assertEqual(thirteenth, 0.0)
        self.assertEqual(vacation, 0.0)

    def test_vacation_cycle_cross_year(self):
        """testa virada do ano"""

        salary = 6000.00
        adm_date = date(2023, 10, 1)
        res_date = date(2024, 2, 20)

        thirteenth_salary, total_vacation, _ = calculate_resignation_benefits(
            salary, adm_date, res_date
        )

        self.assertEqual(thirteenth_salary, 1000.00)
        self.assertEqual(total_vacation, 2666.6666666666665)


if __name__ == "__main__":
    unittest.main()
