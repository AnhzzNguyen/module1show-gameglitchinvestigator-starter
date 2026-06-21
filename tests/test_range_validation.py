import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import get_range_for_difficulty

def test_easy_difficulty_range():
    # Easy difficulty should have range 1-20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    # Normal difficulty should have range 1-100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_difficulty_range():
    # Hard difficulty should have range 1-50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_guess_within_range_acceptable():
    # Guesses within the range (1-100 for Normal) should be accepted
    low, high = get_range_for_difficulty("Normal")
    assert 1 >= low and 1 <= high
    assert 50 >= low and 50 <= high
    assert 100 >= low and 100 <= high

def test_guess_outside_range_rejected():
    # Guesses outside the range (like 1000) should be rejected for Normal (1-100)
    low, high = get_range_for_difficulty("Normal")
    assert not (1000 >= low and 1000 <= high)
    assert not (0 >= low and 0 <= high)
    assert not (101 >= low and 101 <= high)
