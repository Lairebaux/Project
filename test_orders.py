from validate import *
from items_menu import Data
import pytest
import unittest
from unittest.mock import Mock, patch
import itertools




class TestValidateItem:

    @staticmethod
    def test_customer_food_order_data_food_items(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "c")
        choice = validate_item()
        assert choice not in data.food_items

    @staticmethod
    def test_customer_food_order_data_food_items2(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "p")
        choice = validate_item()
        assert choice not in data.food_items

    @staticmethod
    def test_customer_food_order_c_or_p(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x:"p")
        choice = validate_item()
        assert choice in ["c", "p"]

    @staticmethod
    def test_customer_food_order_c_or_p_2(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x:"c")
        choice = validate_item()
        assert choice in ["c", "p"]

    @staticmethod
    def test_customer_food_order_c_or_p_3(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x:"g")
        with pytest.raises(ValueError):
            choice = validate_item()
            assert choice == ValueError

    @staticmethod
    def test_customer_food_order_c_or_p_4(monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: 1)
        with pytest.raises(ValueError):
            choice = validate_item()
            assert choice == ValueError


class TestFlavour(unittest.TestCase):

    def set_up(self):
        self.mock = Mock()
        self.mock.side_effect = itertools.count()

    def test_chip_flavour(self):
        """Test choice (flavour) in dict chips"""
        self.choice = "c"
        # q,k,n,s : correct keys for chips
        with patch('builtins.input', side_effect=["k", "q"]):
             self.assertIn(validate_flavour(self.choice), Data().chips)

    def test_popcorn_flavour(self):
        """Test choice (flavour) in dict popcorn"""
        self.choice = "p"
        # b,c,d,v : correct keys for popcorn
        with patch('builtins.input', side_effect=["c", "v"]):
             self.assertIn(validate_flavour(self.choice), Data().popcorn)

    def test_chip_flavour_twice(self):
        """Test error causes loop to runs twice and 3rd choice in Data().chips)"""
        self.choice = "c"
        with patch('builtins.input', side_effect=["d", "c", "q"]):
             self.assertIn(validate_flavour(self.choice), Data().chips)

    def test_popcorn_flavour_twice(self):
        """Test error causes loop to runs twice and 3rd choice in in Data().popcorn)"""
        self.choice = "p"
        with patch('builtins.input', side_effect=["k", "n", "b"]):
             self.assertIn(validate_flavour(self.choice), Data().popcorn)


class TestAmount(unittest.TestCase):
    def set_up(self):
        self.mock = Mock()
        self.mock.side_effect = itertools.count()

    def test_validate_amount(self):
        """Test error causes loop to runs twice and 3rd amount range(1,10)"""
        with patch('builtins.input', side_effect=[0, 56, 5]):
            self.assertIn(validate_amount(), range(1,10))

    def test_validate_amount_string(self):
        """Test error causes loop to runs once and 2nd amount range(1,10)"""
        with patch('builtins.input', side_effect=["g", 5]):
            self.assertIn(validate_amount(), range(1,10))


class TestExtras(unittest.TestCase):

    def test_anything_else_n(self):
        """test return"""
        with patch("builtins.input", return_value="n"):
            self.assertEqual(anything_else(), "n")

    def test_anything_else_twice(self):
        """Test error causes loop to runs twice and 3rd answer == y or n """
        self.mock = Mock()
        self.mock.side_effect = itertools.count()
        with patch("builtins.input", side_effect=["z","e","y"]):
            self.assertIn(anything_else(), ["y", "n"])

