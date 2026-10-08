#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inherits_from_base_model(self):
        """Test that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_name_defaults_to_empty_string(self):
        """Test that name defaults to an empty string."""
        self.assertEqual(State().name, "")

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name State."""
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        state = State()
        state.name = "Texas"
        self.assertEqual(state.to_dict()["name"], "Texas")

    def test_create_from_dict(self):
        """Test that a State can be rebuilt from its dictionary."""
        state = State()
        state.name = "Texas"
        copy = State(**state.to_dict())
        self.assertEqual(copy.id, state.id)
        self.assertEqual(copy.name, "Texas")
        self.assertIsNot(copy, state)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        state = State()
        before = state.updated_at
        state.save()
        self.assertGreater(state.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        state = State()
        self.assertTrue(str(state).startswith("[State] ({})".format(state.id)))


if __name__ == "__main__":
    unittest.main()
