from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    # Browser setting, browser not visible during tests (Faster)
    #context.browser = context.browser_type.launch(headless=True)
    #Alternative browser setting, browser visible during tests
    context.browser = context.browser_type.launch(headless=False, slow_mo=10)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://tap-ht24-testverktyg.github.io/exam-template/"

def after_scenario(context, scenario):
    if context.page:
       context.page.close()

def after_all(context):
    if context.browser:
       context.browser.close()
    if context.playwright:
       context.playwright.stop()