import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import counter


class CounterTests(unittest.TestCase):
    def test_read_counter_defaults_to_zero_when_file_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing_file = Path(directory) / "counter.txt"
            with patch.object(counter, "COUNTER_FILE", missing_file):
                self.assertEqual(counter.read_counter(), 0)

    def test_main_increments_existing_counter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            counter_file = Path(directory) / "counter.txt"
            counter_file.write_text("41\n", encoding="utf-8")
            with patch.object(counter, "COUNTER_FILE", counter_file):
                counter.main()
            self.assertEqual(counter_file.read_text(encoding="utf-8"), "42\n")

    def test_invalid_counter_fails_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            counter_file = Path(directory) / "counter.txt"
            counter_file.write_text("invalid\n", encoding="utf-8")
            with patch.object(counter, "COUNTER_FILE", counter_file):
                with self.assertRaisesRegex(ValueError, "valid integer"):
                    counter.read_counter()


if __name__ == "__main__":
    unittest.main()
