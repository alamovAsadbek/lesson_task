from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, balance_manager, product_manager


class User:
    def __init__(self):
        self.active_user = user_manager.get_active_user()

    @log_decorator
    def summ_count(self) -> int or bool:
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
    def balance_price(self, balance: int) -> int or bool:
        try:
            all_product = product_manager.read()
            for product in all_product:
                if product['beginning'] <= balance <= product['ending']:
                    return product['price']
            return 0
        except Exception as e:
            print(f'Error: {e}')
            return 0

    @log_decorator
    def add_balance(self) -> bool:
        try:
            print(f'Your balance is {self.summ_count()}')
            balance: int = int(input("Enter balance: "))
            balance_id: int = balance_manager.random_id()
            product_price = self.balance_price(balance)
            data = {
                'id': balance_id,
                'balance': balance,
                'phone_number': self.active_user['phone_number'],
                'price': product_price,
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

    @log_decorator
    def buy_product(self) -> bool:
        pass
