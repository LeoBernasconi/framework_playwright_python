#https://playwright.dev/python/docs/writing-tests#basic-actions

import re
from playwright.sync_api import Page, expect

def test_visitPage (page: Page):
    url = "https://playwright.dev/"
    page.goto(url)
    expect(page).to_have_title(re.compile("Playwright"))
