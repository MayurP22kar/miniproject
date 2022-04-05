import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")
time.sleep(5)
#############################################################################################################
############################ ONLY PROVIDE YOUR CREDENSIALS AND RUN THE PROGRAM ##############################
name = "EMAIL ADDRESS"
passd= 'PASSWORD'
path = "PATH of YOUR FILE "
##############################################################################################################
##################################################################################################################
driver.find_element(By.XPATH,'//*[@id="login_Layer"]/div').click()

wait = WebDriverWait(driver,20)
try:
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[2]/div/form/div[2]/input')))
    username.send_keys(name)
    password = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[3]/div[2]/div/form/div[3]/input')))
    password.send_keys(passd)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[2]/div/form/div[6]/button').click()
except:
    print('element not found')


time.sleep(5)

action = ActionChains(driver)

try:
    my_link = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/ul[2]/li[2]/a/div[2]')))
except:
    print('not found')
edit = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/ul[2]/li[2]/div/ul[1]/li[1]/a')
action.move_to_element(my_link).move_to_element(edit).click().perform()

time.sleep(5)

try:
    driver.find_element(By.XPATH,'//*[@id="attachCV"]').send_keys(path)
    print('update successfully')
except:
    print('upload not found')

# driver.refresh()
