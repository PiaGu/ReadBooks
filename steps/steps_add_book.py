import re
from behave import given, then, when
from playwright.sync_api import expect


@when(u'användaren fyller i fältet "Titel" med en boktitel')
def step_then_title(context):
    title_input = context.page.get_by_test_id("add-input-title")
    title_input.click()
    title_input.fill("Den gudomliga komedin")


@when(u'användaren fyller i fältet "Författare" med bokens författare')
def step_then_author(context):
    author_input = context.page.get_by_test_id("add-input-author")
    author_input.click()
    author_input.fill("Dante Alighieri")


@when(u'användaren klickar på knappen "Lägg till ny bok"')
def step_then_save(context):
    save_button = context.page.get_by_test_id("add-submit")
    save_button.click()


@then(u'ska knappen "Lägg till ny bok" vara inaktiv')
def step_then_disable_save(context):
    save_button = context.page.get_by_test_id("add-submit")
    expect(save_button).to_be_disabled()


@then(u'ska boken visas i katalogen')
def step_added_book(context):
    my_book = context.page.locator(".book").filter(has_text=re.compile(r"Den gudomliga komedin", re.IGNORECASE))
    expect(my_book).to_have_text(re.compile(r'Den gudomliga komedin'))
