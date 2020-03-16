#!/usr/bin/env python3
# -*- encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import argparse

parser = argparse.ArgumentParser(description = "Capture CodeChef Questions as png images")
parser.add_argument("url", type = str, help = "URL of the CodeChef Problem/Question to save")
args = parser.parse_args()

options = webdriver.FirefoxOptions()
options.headless=True
browser = webdriver.Firefox(options=options) # Expecting Geckodrivers to be in PATH

browser.get(args.url)

result = urlparse(args.url)

browser.find_element_by_class_name("problem-container").screenshot("../pngs/" + result.path + ".png")

browser.delete_all_cookies()
browser.close()