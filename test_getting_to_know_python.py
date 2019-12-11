from js_functions import *
import pytest

#Test case 1: Valid function definition
# function fooo(bar){ should return fooo
def test_valid_function():
    assert list_all_js_function_names("test_files/test_file_A.txt")[0]["name"] == "fooo"

#Test case 2: Invalid function definition
# function “a = foo(‘hi there’)” should return []
def test_invalid_function():
    assert list_all_js_function_names("test_files/test_file_B.txt") == []
    
 
#Test case 3: Valid function definition
# function foo.bar = function something(){ should return foo.boo
def test_valid_function_v2():
    assert list_all_js_function_names("test_files/test_file_C.txt")[0]["name"] == "foo.bar" 