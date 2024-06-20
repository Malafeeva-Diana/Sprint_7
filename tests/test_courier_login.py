import allure
import requests
from data import Data, TextAnswer
from helpers import create_login_courier_random, create_courier_pass_random, create_courier_name_random


class TestLoginCourier:
    @allure.title('Проверка успешного логина курьера')
    @allure.description(
        'Создаём аккаунт курьера и логинимся на него, получаем статус 200 и убеждаемся, что id приходит')
    def test_courier_login_passed(self):
        payload = {'login': create_login_courier_random(),
                   'password': create_courier_pass_random(),
                   'name': create_courier_name_random()
                   }
        requests.post(Data.Url_create_courier, data=payload)
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка попытки логина курьера без поля login')
    @allure.description(
        'Пытаемся залогиниться на аккаунт без поля Логин и получаем ошибку 400 и соответствующий текст ответа')
    def test_not_login_courier(self):
        payload = {'login': '',
                   'password': create_courier_pass_random(),
                   'name': create_courier_name_random()
                   }
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 400 and response.json()['message'] == TextAnswer.not_login_courier

    @allure.title('Проверка попытки логина курьера без поля password')
    @allure.description(
        'Пытаемся залогиниться на аккаунт без поля Пароль и получаем ошибку 400 и соответствующий текст ответа')
    def test_not_password_courier(self):
        payload = {'login': create_login_courier_random(),
                   'password': '',
                   'name': create_courier_name_random()
                   }
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 400 and response.json()['message'] == TextAnswer.not_password_courier

    @allure.title('Проверка логина несуществующим курьером')
    @allure.description(
        'Пытаемся залогиниться несуществующим аккаунтом курьера, получаем ошибку 404 и соотвествующее сообщение')
    def test_no_such_username_and_password(self):
        payload = {'login': Data.wrong_name_courier,
                   'password': create_courier_pass_random(),
                   'name': create_courier_name_random()
                   }
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 404, response.json()['message'] == TextAnswer.no_such_username_and_password

    @allure.title('Проверка логина c неправильным паролем')
    @allure.description(
        'Пытаемся залогиниться в аккаунт курьера, получаем ошибку 404 и соотвествующее сообщение')
    def test_no_such_username_and_password(self):
        payload = {'login': create_login_courier_random(),
                   'password': Data.wrong_password,
                   'name': create_courier_name_random()
                   }
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 404, response.json()['message'] == TextAnswer.no_such_username_and_password
