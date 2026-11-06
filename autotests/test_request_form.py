from pages.auth_pages import AuthPage

def test_guest_redirected_to_login(driver):
    page=AuthPage(driver).open('/requests/new')
    assert page.has_text('Вход')
