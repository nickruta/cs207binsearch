from binsearch import binary_search
from pytest import raises, fixture
import numpy as np

@fixture(scope="module")
def array():
	array = [2,3,5]
	return array

# first test to verify that an empty array returns -1
def test_empty_array():
	assert binary_search([], 1) == -1

def test_array_with_one_element():
	assert binary_search([2], 2) == 0

def test_array_with_two_elements():
	assert binary_search([2,3], 2) == 0

def test_using_fixture(array):
	assert binary_search(array, 2) == 0






