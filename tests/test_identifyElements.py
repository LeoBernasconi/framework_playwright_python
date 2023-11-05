import re
from playwright.sync_api import Page, expect

#I NEED TO RESET ALL THIS, FOCUSING ON ACTIONS INSTEOD OF ELEMENTS
#Create a before to visit the URL
def test_locateInput(page: Page):
    page.get_by_label("Name").fill("Leo")
    page.pause()

def test_locateButton(page: Page):
    #Exact name of the button
    page.get_by_role("button", name=re.compile("Submit")).click()
    #Name ignoring uppercase/lowercase
    page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()

def test_locateText(page: Page):
    url = "https://rahulshettyacademy.com/angularpractice/"
    page.goto(url)
    #Locate text
    text_to_search = "Leo"
    expect(page.get_by_role("heading", name = text_to_search)).to_be_visible

def test_locateCheckbox(page: Page):
    url = "https://rahulshettyacademy.com/angularpractice/"
    page.goto(url)
    page.get_by_role("checkbox", name="Check me out if you Love IceCreams!").check()
