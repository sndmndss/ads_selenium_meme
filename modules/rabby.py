from selenium.webdriver.support.wait import WebDriverWait
from data.constants import RABBY_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from helpers import delete_key


def rabby_login(driver, private_key, password=8901324567):
    wait = WebDriverWait(driver, 20)
    driver.get(RABBY_URL)
    print("PRESS F5 IN BROWSER!")
    rabby_button1 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div > div.rabby-container.pb-\[12px\] > div:nth-child(2) > div:nth-child(2)")))
    rabby_button1.click()
    input_confirm = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    input_confirm.send_keys(password)
    input_element = wait.until(EC.presence_of_element_located((By.ID, 'confirmPassword')))
    input_element.send_keys(password)
    rabby_button2 = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div > form > div.p-32.pt-0 > button")))
    rabby_button2.click()
    input_key = wait.until(EC.presence_of_element_located((By.ID, 'key')))
    input_key.send_keys(private_key)
    rabby_button3 = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "#root > div > form > div.bottom-0.left-0.w-full.flex.lg\:bottom-\[-24px\].z-10.footer.fixed > div > button")))
    rabby_button3.click()
    delete_key(private_key)
