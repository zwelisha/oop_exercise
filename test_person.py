import pytest
from person import Person
"""
Copyright @2019
Author: Zwelisha Mthethwa
"""
person = Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'])
def test_hello():
    greeting = person.hello()
    assert greeting == "Hello, my name is Ryan and I am 30 years old. My interests are being a hardarse, agile and ssd hard drives."
