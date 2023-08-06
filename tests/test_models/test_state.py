#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


@unittest.skip("showing class skipping")
class test_state(test_basemodel):
    """ """

    @unittest.skip("demonstrating skipping")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skip("demonstrating skipping")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
