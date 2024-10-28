import pytest
from datetime import datetime, timedelta
from filemodel import MyModel, is_even, find_element


def test_validate_expiration_date():
    future_date = datetime.now() + timedelta(days=1)
    model = MyModel(expiration_date=future_date)
    assert model.expiration_date == future_date


def test_validate_expiration_date_invalid():
    current_date = datetime.now() - timedelta(days=1)

    with pytest.raises(ValueError, match="Expiration date must be in the future"):
        MyModel(expiration_date=current_date)


def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True


def test_find_element():
    assert find_element([1, 2, 3, 4, 5], 2) == True
    assert find_element([1, 2, 3, 4, 5], 7) == False


if __name__ == '__main__':
    pytest.main()