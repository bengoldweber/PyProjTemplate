# test_with_pytest.py
from unittest import TestCase
from unittest.mock import patch
import mock

import project.main
from project import main
import pytest

import unittest
import os

#todo mock test os path
def test_read_envs():
    env_c_result_env, env_c_result_rd = main.read_envs()
    expected_env = 'production'
    # expected_root_dir = os.path.dirname(os.path.abspath("__file__"))
    assert env_c_result_env == expected_env and env_c_result_rd == env_c_result_rd

# class RemoveTestCase(unittest.TestCase):
#     @mock.patch('main.os.patch')
#     @mock.patch('main.os.remove')
#     def test_remove(self, mock_os_remove, mock_os_path):
#         mock_os_path.exists.return_value = True
#         main.remove_file('/Users/benjamingoldweber/PycharmProjects/TTD_Experiment')
#


@pytest.mark.parametrize("test_input,expected", # 1
                         [('ben', 'Hi, ben'), # 2
                          ('joe', 'Hi, joe'),
                          ('joe shmoe', 'Hi, joe shmoe')])
def test_main_hello(test_input, expected):
    hello_c_result = main.print_hi(test_input)
    assert hello_c_result == expected # expected result


#todo im re-using the pytest paramitization. Why?
@pytest.mark.parametrize("test_input,expected", # 1
                         [('ben', 'Hi, ben'), # 2
                          ('joe', 'Hi, joe'),
                          ('joe shmoe', 'Hi, joe shmoe')])
def test_main_class_hello(test_input, expected):
    expected = main.hello_world(test_input).print_name()
    g_result = main.print_hi(test_input)
    assert g_result == expected # expected result


def test_always_passes():
    assert True


def test_always_fails():
    assert False


