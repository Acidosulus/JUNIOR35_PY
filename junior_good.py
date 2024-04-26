from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from my_library import *
from junior_driver import *
import colorama
from colorama import Fore, Back, Style


class junior_good:
    def __init__(self, ol_junior, lc_link):
        print(Fore.LIGHTGREEN_EX, 'Товар: ', Fore.LIGHTBLUE_EX, lc_link, Fore.RESET)
        ol_junior.Get_HTML(lc_link)
        self.name = ''
        self.article = ''
        self.description = ''
        self.price = ''
        self.pictures = []
        self.size = []
        #try:self.name = sx(ol_junior.driver.page_source, '<h1>', '</h1>').strip()
        try:self.name = ol_junior.driver.find_element_by_class_name('product-title').text.strip()
        except: pass
        print('   ', Fore.LIGHTMAGENTA_EX, 'Название:', Fore.LIGHTYELLOW_EX, self.name, Fore.RESET)

        try: self.article = ol_junior.driver.find_element_by_class_name('articul').text
        except: pass
        print('   ', Fore.LIGHTMAGENTA_EX, 'Артикул: ', Fore.LIGHTYELLOW_EX, self.article, Fore.RESET)

        try: self.description =  ol_junior.driver.find_element_by_class_name('product-options').text.replace('\n', ' ').strip() + ' '+\
                            ol_junior.driver.find_element_by_class_name('tabs__content').text.replace('\n', ' ').strip() + ' '
        except:pass
        print('   ', Fore.LIGHTMAGENTA_EX, 'Описание:', Fore.LIGHTYELLOW_EX, self.description, Fore.RESET)

        try: self.price = ol_junior.driver.find_element_by_class_name('new-price').text.replace('₽', ' ').strip()
        except:pass
        print('   ', Fore.LIGHTMAGENTA_EX, 'Цена:    ', Fore.LIGHTYELLOW_EX, self.price, Fore.RESET)

        self.pictures = []
        try:
            lc_picture = sx(ol_junior.driver.page_source, '<img class="product-common-image" src="', '"').strip()
            if len(lc_picture) > 0:
                self.pictures.append('https://junior-35.ru/' + lc_picture)
        except:pass
        lc_picture = ''
        try:
            elements = ol_junior.driver.find_elements_by_class_name('swiper-slide')
            for element in elements:
                lc_picture = 'https://junior-35.ru/' + sx(element.get_attribute('innerHTML'), '<img class="" src="', '"')
                if lc_picture.count('prod_thumb') == 0 and len(lc_picture) > len('https://junior-35.ru/'):
                    self.pictures.append(lc_picture)
        except:pass
        print('   ', Fore.LIGHTMAGENTA_EX, 'Картинки:', Fore.LIGHTYELLOW_EX, self.pictures, Fore.RESET)

        self.size = []
        try:
            lc_table = ol_junior.driver.find_element_by_class_name('size-table').get_attribute('innerHTML').replace('\n', ' ').strip()
            for i in range(lc_table.count('<tr>')+1):
                lc_section = sx(lc_table, '<tr>', '</tr>', i).strip()
                lc_size    = sx(lc_section, '<td>', '</td>', 1).strip()
                lc_count   = sx( sx(lc_section, '<td>', '</td>', 2), '<span class="product__size-count">', '<').strip()
                if len(lc_size)>0 and lc_count.isdigit():
                    self.size.append('Размер: '+lc_size+' - Остаток: '+lc_count)
                    print('     ',Fore.YELLOW + 'Размер: ' + Fore.LIGHTYELLOW_EX + lc_size + Fore.WHITE + '     Остаток: ' + Fore.LIGHTWHITE_EX + lc_count + Fore.RESET)
        except: pass

