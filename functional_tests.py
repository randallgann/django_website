
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):
    
        def setUp(self):
            options = Options()
            options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            self.browser = webdriver.Firefox(options=options)
    
        def tearDown(self):
            self.browser.quit()
    
        def test_can_start_a_booking_(self):

            # user goes to the booking page
            self.browser.get('http://localhost:8000')
    
            # She notices the page title and header mention alabaster trailer
            self.assertIn('Trailer Bookings', self.browser.title)
            self.fail('Finish the test!')

            # She is invited to choose a date and time to rent the trailer.


            # She chooses a date and time and clicks the 'Rent' button.

            # She is taken to a page that shows her the date and time she has chosen.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


  




# She is also shown a confirmation number.

# She is invited to enter her name and email address.

# She enters her name and email address and clicks the 'Confirm' button.

# She is taken to a page that shows her the date and time she has chosen, her name and email address, and the confirmation number.

# A confirmation email is sent to her email address.

# satisfied, she goes back to sleep
