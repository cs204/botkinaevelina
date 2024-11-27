from jar import Jar
import pytest

def test_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)  # Capacity exceeded

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)  # Not enough cookies

def test_str():
    jar = Jar(4)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
