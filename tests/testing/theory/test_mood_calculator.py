import unittest
from lectures.testing.theory.mood_calculator import MoodCalculator
from lectures.testing.theory.mood_calculator import Mood


class MyTestCase(unittest.TestCase):
    """
    Note - we have two methods beginning 'test'. Both these methods will be run
    """

    def setUp(self):
        self.mood_calculator = MoodCalculator()

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            self.mood_calculator.calculate_mood(-1, 70)

    def test_mood_calculator(self):
        """
        TODO - Exercise for the student to write and test the mood calculator
        :return:
        """
        self.assertEqual(self.mood_calculator.calculate_mood(0, 80),
                         Mood.Joyful)

        self.assertEqual(self.mood_calculator.calculate_mood(30, 70),
                         Mood.Grumpy)

        self.assertEqual(self.mood_calculator.calculate_mood(0, 70),
                         Mood.Irritated)

        self.assertEqual(self.mood_calculator.calculate_mood(30, 80),
                         Mood.Hulk)

        pass


if __name__ == '__main__':
    unittest.main()
