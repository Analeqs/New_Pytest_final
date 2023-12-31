import time

from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

SIGN_IN = '//a[text()="Sign In"]'
LOGIN = 'input[placeholder="Email Address"]'
PASSWORD = 'input[placeholder="Password"]'
LOGIN_BUTTON = 'button[value="Login"]'


def test_correct_login(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="anahitaleqs89@gmail.com", password="Anedkuk0123")


def test_incorrect_login(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="wrong", password="Anedkuk0123")
    sign_in_page.locate_wrong_login_message()

    time.sleep(5)


def test_wrong_login_by_text(current_driver): # or wrong pass
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="wrong", password="Anedkuk0123")
    time.sleep(3)
    current_message = sign_in_page.return_wrong_login_message()
    expected_message = "Your username or password is invalid. Please try again."
    assert expected_message == current_message

def test_empty_login_field(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="", password="Anedkuk0123")
    time.sleep(3)
    current_message = sign_in_page.return_empty_login_message()
    expected_message = "The email field is required."
    assert expected_message == current_message


def test_empty_password_field(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="anahitaleqs89@gmail.com", password="")
    time.sleep(3)
    current_message = sign_in_page.return_login_page_heading()
    expected_message = "Login"
    assert expected_message == current_message

def test_correct_login_password_login_was_successfully(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.login_with_user(email="anahitaleqs89@gmail.com", password="Anedkuk0123")
    time.sleep(5)
    sign_in_page.verify_login_was_successfully()
    time.sleep(2)
    current_email = sign_in_page.return_email_value()
    expected_email = "anahitaleqs89@gmail.com"
    assert expected_email == current_email
    print(current_email)


def test_reset_password(current_driver):
    sign_in_page = SignInPage(driver=current_driver)
    home_page = HomePage(driver=current_driver)
    home_page.click_sign_in()
    sign_in_page.reset_password(email="m@gmail.com")
    current_error_message = sign_in_page.return_wrong_email_address_error()
    expected_error_message = "We cannot find a user with that e-mail address"
    time.sleep(2)
    assert expected_error_message == current_error_message
    print(current_error_message)


