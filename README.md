# selenium

## Getting Started

### Prerequisites

- Install brew
- Install pip

### Installing

1. Install Selenium

    ```
    $ pip install selenium
    ```

1. Install Chrome Driver

    ```
    $ brew cask install chromedriver
    ```

    and Confirm that Chrome Driver has been installed

    ```
    $ brew cask list
      chromedriver
    ```

## Create Test

```
1. $ touch test.py
1. $ vi test.py
```


```python
# test.py

from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://github.com/triton27/selenium"); # open URL
driver.save_screenshot('screen.png') # take a screen_shot
driver.close() # close web_page
driver.quit() # quit browser
```

## Run Test

```
$ python test.py
```
