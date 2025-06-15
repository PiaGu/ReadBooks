from behave import when, then
from playwright.sync_api import expect

@then(u'boken med titeln "100 sätt att undvika måndagar" visas i listan')
def step_then_book_visible(context):
    book = context.page.locator('text="100 sätt att undvika måndagar"')
    expect(book).to_be_visible()

@when(u'användaren hovrar över boken "100 sätt att undvika måndagar"')
def step_when_hover_book(context):
    book = context.page.get_by_test_id("star-100 sätt att undvika måndagar")
    book.hover()

@then(u'visas ett hjärta i början av raden för boken')
def step_then_heart_visible(context):
    heart = context.page.locator('[data-testid="heart-icon"]')
    expect(heart).to_be_visible()

@when(u'användaren klickar på hjärtat för boken "100 sätt att undvika måndagar"')
def step_when_click_heart(context):
    book = context.page.locator('text="100 sätt att undvika måndagar"')
    heart = book.locator('[data-testid="heart-icon"]')
    heart.click()

@then(u'favoritmarkeras boken med ett hjärta')
def step_then_book_favorited(context):
    heart_active = context.page.locator('[data-testid="heart-icon"].active')
    expect(heart_active).to_be_visible()

@when(u'användaren klickar på knappen "Mina böcker"')
def step_when_click_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()

@then(u'ska boken "100 sätt att undvika måndagar" visas i listan på sidan "Mina Böcker"')
def step_then_book_in_my_books(context):
    book = context.page.get_by_test_id("fav-100 sätt att undvika måndagar")
    expect(book).to_be_visible()


