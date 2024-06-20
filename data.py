class Data:
    login = 'ninja'
    password = '1234'
    name = 'Нинзя'
    courier = {'login': 'ninja', 'password': '1234', 'name': 'Нинзя'}
    wrong_name_courier = {'login': 'ninja', 'password': '1234'}
    wrong_password = {'login': 'ninja', 'password': '100147859'}

    Url_main_page = 'https://qa-scooter.praktikum-services.ru/'
    Url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    Url_create_login = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    Url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class OrderDate:
    order_scooter_black = {
        'name': 'Шрек',
        'lastName': 'Огр',
        'address': 'Сказочное болото, 15',
        'metroStation': 'Лубянка',
        'phone': '+79973381122',
        'rentTime': '1',
        'deliveryDate': '21-06-2024',
        'comment': 'Успею к Фионе? Надо спасти ее от зловещего дракона',
        'color': ['BLACK']
    }

    order_scooter_grey = {
        'name': 'Граф Монте',
        'lastName': 'Кристо',
        'address': 'Проспект Мира, 16',
        'metroStation': 'Проспект Мира',
        'phone': '+79991113357',
        'rentTime': '6',
        'deliveryDate': '22-06-2024',
        'comment': 'Очень спешу!',
        'color': ['GREY']
    }

    order_scooter_grey_and_black = {
        'name': 'Дядя',
        'lastName': 'Федор',
        'address': 'Хорошевское шоссе, 70',
        'metroStation': 'Полежаевская',
        'phone': '+79997774457',
        'rentTime': '',
        'deliveryDate': '23-06-2024',
        'comment': 'Хочу на море с Матроскиным и Шариком!!!А не вот это вот все.',
        'color': ['BLACK', 'GREY']
    }

    order_scooter_no_color = {
        'name': 'Василиса',
        'lastName': 'Премудрая',
        'address': 'Новинский бульвар, 11',
        'metroStation': 'Баррикадная',
        'phone': '+79998883322',
        'rentTime': '7',
        'deliveryDate': '24-06-2024',
        'comment': '',
        'color': []
    }


class TextAnswer:
    create_courier = '{"ok":true}'
    duplicate_courier = 'Этот логин уже используется. Попробуйте другой.'
    not_once_required_field = 'Недостаточно данных для создания учетной записи'
    not_login_courier = 'Недостаточно данных для входа'
    not_password_courier = 'Недостаточно данных для входа'
    no_such_username_and_password = 'Учетная запись не найдена'
