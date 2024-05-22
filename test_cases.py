import unittest
from wordle_testing import format_score, score_guess

class TestScoring(unittest.TestCase):
    def test_score_hello_against_world(self):
        # Arrange: Start a new game with the target word "world"
        target_word = "world"
        guess = "hello"

        # Act: Score the guess "hello" against the target word "world"
        score = score_guess(guess, target_word)

        # Assert: Verify the response matches the expected output
        expected_formatted_guess = "H E L L O"
        expected_formatted_score = "⬜ ⬜ 🟨 🟩 🟨"

        actual_formatted_guess = format_score(guess, score)

        # Check if the formatted guess matches the expected value
        self.assertEqual(actual_formatted_guess.split('\n')[0], expected_formatted_guess, "Formatted guess does not match")

        actual_formatted_score = actual_formatted_guess.split('\n')[1]

        # Check if the formatted score matches the expected value
        self.assertEqual(actual_formatted_score, expected_formatted_score, "Formatted score does not match")

    def test_score_ankle_against_apple(self):
        # Arrange: Start a new game with the target word "world"
        target_word = "ankle"
        guess = "apple"

        # Act: Score the guess "hello" against the target word "world"
        score = score_guess(guess, target_word)

        # Assert: Verify the response matches the expected output
        expected_formatted_guess = "A P P L E"
        expected_formatted_score = "🟩 ⬜ ⬜ 🟩 🟩"

        actual_formatted_guess = format_score(guess, score)

        # Check if the formatted guess matches the expected value
        self.assertEqual(actual_formatted_guess.split('\n')[0], expected_formatted_guess, "Formatted guess does not match")

        actual_formatted_score = actual_formatted_guess.split('\n')[1]

        # Check if the formatted score matches the expected value
        self.assertEqual(actual_formatted_score, expected_formatted_score, "Formatted score does not match")

    def test_score_batch_against_right(self):
        # Arrange: Start a new game with the target word "world"
        target_word = "batch"
        guess = "right"

        # Act: Score the guess "hello" against the target word "world"
        score = score_guess(guess, target_word)

        # Assert: Verify the response matches the expected output
        expected_formatted_guess = "R I G H T"
        expected_formatted_score = "⬜ ⬜ ⬜ 🟨 🟨"

        actual_formatted_guess = format_score(guess, score)

        # Check if the formatted guess matches the expected value
        self.assertEqual(actual_formatted_guess.split('\n')[0], expected_formatted_guess, "Formatted guess does not match")

        actual_formatted_score = actual_formatted_guess.split('\n')[1]

        # Check if the formatted score matches the expected value
        self.assertEqual(actual_formatted_score, expected_formatted_score, "Formatted score does not match")
if __name__ == "__main__":
    unittest.main()
