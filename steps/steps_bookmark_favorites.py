from behave import when, then, given
from playwright.sync_api import expect
import re

@given(u'boken med titeln "100 sätt att undvika måndagar" visas i listan')
def step_given_book_visible(context):
    book = context.page.locator('[data-testid="star-100 sätt att undvika måndagar"]')
    book.wait_for()


@when(u'användaren hovrar över boken "100 sätt att undvika måndagar"')
def step_when_hover_book(context):
    book = context.page.get_by_test_id("star-100 sätt att undvika måndagar")
    book.hover()

@then(u'visas ett hjärta i början av raden för boken')
def step_then_heart_visible(context):
    heart = context.page.get_by_test_id("star-100 sätt att undvika måndagar")
    expect(heart).to_have_class(re.compile(r"\bstar\b"))


@when(u'användaren klickar på hjärtat för boken "100 sätt att undvika måndagar"')
def step_when_click_heart(context):
    click_heart_book = context.page.get_by_test_id("star-100 sätt att undvika måndagar")
    click_heart_book.click()
    expect(click_heart_book).to_have_class(re.compile(r"\bselected\b"))


@then(u'favoritmarkeras boken med ett hjärta')
def step_then_book_is_favorited(context):
    star = context.page.locator('[data-testid="star-100 sätt att undvika måndagar"]')
    expect(star).to_have_class(re.compile(r'\bstar\b.*\bselected\b'))



@then(u'ska boken "100 sätt att undvika måndagar" visas i listan på sidan "Mina Böcker"')
def step_then_book_in_my_books(context):
    book = context.page.get_by_test_id("fav-100 sätt att undvika måndagar")
    expect(book).to_have_text("100 sätt att undvika måndagar")
