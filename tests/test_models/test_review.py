#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_inherits_from_base_model(self):
        """Test that Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes_default_to_empty_string(self):
        """Test that place_id, user_id and text default to empty strings."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_has_base_attributes(self):
        """Test that id, created_at and updated_at are set."""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_to_dict_has_class_name(self):
        """Test that to_dict stores the class name Review."""
        self.assertEqual(Review().to_dict()["__class__"], "Review")

    def test_to_dict_includes_set_attributes(self):
        """Test that attributes set on the instance appear in to_dict."""
        review = Review()
        review.text = "Great stay"
        self.assertEqual(review.to_dict()["text"], "Great stay")

    def test_create_from_dict(self):
        """Test that a Review can be rebuilt from its dictionary."""
        review = Review()
        review.text = "Great stay"
        copy = Review(**review.to_dict())
        self.assertEqual(copy.id, review.id)
        self.assertEqual(copy.text, "Great stay")
        self.assertIsNot(copy, review)

    def test_save_updates_updated_at(self):
        """Test that save changes updated_at."""
        review = Review()
        before = review.updated_at
        review.save()
        self.assertGreater(review.updated_at, before)

    def test_str_format(self):
        """Test that __str__ starts with the class name and id."""
        review = Review()
        expected = "[Review] ({})".format(review.id)
        self.assertTrue(str(review).startswith(expected))


if __name__ == "__main__":
    unittest.main()
