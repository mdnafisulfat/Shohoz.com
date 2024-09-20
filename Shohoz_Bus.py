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
    driver.find_element(By.CSS_SELECTOR,
                        "a[class='border-2 border-[#079d494d] flex h-10 hover:border-[#079d494d] hover:text-primary-green items-center justify-center mr-2 rounded-[10px] text-primary-green w-[100px] ng-star-inserted']").click()

    if driver.current_url == "https://www.shohoz.com/bus-tickets":
        print("You are in Bus tickets site")
    else:
        print("You failed to select Bus tickets site")
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "button[class='btn-trip-type']").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Dhaka")
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "div[class='station-filter-dropdown'] button[type='button']").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#tocity").send_keys("Rangpur")
    time.sleep(1)

    journey_date_input = driver.find_element(By.ID, "doj")
    journey_date_input.click()
    time.sleep(2)

    journey_date = driver.find_element(By.XPATH, "//div[@class='btn-light bg-primary text-white'][normalize-space()='24']")
    journey_date.click()
    time.sleep(2)

    return_date_input = driver.find_element(By.ID, "dor")
    return_date_input.click()
    time.sleep(2)

    return_date = driver.find_element(By.XPATH, "//div[@class='datepicker-container']//div[@class='btn-light'][normalize-space()='27']")
    return_date.click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").submit()
    time.sleep(5)

    driver.close()
    print("Successfully completed the journey and return date selection process.")

except Exception as e:
    print(f"Something went wrong: {e}")
    driver.quit()
