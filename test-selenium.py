from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service('/usr/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=Options)

# driver = webdriver.Firefox()

# # Thiết lập tùy chọn cho Firefox
# options = Options()
# # # # options.headless = True  # Uncomment this line to run Firefox in headless mode (no GUI)

# # # # Cấu hình Geckodriver
# service = Service(executable_path='/usr/bin/geckodriver')

# # # # Khởi động Firefox WebDriver với các tùy chọn
# driver = webdriver.Firefox(service=service, options=options)

try:
    # Truy cập trang YouTube
    driver.get("https://www.youtube.com/")
    
    # Đợi trang tải xong
    WebDriverWait(driver, 10).until(EC.title_contains("YouTube"))
    
    # Thực hiện các thao tác trên trang, nếu cần

    # Ví dụ: Tìm kiếm một video
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    # Đợi kết quả tìm kiếm xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
    
finally:
    # Đóng trình duyệt
    driver.quit()
