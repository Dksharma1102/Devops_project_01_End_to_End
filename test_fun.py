import pytest
from app import fa ,no

def test_no():
    assert no("hi")=="give the value in side url like this: /fact/<your number>"

def test_fa_positive():
    assert fa(5) == 120
    assert fa(0) == 1
    assert fa(1) == 1

def test_fa_negative():
    assert fa(-3) == "give correct number in positive"

