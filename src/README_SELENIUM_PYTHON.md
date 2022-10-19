# SELENIUM WEBDRIVER

-----
## 1. Define:
- Selenium supports automation through the use of WebDriver
- WebDriver is an API and protocol interface


## 2. Install:
- Install library (Python):
  `pip install selenium`
- Install browser
- Download browser driver (not need if using Driver Manager package)

## 3. Use Driver
Three ways:
### 3.1. Driver Management Software
- Import WebDriver Management:
from webdriver_manager.chrome import ChromeDriverManager 

- Import webdriver, service:
```python
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
```

- Use install() to get the location used by the manager and pass it into service class:
```python
service = Service(executable_path=ChromeDriverManager().install())
```

- Use Service instance when initializing the driver:
```python
driver = webdriver.Chrome(service=service)
```

### 3.2. PATH
- Download driver
- Add driver location to PATH:
```commandline
echo 'export PATH=$PATH:/path/to/driver' >> ~/.bash_profile
source ~/.bash_profile
```

- Or put the driver to available path: `echo $PATH`

- Check by running command: `chromedriver`

- Import webdriver, service:
```python
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
```

- Use driver:
```python
driver = webdriver.Chrome()
```

### 3.3. Hard Coded Location
- Import
```python
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
```

- Use driver:
```python
service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)
```

### 3.4. Extend
- Browser Options - [Capability](https://w3c.github.io/webdriver/#capabilities):
  - browserName
  - browserVersion
  - pageLoadStrategy # indicate when driver.get() will stop the hold o
    - normal
    - eager
    - none
  - platformName # OS
  - timeouts: # sessions
    - script 
    - pageLoad
    - implicit # locating an element

  Example:
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
  
    options = Options()
    options.page_load_strategy = 'normal'
    
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.google.com")
    
    driver.quit()
    ```



- Remote WebDiver
```python
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "Windows XP")

driver = webdriver.Remote(
    command_executor='http://www.example.com', # remote web 
    options=firefox_options
)
driver.get("http://www.google.com")

driver.quit() 
```


## 4. SELENIUM SCRIPTS:
8 basic components:
### 4.1. Take action on Browser (driver.)
  - Navigation:
    - get('url')
    - back
    - forward
    - refresh

  - alert
    - Alert
    - Confirm
    - Prompt

  - cookie
  - Frames
  - Windows and tab:
    - current_window_handle
    - title
    - current_url
    - switching windows or tabs
    - Create new window (or) new tab and switch
    - Closing a window or tab
    - quit(): Quitting the browser at the end of a session
    - Window management:
      - get, set size
      - get, set position
      - maximize_window()
      - minimize_window()
      - fullscreen_window()
      - save_screenshot('./image.png')
      - Execute Script
      - Print Page

### 4.2. Request browser info
  - https://www.selenium.dev/documentation/webdriver/interactions/

### 4.3. Waiting Strategy
  - https://www.selenium.dev/documentation/webdriver/waits/
  - Explicit wait:
    ```python
    from selenium.webdriver.support.wait import WebDriverWait
    
    
    def document_initialised(driver):
       return driver.execute_script("return initialised")

    driver.navigate("file:///race_condition.html")
    WebDriverWait(driver, timeout=10).until(document_initialised)
    ```

  - Implicit: polls the DOM for a certain duration when trying to find any element. 
  - Fluent Wait: ?

### 4.4.[Find an element](https://www.w3.org/TR/webdriver/#locator-strategies) (from selenium.webdriver.common.by import By)
  - find_element(), find_elements()
    - By.ID
    - By.CLASS_NAME
    - By.TAG_NAME
    - By.NAME
    - By.CSS_SELECTOR
    - By.XPATH
    - By.LINK_TEXT

### 4.5. Take action on element
  - https://www.selenium.dev/documentation/webdriver/elements/interactions/
    - send_keys("Selenium"): text, file upload
      - transfer file from client to remote
        ```python
        driver.get("http://sso.dev.saucelabs.com/test/guinea-file-upload")
        driver.find_element(By.ID, "myfile").send_keys("/Users/sso/the/local/path/to/darkbulb.jpg")
        ```
    - click()

#### 4.6. Request element information
- https://www.selenium.dev/documentation/webdriver/elements/information/
  - text
  - get_attribute
  - is_displayed()
  - is_enabled()
  - is_selected()
  - tag_name 
  - rect # Returns height, width, x and y coordinates referenced element 
  - value_of_css_property('color')
    
### 4.7. End the session
- driver.quit()

## 5. ACTIONS API:
- keyboard (Keys.)
- mouse, pen
- scroll wheel (Selenium 4.2)
- ActionChains(driver)\
        .move_to_element(clickable)\
        .pause(1)\
        .click_and_hold()\
        .pause(1)\
        .send_keys("abc")\
        .perform()
  ActionBuilder(driver).clear_actions()
