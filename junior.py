from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from my_library import *
import sys
from junior_driver import *
from junior_good import *
import colorama
from colorama import Fore, Back, Style


def unload_one_good(lc_link_on_good: str):
    print(Fore.YELLOW + 'Товар: ' + Fore.BLACK + Back.LIGHTWHITE_EX + lc_link_on_good + Fore.RESET + Back.RESET)
    lo_good = junior_good(lo_junior, lc_link_on_good)
    print(Fore.YELLOW + "Артикул: " + Fore.LIGHTGREEN_EX, lo_good.article, Fore.RESET)
    print(Fore.YELLOW + "Название:" + Fore.LIGHTGREEN_EX, lo_good.name, Fore.RESET)
    print(Fore.YELLOW + "Размеры:" + Fore.LIGHTGREEN_EX, lo_good.size_list, Fore.RESET)
    print(Fore.YELLOW + "Цена:" + Fore.LIGHTGREEN_EX, lo_good.price, Fore.RESET)
    print(Fore.YELLOW + "Цвета:" + Fore.LIGHTGREEN_EX, lo_good.colors, Fore.RESET)
    print(Fore.YELLOW + "Описание:" + Fore.LIGHTGREEN_EX, lo_good.description, Fore.RESET)
    print(Fore.YELLOW + "Картинки:" + Fore.LIGHTGREEN_EX, lo_good.pictures, Fore.RESET)

def unload_catalog_junior(lc_first_page_of_catalog:str, lc_filename:str):
        price = Price(lc_filename+'.csv')
        lo_junior = juniorWD()
        ll_list_links_on_goods = lo_junior.Get_List_Of_Links_On_Goods_From_Catalog(lc_first_page_of_catalog)
        for g in ll_list_links_on_goods:
            if is_price_have_link(lc_filename + '.csv', g):
                print(Fore.LIGHTRED_EX, 'Товар уже имеется в прайсе:', Fore.YELLOW, g, Fore.RESET)
                continue
            try: lo_good = junior_good(lo_junior, g)
            except:
                try:
                    lo_junior = juniorWD()
                    lo_good = junior_good(lo_junior, g)
                except:
                    lo_junior = juniorWD()
                    lo_good = junior_good(lo_junior, g)
            if len(lo_good.size) > 0:
                price.add_good('',
                               prepare_str(lo_good.article).strip() + ' ' + prepare_str(lo_good.name).strip(),
                               prepare_str(lo_good.description),
                               f"{round(float(prepare_str(lo_good.price).replace(',', '.').replace(' ','')), 2)}",
                               '15',
                               prepare_str(g),
                               prepare_for_csv_non_list(lo_good.pictures),
                               prepare_for_csv_list(lo_good.size)
                               )
                price.write_to_csv(lc_filename + '.csv')
        lo_junior.driver.quit()


########################################################################################################################

#st = '|-_<a href=/katalog/djempera-tuniki/djemper-dj285-pudra-4240>ДЖ285</a>_'
#print(st.find('<'))
#print('<' + sx(st, '<', '>') + '>')
#print(st.replace('<' + sx(st, '<', '>') + '>',''))
#exit()

colorama.init()

########################################################################################################################
#lo_junior = juniorWD()
#ll_list_links_on_goods = lo_junior.Get_List_Of_Links_On_Goods_From_Catalog('https://junior35.ru/devochkam?available_sizes=1')
#print(ll_list_links_on_goods)
#exit()
#reverse_csv_price(r'g:\JUNIOR35_PY\scvs\devochki.csv')
#exit()
########################################################################################################################




#price = Price()
#lo_junior = juniorWD()
#lst = lo_junior.Get_List_Of_Links_On_Goods_From_Catalog('http://newskazka.ru/katalog/shtuchnyiy-tovar/sh-t--odejda')
#lo_good = junior_good(lo_junior, 'http://newskazka.ru/katalog/odejda/odejda-detskaya/shkolnaya-odejda/bluzka-dlya-devochki-94665')
#lo_good = junior_good(lo_junior, 'http://newskazka.ru/katalog/odejda/odejda-detskaya/tuniki-i-bluzyi-detskie/bluzka-dlya-devochki--tsepochka-110396')

#wd = juniorWD()
#print(wd.Get_List_Of_Links_On_Goods_From_Catalog('https://junior35.ru/devochkam.html'))
#wd.driver.quit()

#lo_good = junior_good(wd, 'https://junior35.ru/catalog/littlemaven/futbolka_little_maven_art_lm1077')
#unload_catalog_junior(r'https://junior35.ru/boinc.html?vendor=15', r'g:\JUNIOR35_PY\scvs\test')



if sys.argv[1] == 'good' or sys.argv[1] == 'catalog':
    if sys.argv[1] == 'catalog':
        unload_catalog_junior(sys.argv[2], sys.argv[3])
        reverse_csv_price(sys.argv[3]+'.csv')
    if sys.argv[1] == 'good':
        lo_junior = juniorWD()
        print(sys.argv[2])
        lo_good = junior_good(lo_junior, sys.argv[2])
else: print(Fore.LIGHTRED_EX + 'Неверный формат параметров' + Fore.RESET)

#unload_catalog_junior('http://newskazka.ru/katalog/shtuchnyiy-tovar/sh-t--odejda','Одежда')



