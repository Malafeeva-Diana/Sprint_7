import allure
import requests
from data import Data, TextAnswer
from helpers import create_login_courier_random, create_courier_pass_random, create_courier_name_random


class TestNewCourierCreate:
    @allure.title('Проверка создания аккаунта курьера')
    @allure.description('Создаём аккаунт курьера и проверяем, что код ответа равен 201 и тело ответа соотвествует '
                        'документации')
    def test_create_courier(self):
        payload = {'login': create_login_courier_random(),
                   'password': create_courier_pass_random(),
                   'name': create_courier_name_random()
        }
        response = requests.post(Data.Url_create_courier, data=payload)
        assert response.status_code == 201, response.json == TextAnswer.create_courier

    @allure.title('Проверка невозможности создания двух одинаковых аккаунтов курьеров')
    @allure.description('Посылаем два запроса с одинаковыми регистрационными данными и получаем ошибку и сообщение о '
                        'ней')
    def test_duplicate_courier(self):
        payload = {'login': Data.login,
                   'password': create_courier_pass_random(),
                   'name': create_courier_name_random
                   }
        requests.post(Data.Url_create_courier, data=payload)
        response = requests.post(Data.Url_create_courier, data=payload)
        assert response.status_code == 409, response.json()['message'] == TextAnswer.duplicate_courier

    @allure.title('Проверка невозможности регистрации курьера без одного обязательного поля')
    @allure.description('Посылаем запрос без поля "Пароль" и пытаемся создать аккаунт, получаем ошибку и её текст')
    def test_not_once_required_field(self):
        payload = {'login': create_login_courier_random(),
                   'name': create_courier_name_random()
                   }
        response = requests.post(Data.Url_create_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == TextAnswer.not_once_required_field
