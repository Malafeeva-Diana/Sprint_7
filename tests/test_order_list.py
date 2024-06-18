import allure
import requests
from data import Data


class TestGetListOrder:
    @allure.title('Проверка получения списка заказов')
    @allure.description(
        'Проверяем получение общего списка заказов, получаем статус 200 и проверяем, что список не пустой')
    def test_get_list_order(self):
        response = requests.get(Data.Url_create_order)
        assert response.status_code == 200 and response.json()["orders"] != []
