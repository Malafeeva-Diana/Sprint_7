from faker import Faker

faker = Faker()
fakerRU = Faker(locale='ru_Ru')


def create_login_courier_random():
    login = faker.text(max_nb_chars=7) + str(faker.random_int(0, 999))
    return login


def create_courier_pass_random():
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_courier_name_random():
    name = faker.name()
    return name

