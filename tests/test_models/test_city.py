#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inherits_from_base_model(self):
        """Test that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes_default_to_empty_string(self):
        """Test that state_id and name default to empty strings."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name City."""
        self.assertEqual(City().to_dict()["__class__"], "City")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        city = City()
        city.name = "Austin"
        city.state_id = "123"
        data = city.to_dict()
        self.assertEqual(data["name"], "Austin")
        self.assertEqual(data["state_id"], "123")

    def test_create_from_dict(self):
        """Test that a City can be rebuilt from its dictionary."""
        city = City()
        city.name = "Austin"
        copy = City(**city.to_dict())
        self.assertEqual(copy.id, city.id)
        self.assertEqual(copy.name, "Austin")
        self.assertIsNot(copy, city)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        city = City()
        before = city.updated_at
        city.save()
        self.assertGreater(city.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        city = City()
        self.assertTrue(str(city).startswith("[City] ({})".format(city.id)))


if __name__ == "__main__":
    unittest.main()
