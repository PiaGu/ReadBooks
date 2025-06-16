from behave import when, then
from playwright.sync_api import expect


@then('knappen "Katalog" ska vara inaktiv')
def step_then_catalog_disabled(context):
    button = context.page.get_by_test_id("catalog")
    expect(button).to_be_disabled()


@then('knappen "Katalog" ska vara aktiv')
def step_then_catalog_enabled(context):
    button = context.page.get_by_test_id("catalog")
    expect(button).to_be_enabled()


@then('knappen "Lägg till bok" ska vara inaktiv')
def step_then_add_book_disabled(context):
    button = context.page.get_by_test_id("add-book")
    expect(button).to_be_disabled()


@then('knappen "Lägg till bok" ska vara aktiv')
def step_then_add_book_enabled(context):
    button = context.page.get_by_test_id("add-book")
    expect(button).to_be_enabled()


@then('knappen "Mina böcker" ska vara inaktiv')
def step_then_favorites_disabled(context):
    button = context.page.get_by_test_id("favorites")
    expect(button).to_be_disabled()


@then('knappen "Mina böcker" ska vara aktiv')
def step_then_favorites_enabled(context):
    button = context.page.get_by_test_id("favorites")
    expect(button).to_be_enabled()
