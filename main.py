import time

import data
import helpers
from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes. Conectado com sucesso")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO




    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        assert routes_page.click_comfort_active()
        time.sleep(10)



    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in routes_page.numero_confirmado()


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartao" in routes_page.confirm_card()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_comment(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in routes_page.comment_confirm()

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.switch_cobertor()
        assert routes_page.switch_cobertor_active() is True
        time.sleep(10)

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        for _ in range(2):
            routes_page.add_ice()
        assert int(routes_page.qnt_icecream()) == 2


    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        routes_page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.add_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.call_taxi()
        assert "Buscar carro" in routes_page.pop_up_show()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

