from selenium import webdriver
from tkinter import filedialog
from tkinter import *
import time
browser = webdriver.Chrome(executable_path='E:\hritik\pystro\chromedriver.exe')
browser.get('https:/www.caloriemama.ai/api')
upload = browser.find_element_by_class_name('file-upload')
root=Tk()
root.filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("jpeg files","*.jpg"),("all files",".*")))
upload.send_keys(root.filename)
time.sleep(5)
get=browser.find_element_by_class_name('group-name')
print(get.text)
browser.quit()