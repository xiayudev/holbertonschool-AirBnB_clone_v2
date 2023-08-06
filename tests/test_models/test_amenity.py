#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


@unittest.skip("showing class skipping")
class test_Amenity(test_basemodel):
    """ """

    @unittest.skip("demonstrating skipping")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skip("demonstrating skipping")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
