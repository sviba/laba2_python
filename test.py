import unittest
from parser import DataValidator

class TestDateValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = DataValidator()

    def test_valid(self):
        text = "Важные даты: 01.01.2000, 25.12.2023 и 31.08.1995."
        result = self.validator.validate_text(text)
        self.assertEqual(result, ["01.01.2000", "25.12.2023", "31.08.1995"])

    def test_invalid(self):
        text = "Ошибки: 32.01.2020, 15.13.2023, 12.12.99, 00.05.2021"
        result = self.validator.validate_text(text)
        self.assertEqual(result, [])
    
if __name__ == "__main__":
    unittest.main()