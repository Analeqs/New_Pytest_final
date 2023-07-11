from pages.base_page import BasePage


class MyCoursesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    AVATAR = 'Img[class="zl-navbar-rhs-img "]'
    LOGOUT = '//a [text()="Logout"]'
    MY_ACCOUNT = '//a[text()="My Account "]'