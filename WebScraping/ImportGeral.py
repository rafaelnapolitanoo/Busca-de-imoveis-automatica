from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ! options é para quando o selenium abre e fecha sozinho
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)


#from selenium import webdriver from selenium.webdriver.chrome.service 
#import Service 
#service = Service() 
#options = webdriver.ChromeOptions() 
#driver = webdriver.Chrome(service=service, options=options)