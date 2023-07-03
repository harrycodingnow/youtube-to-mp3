import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('disable-extensions')
options.add_argument('incognito')

def on_button_click():
    music_name = entry.get()
    browser = webdriver.Chrome(options=options)
    wait = WebDriverWait(browser, 10)
    
    try:
        url = 'https://www.backupmp3.com/zh/'
        browser.get(url)
        
        element = wait.until(EC.presence_of_element_located((By.ID, 'url')))
        element.send_keys(music_name)
        
        element = wait.until(EC.presence_of_element_located((By.ID, 'conversionWrapper')))
        element.click()
        
        element = wait.until(EC.presence_of_element_located((By.ID, 'DownloadMP3')))
        element.click()
        
        original_window_handle = browser.current_window_handle
        for window_handle in browser.window_handles:
            if window_handle != original_window_handle:
                browser.switch_to.window(window_handle)
                break
        browser.close()
        browser.switch_to.window(original_window_handle)
        
        text_to_scroll = "下載 MP3"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{text_to_scroll}')]")))
        browser.execute_script("arguments[0].remove()", element)
        
        element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{text_to_scroll}')]")))
        element.click()
        sleep(10)
        browser.quit()
    
    except Exception as e:
        print("An error occurred:", str(e))
        browser.quit()

window = tk.Tk()
window.title("Youtube to MP3")
label = tk.Label(window, text="Youtube to MP3", font=("Arial Bold", 16))
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

button = tk.Button(window, text="Download", command=on_button_click)
button1 = tk.Button(window, text="Quit", command=window.quit)
button.pack()
button1.pack()

window.mainloop()
