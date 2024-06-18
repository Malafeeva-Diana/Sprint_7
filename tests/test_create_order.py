import allure
import pytest
import requests
from data import OrderDate, Data
import json


class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Создание заказа с различным выбором цвета самоката')
    @pytest.mark.parametrize(
        'payload',
        [
            OrderDate.order_scooter_black,
            OrderDate.order_scooter_grey,
            OrderDate.order_scooter_grey_and_black,
            OrderDate.order_scooter_no_color
        ]
    )
    def test_create_order(self, payload):
        payload_string = json.dumps(payload)
        response = requests.post(Data.Url_create_order, data=payload_string)
        assert response.status_code == 201, 'track' in response.text
