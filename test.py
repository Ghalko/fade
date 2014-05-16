import unittest #to test floating points
import pytest
from fader import Fade

@pytest.mark.parametrize('steps', [
	7,
    8,
    16,
    32,
])
def test_find_int_len(steps):
	f = Fade(steps)
	assert len(f.find_int(steps, 0, 255)) == steps+1

@pytest.mark.parametrize('steps', [
	7,
    8,
    16,
    32,
])
def test_last_number_255(steps):
	f = Fade(steps)
	ans = f.find_int(steps, 0, 255)
	assert ans[-1] == 255

@pytest.mark.parametrize('largest', [
	0,
	3,
    25,
    82,
    163,
])
def test_range(largest):
	f = Fade(10)
	ans = f.find_int(10, 0, largest)
	assert len(ans) == 11
	assert ans[-1] == largest

@pytest.mark.parametrize('start', [
	0,
	3,
    25,
    82,
    163,
])
def test_start(start):
	f = Fade(10)
	ans = f.find_int(10, start, 255)
	assert len(ans) == 11
	assert ans[-1] == 255

@pytest.mark.parametrize('start', [
	0,
	3,
    25,
    82,
    163,
])
def test_negative(start):
	f = Fade(10)
	ans = f.find_int(10, 255, start)
	assert len(ans) == 11
	assert ans[-1] == start