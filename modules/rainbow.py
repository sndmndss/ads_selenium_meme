from data.constants import *
from helpers import wait_for_tab_to_load, rainbow_fill


def rainbow_login(driver, key: str):
    window_handles = driver.window_handles
    wait_for_tab_to_load(driver, window_handles[1])
    driver.switch_to.window(window_handles[1])
    driver.get(RAINBOW_LINK)
    rainbow_fill(driver, key)
