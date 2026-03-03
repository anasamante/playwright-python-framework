def test_homepage_opens(page):
    assert "Automation Exercise" in page.title()
    print(f"Homepage loaded: {page.url}")