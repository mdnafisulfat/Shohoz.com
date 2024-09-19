from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.shohoz.com/")
time.sleep(2)

try:
    driver.find_element(By.CSS_SELECTOR, "a[class='mr-2 pl-1 flex justify-start items-center rounded-[10px] w-[100px] h-10 border-2 border-transparent hover:border-[#079d494d] hover:text-primary-green relative']").click()
    if driver.current_url == "https://parks.shohoz.com/":
        print("You are in park site")
    else:
        print("You Fail to select park")

    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@placeholder='Select Location']").send_keys("Dhaka")

    time.sleep(5)
    driver.find_element(By.XPATH, "//span[@class='main_fw_600__O7Gmr main_fs_20__fi0fZ pe-5 text-light']").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,
                        "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(2)").click()
    if driver.current_url == "https://parks.shohoz.com/park/2":
        print("You are in Tickets Details")
    else:
        print("You Fail into tickets details page")

    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "div[class='entry-tickets'] div[class='pt-2 d-flex flex-md-row flex-column gap-2 justify-content-md-start justify-content-center flex-wrap align-items-center'] div div[class='bg-light box-sizing d-flex flex-column'] div[class='d-flex justify-content-between align-items-start gap-2 px-2 pt-2'] div button[type='button']").click()
    time.sleep(5)
    # needed to change
    driver.find_element(By.CSS_SELECTOR,
                        "button[class='main_bg_primary__eAAI- main_fw_600__O7Gmr main_fs_16__ZNR65 text-light border-0 rounded px-2 py-1 d-flex justify-content-between align-items-center']").click()
    time.sleep(5)

    driver.find_element(By.XPATH,
                        "//div[@class='d-none d-md-block']//div//div[1]//button[1]").click()
    time.sleep(5)


    driver.find_element(By.CSS_SELECTOR,
                        "button[class='main_bg_primary__eAAI- main_fs_20__fi0fZ main_fw_600__O7Gmr border-0 text-light w-100 cart-checkout-btn']").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,
                        "button[class='main_bg_primary__eAAI- main_fs_20__fi0fZ main_fw_600__O7Gmr border-0 text-light w-100 cart-checkout-btn']").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,
                        "input[placeholder='Enter Mobile Number']").send_keys("01786806814")
    driver.find_element(By.CSS_SELECTOR,
                        "input[placeholder='Enter Password']").send_keys("abcdefgh")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,
                        "button[class='main_bg_primary__eAAI- main_fs_14__uIQK0 main_fw_400__GhLuQ text-light rounded-1 p-1 border-0 w-100']").click()
    try:
        n
        driver.find_element(By.ID, "logoutButton")
        print("Login successful")
    except Exception:
        print("Using invalid credential you failed to Login")

    time.sleep(5)

    driver.close()
    print("Successfully")

except Exception:
    print("Sorry")

