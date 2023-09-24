# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
TTD template code main file, which contains basic TTD base function examples
"""
import os
from project import config

# print(os.path.abspath("__file__"))
# print("////")
# print(os.path.dirname(os.path.abspath("__file__"
# )))

def read_envs():
    env = config.ENV
    root_dir = config.ROOT_DIR
    return env, root_dir


def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("file doesnt exist")

def print_hi(name):
    """ function that returns hello {name}
    :param name:
    :return: hello {name}
    """
    hello_str = f'Hi, {name}'
    return hello_str


class hello_world():
    """
    Used to test testing functionality around classes. methods print, add and mutate.
    """

    def __init__(self, name):
        self.name = name

    def print_name(self):
        hello_str = f'Hi, {self.name}'
        return hello_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hw = hello_world("test").print_name()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
