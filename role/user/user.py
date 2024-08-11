from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.email_sender import invite_friend
from main_files.json_manager import user_manager, balance_manager, product_manager, message_manager


class User:
    def __init__(self):
        self.active_user = user_manager.get_active_user()
        self.__admin_email = 'alamovasad@gmail.com'

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
    def show_product_price(self):
        try:
            all_products: list = product_manager.read()
            count = 1
            for product in all_products:
                yield (f"{count}. The beginning: {product['beginning']},  The end: {product['ending']}, "
                       f"Price: {product['price']} UZS")
                count += 1
            if count == 1:
                print("Product not found")
                yield False

        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def show_all_balance(self):
        try:
            all_balance = balance_manager.read()
            for balance in all_balance:
                if balance['phone_number'] == self.active_user['phone_number']:
                    yield balance
        except KeyError:
            print("No balance found")
            yield False
        except Exception as e:
            print(f'Error: {e}')
            yield False

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
            for product in self.show_product_price():
                if product is False:
                    print("Something went wrong")
                    return False
                print(product)

            print(f'\nYour balance is {self.summ_count()}\n')
            balance: int = int(input("Enter balance: "))
            while balance < 1:
                print("Number cannot be less than 1, Please try again.")
                balance: int = int(input("Enter balance: "))
            balance_id: int = balance_manager.random_id()
            data = {
                'id': balance_id,
                'balance': balance,
                'phone_number': self.active_user['phone_number'],
                'price': 0,
                'create_data': datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
            }
            if balance_manager.append_data(data=data):
                print(f"You added {balance} to your balance")
                return True
            print("Something went wrong")
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def history_balance(self):
        user_balance: int = self.summ_count()
        count = 1
        if user_balance is False:
            print("Something went wrong")
            return False
        print("Your balance is " + str(user_balance) + '\n')
        for balance in self.show_all_balance():
            if balance['phone_number'] != self.active_user['phone_number']:
                continue
            if balance is False:
                print("Something went wrong")
                return False
            elif balance['balance'] > 1:
                print(
                    f"{count}. Status: Balance replenishment, Balance: {balance['balance']}, "
                    f"Time: {balance['create_data']}")
                count += 1
            elif balance['balance'] < 1:
                print(f"{count}. Status: Product purchased, Balance: {balance['balance'] * -1}, "
                      f"Price: {balance['price']} UZS, Time: {balance['create_data']}")
                count += 1
            else:
                print("Something went wrong")
                return False
        if count == 1:
            print("Data not available")
            return False
        return True

    @log_decorator
    def history_product(self):
        user_balance: int = self.summ_count()
        count = 1
        if user_balance is False:
            print("Something went wrong")
            return False
        print("Your balance is " + str(user_balance) + '\n')
        for balance in self.show_all_balance():
            if balance['phone_number'] != self.active_user['phone_number']:
                continue
            if balance is False:
                print("Something went wrong")
                return False
            elif balance['balance'] < 1:
                print(f"{count}. Status: Product purchased, Balance: {balance['balance'] * -1}, "
                      f"Price: {balance['price']} UZS, Time: {balance['create_data']}")
                count += 1
        if count == 1:
            print("Product not found")
            return False
        return True

    @log_decorator
    def buy_product(self) -> bool:
        try:
            products = list(self.show_product_price())
            for product in self.show_product_price():
                if product is False:
                    print("Something went wrong")
                    return False
                print(product)
            if not products or products[0] is False:
                print("No products available for purchase.")
                return False

            user_balance = self.summ_count()
            if user_balance is False:
                print("Unable to retrieve balance.")
                return False
            print(f"\nYour current balance is {user_balance}\n")
            product_choice = int(input("Enter the number of the product you want to buy: "))
            if product_choice < 1 or user_balance < product_choice:
                print("Invalid product choice.")
                return False

            product_price = self.balance_price(product_choice)
            data_id: int = balance_manager.random_id()
            balance_data = {
                'id': data_id,
                'balance': -product_choice,
                'phone_number': self.active_user['phone_number'],
                'price': product_price,
                'create_data': datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
            }
            if not balance_manager.append_data(data=balance_data):
                print("Failed to update balance. Purchase unsuccessful.")
                return False
            print(f"You bought {product_choice} products for {product_price} UZS")
            print(f"Successfully purchased the product. Your new balance is {self.summ_count()}")
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def profile(self):
        try:
            print(f"Fullname: {self.active_user['full_name']}")
            print(f"Phone number: {self.active_user['phone_number']}")
            print(f"Balance: {self.summ_count()}")
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    @log_decorator
    def offer(self):
        print('To invite a friend, you need to enter their email and enter the verification code sent to them')
        print("For inviting a friend, you will be credited with 5 products")
        all_messages = message_manager.read()
        confirm_code = message_manager.random_id()
        to_email: str = input("Enter your friend's email: ")
        if to_email == self.__admin_email:
            print("This email is already is use")
            return False
        if len(all_messages) != 0:
            for message in all_messages:
                if to_email == message['email']:
                    print("This email is already in use")
                    return False
        if invite_friend(to_email=to_email, code=confirm_code):
            print("Thank you for inviting the friend")
            return True
        print("Sorry, we encountered an error")
        return False

    @log_decorator
    def my_invite(self) -> bool:
        all_invites: list = message_manager.read()
        count = 1
        if len(all_invites) == 0:
            print("No offers found")
            return False
        for invite in all_invites:
            if invite['phone_number'] == self.active_user['phone_number']:
                print(f"{count}. Balance: +5, Email: {invite['email']}, Data: {invite['create_data']}")
                count += 1
        if count == 1:
            print("Your offer is not available")
            return False
        print(f"\nYour offer is available: {(count - 1) * 5}")
        return True
