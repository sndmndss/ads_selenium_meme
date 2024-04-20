from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.constants import XVERSE_WALLET
from data.css_selectors import STAKELAND_BUTTON_2_CSS_SELECTOR
from time import sleep


def login_xverse(driver, password=8901324567):
    driver.get(XVERSE_WALLET)
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[1]/div/button"))
    )
    button.click()
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/button[1]"))
    )
    button.click()
    input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div[2]/input")))
    input.send_keys(8901324567)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div[4]/div[2]/button"))
    )
    button.click()
    input = wait.until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div[2]/input")))
    input.send_keys(8901324567)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div[3]/div[2]/button"))
    )
    button.click()
