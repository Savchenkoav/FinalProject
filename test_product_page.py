from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.test_add_to_basket()
    page.solve_quiz_and_get_code()
    page.test_should_be_basket_message()
    page.test_should_be_product_name_equal()
    page.test_should_be_price_message()
    page.test_should_be_price_equal()
    
    