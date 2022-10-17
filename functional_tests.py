
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create a new instance of the Firefox driver and navigate to the URL http://localhost:8000 and assert 'Django' in the title

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser  =  webdriver.Firefox(options=options)
browser.get( 'http://localhost:8000' )
assert  'Django'  in  browser.title