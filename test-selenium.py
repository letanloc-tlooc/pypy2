from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Khởi động Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Truy cập trang đăng nhập GitHub
    driver.get("https://www.youtube.com/")
    # Đợi một vài giây để quá trình tạo repository hoàn tất
    time.sleep(10)
finally:
    # Đóng trình duyệt
    driver.quit()