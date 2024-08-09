from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class User:
    def __init__(self):
        self.active_user = user_manager.get_active_user()

    @log_decorator
    def summ_count(self):
        pass

    @log_decorator
    def add_balance(self):
        try:
            balance: int = int(input("Enter balance: "))
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def history_balance(self):
        print("Menu: History Balance")

    @log_decorator
    def history_product(self):
        print("Menu: Product History")
