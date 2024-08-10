from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import product_manager, balance_manager


class Admin:
    def __init__(self):
        self.create_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()

    @log_decorator
    def pricing(self) -> bool:
        try:
            all_product: list = product_manager.read()
            is_there = False
            beginning: int = int(input("The beginning: "))
            while True:
                if beginning < 1:
                    print("Number cannot be less than 1, Please try again.")
                    beginning = int(input("The beginning: "))
                    continue
                break
            ending: int = int(input("The ending: "))
            price: int = int(input("The price (uzs): "))
            for product in all_product:
                if product['beginning'] == beginning and product['ending'] == ending:
                    is_there = True
                    product['beginning'] = beginning
                    product['ending'] = ending
                    product['price'] = price
            if not is_there:
                data_id = product_manager.random_id()
                data = {
                    'id': data_id,
                    'beginning': beginning,
                    'ending': ending,
                    'price': price,
                    'create_data': self.create_data
                }
                if product_manager.append_data(data=data):
                    print('Product Added Successfully!')
                    return True
                print("Product Added Failed")
                return False
            if product_manager.write(data=all_product):
                print("Product Added Successfully")
                return True
            print("Product Not Added")
            return False
        except KeyError:
            print("Error")
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def show_sold(self) -> bool:
        all_sold: list = balance_manager.read()
        count: int = 1
        if len(all_sold) == 0:
            print("No sold yet")
            return False
        for sold in all_sold:
            if sold['balance'] < 1:
                print(f"{count}. User phone number: {sold['phone_number']},  Balance: {sold['balance'] * -1}, "
                      f"Price: {sold['price']} UZS, Time: {sold['create_data']}")
                count += 1
        if count == 0:
            print("No sold yet")
            return False
        return True

    @log_decorator
    def show_all_users(self):
        pass
