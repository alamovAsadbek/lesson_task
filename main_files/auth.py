import hashlib

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class Auth:
    def __init__(self):
        self.__phone_number = "990690142"
        self.__password = "admin"

    @log_decorator
    def register(self) -> bool:
        try:
            full_name: str = input('Full name: ').strip()
            phone_number: int = int(input('Phone number (+998): ').strip())
            if self.__phone_number == phone_number.__str__():
                print('Phone number already taken')
                return False
            else:
                if user_manager.check_phone_number(phone_number=phone_number):
                    print('Phone number already taken')
                    return False
            while True:
                password = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
                confirm_password = hashlib.sha256(input("Confirm password: ").encode('utf-8')).hexdigest()
                if password == confirm_password:
                    break
                print('Passwords do not match')
            user_id = user_manager.random_id()
            data = {
                'id': user_id,
                'full_name': full_name,
                'password': password,
                'confirm_password': confirm_password,
                'phone_number': phone_number,
                'is_login': False
            }
            if user_manager.append_data(data=data):
                print('User registered')
                return True
            print('An error occurred')
            return False
        except ValueError:
            print("Invalid input")
            return False
        except Exception as e:
            print(f'An error occurred: {e}')
            return False

    @log_decorator
    def login(self) -> dict:
        try:
            all_users: list = user_manager.read()
            phone_number: int = int(input('Enter phone number: ').strip())
            password: str = hashlib.sha256(input('Enter password (+998 ): ').strip().encode('utf-8')).hexdigest()
            if phone_number.__str__() == self.__phone_number and hashlib.sha256(
                    self.__password.encode('utf-8')).hexdigest() == password:
                print('Login successful')
                return {'is_login': True, 'role': 'admin'}
            if not user_manager.check_phone_number(phone_number=phone_number):
                print('Phone number not found')
                return {'is_login': False, 'role': "admin"}
            for user in all_users:
                if user['phone_number'] == phone_number and user['password'] == password:
                    user['is_login'] = True
                    if user_manager.write(data=all_users):
                        print('Login successful')
                        return {'is_login': True, 'role': 'user'}
            print('Login failed')
            return {'is_login': False, 'role': 'admin'}
        except ValueError:
            print('Invalid input')
            return {'is_login': False, 'role': 'admin'}
        except Exception as e:
            print(f'An error occurred: {e}')
            return {'is_login': False, 'role': 'admin'}

    @log_decorator
    def logout(self) -> bool:
        try:
            all_users: list = user_manager.read()
            for user in all_users:
                user['is_login'] = False
            user_manager.write(all_users)
            return True
        except ValueError:
            return True
