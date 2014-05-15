import unittest #to test floating points
import pytest
from fader import Fade

@pytest.mark.parametrize('steps', [
	7,
    8,
    16,
    32,
])
def test_positive_pw2_steps(steps):
	f = Fade(steps)
	answers = []
	for each in f:
		answers.append(each)
	assert len(answers) == steps

@pytest.mark.parametrize('steps', [
	7,
    8,
    16,
    32,
])
def test_last_number(steps):
	f = Fade(steps)
	answer = 0
	for each in f:
		answer = each
	assert answer == (255, 255, 255)