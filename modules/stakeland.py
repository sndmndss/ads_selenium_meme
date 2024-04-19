from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.constants import STAKELAND
from data.css_selectors import STAKELAND_BUTTON_2_CSS_SELECTOR
from time import sleep


def stakeland(driver):
    driver.get(STAKELAND)
    wait = WebDriverWait(driver, 30)
    try:
        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[2]/button"))
        )
        button.click()
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div[3]/button[2]"))
        )
        button.click()
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, STAKELAND_BUTTON_2_CSS_SELECTOR))
        )
        button.click()
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/button"))
        )
        button.click()
        sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/button"))
        )
        button.click()
        for handle in windows:
            driver.switch_to.window(handle)
            if driver.title == "Stakeland - Farm":
                break
        sleep(1)
        driver.execute_script("""
        var xpath = '/html/body/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[3]/div[1]/div/div';
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {
            element.click();
        }
        """)
        sleep(1)
        button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/div/div[3]/div[3]/button"))
        )
        button.click()
        sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[2]/button"))
        )
        button.click()
        for handle in windows:
            driver.switch_to.window(handle)
            if driver.title == "Stakeland - Farm":
                break
        sleep(1)
        button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[8]/div/div/div/div[3]/div[3]/button"))
        )
        button.click()
        button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/form/fieldset/input[1]"))
        )
        button.click()
    except Exception as e:
        print(str(e))
