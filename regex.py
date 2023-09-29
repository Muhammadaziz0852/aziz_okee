from playwright.sync_api import sync_playwright


def kun_uz_screenshot():
    url = 'https://www.kun.uz/news/category/jahon'
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        screenshot = page.screenshot(path='kun_uz_screenshot.png')
        browser.close()

    return screenshot


kun_uz_screenshot()





