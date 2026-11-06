from pages.auth_pages import AuthPage
import uuid

def test_empty_registration_shows_errors(driver):
    page=AuthPage(driver).open('/register').submit()
    assert page.wait_text('Заполните это поле')

def test_too_short_password(driver):
    page=AuthPage(driver).open('/register').fill(login='studentabc',full_name='Тестовый Пользователь',password='1234567',email='student@example.test',phone='+79991234567').submit()
    assert page.wait_text('Пароль: 8–128 символов')

def test_valid_registration(driver):
    username='u_'+uuid.uuid4().hex[:10]
    page=AuthPage(driver).open('/register').fill(login=username,full_name='Тестовый Пользователь',password='Password2026',email=username+'@example.test',phone='+79991234567').submit()
    assert page.wait_text('Регистрация прошла успешно')
