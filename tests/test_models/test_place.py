#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inherits_from_base_model(self):
        """Test that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_string_attributes_default_to_empty(self):
        """Test that the string attributes default to empty strings."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")

    def test_integer_attributes_default_to_zero(self):
        """Test that the integer attributes default to 0."""
        place = Place()
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertIsInstance(place.number_rooms, int)

    def test_float_attributes_default_to_zero(self):
        """Test that latitude and longitude default to 0.0."""
        place = Place()
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertIsInstance(place.latitude, float)

    def test_amenity_ids_defaults_to_empty_list(self):
        """Test that amenity_ids defaults to an empty list."""
        self.assertEqual(Place().amenity_ids, [])
        self.assertIsInstance(Place().amenity_ids, list)

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name Place."""
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        place = Place()
        place.name = "Cabin"
        place.max_guest = 4
        data = place.to_dict()
        self.assertEqual(data["name"], "Cabin")
        self.assertEqual(data["max_guest"], 4)

    def test_create_from_dict(self):
        """Test that a Place can be rebuilt from its dictionary."""
        place = Place()
        place.name = "Cabin"
        copy = Place(**place.to_dict())
        self.assertEqual(copy.id, place.id)
        self.assertEqual(copy.name, "Cabin")
        self.assertIsNot(copy, place)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        place = Place()
        before = place.updated_at
        place.save()
        self.assertGreater(place.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        place = Place()
        self.assertTrue(str(place).startswith("[Place] ({})".format(place.id)))


if __name__ == "__main__":
    unittest.main()
