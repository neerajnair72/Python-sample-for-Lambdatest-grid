import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



class LTAutomate(unittest.TestCase):
    """
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section
    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
    """

    
    def setUp(self):
        """
        Setup remote driver
        Params
        ----------
        platfrom : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
        browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
        version :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/
        Result
        -------
        """
        # username: Username can be found at automation dashboard
        username="shubhamr@lambdatest.com"  
        # accessToken:  AccessToken can be genarated from automation dashboard or profile section
        accessToken="bKCQ8wHNM5QHi8m3c9vc9JecZjXeWN34SfNIEBYZywYAPoC87Z"
        # gridUrl: gridUrl can be found at automation dashboard
        gridUrl = "hub.lambdatest.com/wd/hub"

        


        
        desired_cap = {
            'platform' : "win10", 
            'browserName' : "chrome",
            'version' :  "94.0",
            # Resolution of machine
            "resolution": "1920x1080", 
            "name": "LambdaTest python google search test ",
            "build": "LambdaTest python google search build",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
             'goog:chromeOptions':{
                'prefs':{
                     "download.default_directory": "D:",
                # "download.prompt_for_download": False,
                # "download.directory_upgrade": False,
                 # "safebrowsing.enabled": True
                }
            }
                
        }
        options=webdriver.ChromeOptions()
        prefs={'download.prompt_for_download':False,'safebrowsing.enabled':True,"download.directory_upgrade": True,"download.default_directory": "D:"}
        options.add_experimental_option("prefs", prefs)

        # URL: https://{username}:{accessToken}@beta-hub.lambdatest.com/wd/hub
        url = "https://"+username+":"+accessToken+"@"+gridUrl
        
        print("Initiating remote driver on platfrom: "+desired_cap["platform"]+" browser: "+desired_cap["browserName"]+" version: "+desired_cap["version"])
        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor= url,
           # options=options,
        )
        

    
    def test_search_in_google(self):
        """
        Setup remote driver
        Params
        ----------
        Execute test:  navigate google.com search LambdaTest
        Result
        -------
        print title
        """
        driver = self.driver
        print("Driver initiated sucessfully.  Navigate url")
        #driver.get("https://www.google.com/ncr")
        driver.get('https://the-internet.herokuapp.com/geolocation')


        print("Searching lambdatest on google.com ")
        time.sleep(4)
      # elem = driver.find_element_by_id("uc-download-link")
        #elem.send_keys("lambdatest.com")
       # elem.click()
       # driver.find_element_by_id("uc-download-link").click()
       # time.sleep(2)
        #elem = driver.find_element_by_id("uc-download-link")
       # elem.click()

        #print("Printing title of current page :"+driver.title)
        driver.execute_script("lambda-status=passed")
        print("Requesting to mark test : pass")

    
    def tearDown(self):
        """
        Quit selenium driver
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()