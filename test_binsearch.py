from binsearch import binary_search
from pytest import raises, fixture
import numpy as np

# In the binsearch.py file, I only left doc tests that demonstrate to the user what the 
# functionality is and how to use it. I left searching for input, and searching for input in a range
# of the array. I demonstrated what the return value is when the item is found and not found in each
# instance.

# Use fixtures to set up arrays that will be called in many of the below tests 
# in order to acknowledge the DRY software dev. principle.
@fixture(scope="module")
def input_array():
	input_array = list(range(10))
	return input_array

@fixture(scope="module")
def input_array_with_inf():
	input_array_with_inf = [1,2,np.inf]
	return input_array_with_inf

@fixture(scope="module")
def input_array_with_nan():
	input_array_with_nan = [0,1,2,3,np.nan,3,5,6,7]
	return input_array_with_nan

#We should test with wierd data, ie a wierd array: does it have NANs, is it numeric? 
#Does it have 0 elelemts? 1 element? 2?...ie test the boundaries

# first test to verify that an empty array returns -1
# if rangemax > rangemin, binary_search should return -1
def test_array_found(input_array):
	assert binary_search(input_array, 2) == 2

def test_array_not_found(input_array):
	assert binary_search(input_array, 10) == -1 

# an empty array should return -1 
def test_empty_array():
	assert binary_search([], 1) == -1

def test_array_with_one_element_found():
	assert binary_search([2], 2) == 0

def test_array_with_one_element_not_found():
	assert binary_search([5], 4) == -1

def test_array_with_two_elements_found():
	assert binary_search([3,4], 4) == 1

def test_array_with_two_elements_not_found():
	assert binary_search([2,3], 5) == -1

# data types that are comparable will work, use a char array to verify this
def test_char_array():
	assert binary_search(['a','b','c', 'd', 'e', 'f', 'g'], 'f') == 5

def test_int_array_for_float():
	assert binary_search([1,2,3,4,5,6], 2.0) == 1

# test if TypeError will be raised during a search
def test_array_int_str():
	with raises(TypeError):
		binary_search([1,'b',3,4,5], 2)

# Since the PRE-condition defined in the docs for binary search states that the array should consist of
# comparable items, the presence of an inf or nan violates said agreement. If one of these elements of
# the array is set as the midpoint during the binary search, the results will be unpredictable.
# This issue can be addressed using a combination of tests and code to check if an inf or nan value
# is present in the array. 
# For example -

# This could be added to the binary_search function
# if np.nan in list(da_array):
#     raise TypeError("nan is not an acceptable element for the array")
# if np.isnan(needle):
# 	raise TypeError("cannot search for nan")
# if right>len(da_array)-1:
# 	raise ValueError("rangemax shouldn't exceed length of array")

# and these tests could verify the the TypeError is raised
# def test_raise_TypeError_nan():
# 	with raises(TypeError):
# 		binary_search(input_array_with_nan, 5)
# def test_rangemax_exceeds_len():
# 	with raises(ValueError):
# 		binary_search(input_array, 0, 20)

# Search for a value in an array containing a np.inf
def test_array_with_inf(input_array_with_inf):
	assert binary_search(input_array_with_inf, 2) == 1 

# Search for a np.inf 
def test_array_with_inf_needle(input_array_with_inf):
	assert binary_search(input_array_with_inf, np.inf) == 2

# Search for a value in an array containing a np.nan
def test_array_with_nan(input_array_with_nan):
    assert binary_search(input_array_with_nan, 4) == 4

# Search for a np.nan
def test_array_with_nan_needle(input_array_with_nan):
    assert binary_search(input_array_with_nan, np.nan) == 4

# Then think of how the needle relates to the above. 
# Try needles less than or greter than the range in the sorted array, 
# besides needles inbetween (in both cases the needle not being in the array). 
# Try needles at the extremes of the array.
def test_needle_found_in_range(input_array):
	assert binary_search(input_array, 2, 1, 3) == 2 

def test_needle_greater_than_range(input_array):
	assert binary_search(input_array, 6, 1 ,4) == -1 

def test_needle_less_than_range(input_array):
	assert binary_search(input_array, 0, 1 ,3) == -1 

def test_rangemin_greater_than_rangemax(input_array):
	assert binary_search(input_array, 2, 5, 1) == -1 

def test_one_element_range_found(input_array):
	assert binary_search(input_array, 2, 2, 2) == 2 

def test__one_element_range_not_found(input_array):
	assert binary_search(input_array, 5, 2, 2) == -1 

def test_needle_at_beginning_of_range():
	assert binary_search(list(range(6)), 3, 3, 6) == 3

def test_needle_at_end_array():
	assert binary_search(list(range(3)), 2) == 2