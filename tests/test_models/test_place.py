#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


@unittest.skip("showing class skipping")
class test_Place(test_basemodel):
    """ """

    @unittest.skip("demonstrating skipping")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skip("demonstrating skipping")
    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skip("demonstrating skipping")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skip("demonstrating skipping")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skip("demonstrating skipping")
    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skip("demonstrating skipping")
    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skip("demonstrating skipping")
    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skip("demonstrating skipping")
    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skip("demonstrating skipping")
    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skip("demonstrating skipping")
    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skip("demonstrating skipping")
    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skip("demonstrating skipping")
    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
