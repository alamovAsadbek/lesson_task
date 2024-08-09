from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import product_manager


class Admin:
    def __init__(self):
        self.create_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()

    @log_decorator
    def pricing(self):
        try:
            all_product: list = product_manager.read()
            is_there = False
            beginning: int = int(input("The beginning: "))
            ending: int = int(input("The ending: "))
            price: int = int(input("The price: "))
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
