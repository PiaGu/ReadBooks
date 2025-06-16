import re
from behave import given, when, then
from playwright.sync_api import expect

@given(u'att användaren är på sidan "Läslistan"')
def step_given_start(context):
    context.page.goto(context.base_url)
    expect(context.page).to_have_title(re.compile("Läslistan"), timeout=500)


@when(u'användaren klickar på knappen "Katalog"')
def step_then_catalogue(context):
    catalog_button = context.page.get_by_test_id("catalog")
    catalog_button.click()
    context.catalog_button = catalog_button


@when(u'användaren klickar på knappen "Lägg till bok"')
def step_when_add_book_button(context):
    add_book_button = context.page.get_by_test_id("add-book")
    add_book_button.click()
    context.add_book_button = add_book_button

@when(u'användaren klickar på knappen "Mina böcker"')
def step_when_click_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()
