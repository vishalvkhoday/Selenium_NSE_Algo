'''
Created on Dec 19, 2019

@author: DELL
'''

import pytest
import allure

@allure.step("This is step 1")
def test_success():
    """this test succeeds"""
    assert True

@allure.step("This is step 2")
def test_failure():
    """this test fails"""
    assert True

@allure.step("This is step 3")
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.step("This is step 4")
def test_broken():
   assert True