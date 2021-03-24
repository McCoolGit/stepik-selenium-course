import pytest
import math
import time


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_UFO_text(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    browser.find_element_by_class_name("textarea").send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(2)
    text_to_compare = browser.find_element_by_class_name("smart-hints__hint").text
    assert text_to_compare == "Correct!", F"text is not compare {text_to_compare}"
