#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inherits_from_base_model(self):
        """Test that User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_string_attributes_default_to_empty(self):
        """Test that email, password and names default to empty strings."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name User."""
        self.assertEqual(User().to_dict()["__class__"], "User")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        user = User()
        user.email = "airbnb@mail.com"
        self.assertEqual(user.to_dict()["email"], "airbnb@mail.com")

    def test_create_from_dict(self):
        """Test that a User can be rebuilt from its dictionary."""
        user = User()
        user.first_name = "Betty"
        copy = User(**user.to_dict())
        self.assertEqual(copy.id, user.id)
        self.assertEqual(copy.first_name, "Betty")
        self.assertIsNot(copy, user)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        user = User()
        before = user.updated_at
        user.save()
        self.assertGreater(user.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        user = User()
        self.assertTrue(str(user).startswith("[User] ({})".format(user.id)))


if __name__ == "__main__":
    unittest.main()
