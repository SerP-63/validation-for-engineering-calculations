from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LoginPageLocators.LOGIN_PAGE_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()