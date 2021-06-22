from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://squid-kale-ngrp.squarespace.com/config/pages/5ffcf530bf58d440b220716a')

def login_to_squarespace(username,password):
    username_element = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/input")
    username_element.send_keys(username)
    password_element = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/input")
    password_element.send_keys(password)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/button").click()

def wait_for_page_to_load(seconds, class_name):
    time.sleep(seconds)
    try:
        browser.find_element_by_class_name(class_name)
        print("PAGE LOADED")
    except:
        print("ERROR:: page did not load could not find class: ", class_name)

def duplicate():
    browser.find_element_by_class_name("css-it1j3z").click() # click ...
    dropdown_items = browser.find_elements_by_class_name("css-dt15ob")
    duplicate_button = [item for item in dropdown_items if "DUPLICATE" == item.text][0]
    duplicate_button.click()
    print("DUPLICATED")

def edit_with_map():
    # click the draft
    browser.find_element_by_class_name("_16pKNQB2c css-n8hblf").click() # click the draft duplicated business
    # click the edit button 
    browser.find_element_by_class_name(" _2t47SrmXZ undefined i-5B3bsbH _3VRcd9E3s").click() # click the draft duplicated business
    # get the class of the Title, update 
    browser.find_element_by_class_name(" _2t47SrmXZ undefined i-5B3bsbH _3VRcd9E3s").click() # click the draft duplicated business
    print("Editting")
    # access the database

def main():
    login_to_squarespace("username", "password")
    wait_for_page_to_load(15, "css-it1j3z")
    duplicate()

main()
