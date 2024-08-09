from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, balance_manager


class User:
    def __init__(self):
        self.active_user = user_manager.get_active_user()

    @log_decorator
    def summ_count(self):
        try:
            summ = 0
            all_balance = balance_manager.read()
            for balance in all_balance:
                if balance['phone_number'] == self.active_user['phone_number']:
                    summ += balance['balance']
            return summ
        except KeyError:
            return 0
        except IndexError:
            return 0
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def add_balance(self):
        try:
            print(f'Your balance is {self.summ_count()}')
            balance: int = int(input("Enter balance: "))
            data = {
                'balance': balance,
                'phone_number': self.active_user['phone_number'],
                'create_data': datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
            }
            if balance_manager.append_data(data=data):
                print(f'{balance} has been added to your balance')
                return True
            print("Something went wrong")
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def history_balance(self):
        print("Menu: History Balance")

    @log_decorator
    def history_product(self):
        print("Menu: Product History")
