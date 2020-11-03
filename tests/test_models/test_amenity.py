#!/usr/bin/python3
"""Defines unittests for models/state.py"""
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))
