from pages.auth_pages import AuthPage

def test_empty_login(driver):
    page=AuthPage(driver).open('/login').submit()
    assert page.wait_text('Заполните это поле')
def test_wrong_password(driver):
    page=AuthPage(driver).open('/login').fill(login='nonexistent',password='WrongPass2026').submit()
    assert page.wait_text('Неверный логин или пароль')
