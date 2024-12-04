from bank import value
import pytest

def test_value_greeting_hello():
 assert value("здравствуйте") == 0

def test_value_greeting_z():
 assert value("з") == 20

def test_value_greeting_other():
 assert value("привет") == 100
 assert value("доброе утро") == 100
