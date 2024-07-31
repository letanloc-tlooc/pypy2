from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình dịch vụ và tùy chọn Firefox
service = Service('/usr/bin/geckodriver')
options = Options()
# Thêm tùy chọn chạy Firefox không giao diện người dùng
options.add_argument('--headless')

# Khởi tạo driver
driver = webdriver.Firefox(service=service, options=options)

try:
    # Truy cập trang YouTube
    driver.get("https://www.youtube.com/")
    
    # Đợi trang tải xong
    WebDriverWait(driver, 10).until(EC.title_contains("YouTube"))
    
    # Tìm kiếm một video
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    # Đợi kết quả tìm kiếm xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
    
finally:
    # Đóng trình duyệt
    driver.quit()
