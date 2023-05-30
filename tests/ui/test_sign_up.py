import pytest
from src.user import User

@pytest.fixture
def specific_sign_up_user_fixture():
    yield 42

def test_signup_initial(specific_sign_up_user_fixture):
    assert specific_sign_up_user_fixture == 42

@pytest.mark.skip('Correct Data not provided')
def test_signup_final_negative(user_fixture):
    assert user_fixture.get('name') == "afvsvzvszvsadvasv"

def test_signup_final_positive(user_fixture):
    assert user_fixture.get('name') == User.username