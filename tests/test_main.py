import unittest
from main import align_markdown, cells, is_separator

class Tests(unittest.TestCase):
    def test_separator(self):
        self.assertTrue(is_separator("| --- | :---: |"))
        self.assertFalse(is_separator("| -- | x |"))
    def test_aligns_columns(self):
        result = align_markdown("| A | Longer |\n| --- | --- |\n| x | y |\n")
        self.assertIn("| A   | Longer |", result)
        self.assertIn("| --- | ------ |", result)
    def test_preserves_non_table_text(self):
        text = "# Title\n\nnot a table\n"
        self.assertEqual(align_markdown(text), text)
    def test_cells(self):
        self.assertEqual(cells("| a | b |"), ["a", "b"])

if __name__ == "__main__":
    unittest.main()
