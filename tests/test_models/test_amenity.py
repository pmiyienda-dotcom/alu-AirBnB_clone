#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inherits_from_base_model(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name_defaults_to_empty_string(self):
        """Test that name defaults to an empty string."""
        self.assertEqual(Amenity().name, "")

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name Amenity."""
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.to_dict()["name"], "Wifi")

    def test_create_from_dict(self):
        """Test that an Amenity can be rebuilt from its dictionary."""
        amenity = Amenity()
        amenity.name = "Wifi"
        copy = Amenity(**amenity.to_dict())
        self.assertEqual(copy.id, amenity.id)
        self.assertEqual(copy.name, "Wifi")
        self.assertIsNot(copy, amenity)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        amenity = Amenity()
        before = amenity.updated_at
        amenity.save()
        self.assertGreater(amenity.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        amenity = Amenity()
        expected = "[Amenity] ({})".format(amenity.id)
        self.assertTrue(str(amenity).startswith(expected))


if __name__ == "__main__":
    unittest.main()
