import json
import os
import random
import threading
if not os.path.exists('datas'):
    os.makedirs('datas')


class JsonManager:
    def __init__(self, file_name):
        self.file_name: str = file_name

    # context manager
    def open_file(self, mode: str):
        file = open(self.file_name, mode)
        yield file
        file.close()

    def read(self) -> dict or bool:
        try:
            with self.open_file(mode='r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            with self.open_file(mode="w") as file:
                json.dump([], file, indent=4)
                return []

    def write(self, data) -> bool:
        with self.open_file(mode="w") as file:
            json.dump(data, file, indent=4)
            return True

    def check_phone_number(self, phone_number) -> bool:
        all_users: list = self.read()
        try:
            for user in all_users:
                if user['phone_number'] == phone_number:
                    return True
            return False
        except KeyError:
            return False

    def append_data(self, data) -> bool:
        try:
            all_data: list = self.read()
            all_data.append(data)
            self.write(all_data)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    def get_active_user(self) -> dict or bool:
        all_users: list = self.read()
        try:
            for user in all_users:
                if user['is_login']:
                    return user
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    def get_data(self, data_id) -> dict or bool:
        all_users: list = self.read()
        try:
            for data in all_users:
                if data['id'] == data_id:
                    return data
            return False
        except KeyError:
            return False

    def random_id(self):
        try:
            all_data: list = self.read()
            while True:
                random_number: int = random.randint(1, 9999)
                for data in all_data:
                    if data['id'] == random_number:
                        break
                return random_number
        except Exception as e:
            print(f'Error: {e}')
            return False


user_manager = JsonManager(file_name='datas/users.json')
balance_manager = JsonManager(file_name='datas/balance.json')
product_manager = JsonManager(file_name='datas/product.json')
