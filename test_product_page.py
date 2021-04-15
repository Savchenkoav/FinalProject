from .pages.product_page import ProductPage
import pytest
import time
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
                                  
#def test_guest_can_add_product_to_basket(browser, link):
#    link = f"{link}"
#    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                      # открываем страницу
#    page.should_not_be_success_message()
#    page.test_add_to_basket()
#    page.solve_quiz_and_get_code()
#    #time.sleep(10)
#    page.test_should_be_basket_message()
#    page.test_should_be_product_name_equal()
#    page.test_should_be_price_message()
#    page.test_should_be_price_equal()
@pytest.mark.xfail(reason="correct work")    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)    
    page.open()                      
    page.test_add_to_basket()
    page.should_not_be_success_message() 
    
def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)    
    page.open()                      
    page.should_not_be_success_message() 
    
@pytest.mark.xfail(reason="correct work")  
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   
    page.open()                     
    page.test_add_to_basket()
    page.should_dissapear_of_success_message() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


    
    
    