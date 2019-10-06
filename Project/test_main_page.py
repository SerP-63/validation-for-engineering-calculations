from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    #page.should_be_login_link()
    page.should_be_login_page()