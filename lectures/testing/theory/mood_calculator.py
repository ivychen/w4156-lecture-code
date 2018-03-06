# from enum import Enum, auto
from enum import Enum


class Mood(Enum):
    Joyful = 0
    Grumpy = 1
    Irritated = 2
    Hulk = 3


class MoodCalculator:

    def calculate_mood(self, sleep_deprivation: int, blood_sugar: int) -> Mood:
        """
        Calculate humans Mood based on  and blood sugar
        :param sleep_deprivation: hours since last nap. Must be within 0 and 36 inclusive
        :param blood_sugar: glucose mmol/L. Must be within 70 to 90 inclusive
        :return: mood
        """
        if not 0 <= sleep_deprivation <= 36:
            raise ValueError("Sleep Deprivation:%s not within valid range (%s,%s)" % (sleep_deprivation, 0, 36))

        # TODO - student to complete the rest of the function and write the tests

        if not 0 <= blood_sugar <= 140:
            raise ValueError(
                "Blood Sugar:%s not within valid range (%s, %s)" % (
                    blood_sugar, 0, 140))

        if sleep_deprivation <= 26:
            if 70 <= blood_sugar <= 75:
                return Mood.Irritated
            elif 75 < blood_sugar <= 90:
                return Mood.Joyful
        elif sleep_deprivation > 26:
            if 70 <= blood_sugar <= 75:
                return Mood.Grumpy
            elif 75 < blood_sugar <= 90:
                return Mood.Hulk
        else:
            raise ValueError("Sorry, this doesn't produce a valid mood.")




