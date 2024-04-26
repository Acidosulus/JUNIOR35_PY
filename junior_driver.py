from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from my_library import *
from junior_good import *
import colorama
from colorama import Fore, Back, Style
import time


class juniorWD:
    def init(self):
        print(Fore.RED + 'Chrome Web Driver '+Fore.YELLOW +"https://junior-35.ru/"+Fore.RESET)
        chrome_options = webdriver.ChromeOptions()
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        #chrome_prefs["profile.default_content_settings"] = {"images": 2}
        #chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        chrome_options.add_argument('--disable-gpu')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver.minimize_window()

        #self.driver.find_element_by_name("login").send_keys("Lessie")
        #self.driver.find_element_by_name("pass").send_keys("uslm1976")
        #self.driver.find_element_by_class_name("button").click()
        #self.driver.find_element_by_xpath("//input[contains(@value,'Войти')]").click()
    def __init__(self):
        self.init()

    def Get_HTML(self, curl):
        self.driver.get(curl)
        return self.driver.page_source

    def Get_List_Of_Links_On_Goods_From_Catalog(self, curl):
        print(Fore.RED + 'Список товаров каталога: ' + Fore.YELLOW + curl + Fore.RESET)
        lst = []
        lst_goods = []
        while len(curl) > 1:
            lst.append(curl)
            curl = self.Get_Link_On_Next_Catalog_Page(curl)
            print(Fore.RED + 'Список товаров каталога, следущая страница: ' + Fore.YELLOW + curl + Fore.RESET)
            elements = self.driver.find_elements_by_class_name('name')
            for element in elements:
                lc_link = element.get_attribute('href')
                if lc_link not in lst_goods:
                    lst_goods.append(lc_link)
        return lst_goods

        lst = []
        ln_count = 0
        for i in range(120):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            elements = self.driver.find_elements_by_class_name('name')
            print(Fore.YELLOW + '  Wait infinity scroll: 3 seconds - ' + str(i+1)+' times' + Fore.RESET)
            if len(elements) == ln_count: break
            else: ln_count = len(elements)

        elements = self.driver.find_elements_by_class_name('name')
        for element in elements:
            lc_link = element.get_attribute('href')
            if lc_link not in lst:
                lst.append(lc_link)

        return lst

    def Get_Link_On_Next_Catalog_Page(self, pc_url:str):
        lc_html = self.Get_HTML(pc_url)
        lc_link = sx(lc_html, '<link rel="next" href="', '"')
        return lc_link

    #def Get_List_Pages_Of_Catalog(self, c_link_on_first_catalog):
    #    ll_link_on_first_catalog = []
    #    lc_link_on_next_page = c_link_on_first_catalog
    #    while len(lc_link_on_next_page) > 5:
    #        ll_link_on_first_catalog.append(lc_link_on_next_page)
    #        self.Get_HTML(lc_link_on_next_page)
    #        lc_link_on_next_page = self.Get_Link_On_Next_Catalog_Page()
    #    return ll_link_on_first_catalog

    def Write_To_File(self, cfilename):
        file = open(cfilename, "w", encoding='utf-8')
        file.write(self.driver.page_source)
        file.close()
