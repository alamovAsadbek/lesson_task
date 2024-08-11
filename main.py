from main_files.auth import Auth
from main_files.decorator_func import log_decorator
from role.admin.admin import Admin
from role.user.user import User


@log_decorator
def show_auth():
    text = '''
1. Register
2. Login
3. Quit
    '''
    print(text)
    try:
        choose_menu = int(input("Choose menu number: "))
        if choose_menu == 1:
            auth.register()
            show_auth()
        elif choose_menu == 2:
            login = auth.login()
            if login is None:
                print("Login Failed")
                show_auth()
            elif not login['is_login']:
                show_auth()
            elif login['role'] == 'admin':
                show_admin_menu()
            elif login['role'] == 'user':
                show_user_menu()
            else:
                print("Something went wrong")
                show_auth()
        elif choose_menu == 3:
            print("Good bye!")
            auth.logout()
            return
        else:
            print("Wrong menu number")
            show_auth()
    except ValueError:
        print("Wrong menu number")
        show_auth()
    except Exception as e:
        print(f'Error: {e}')
        show_auth()


@log_decorator
def show_user_menu():
    text = '''
1. Add product to balance
2. History balance
3. History product
4. Buy product
5. Invite friend
6. Profile
7. Logout
    '''
    print(text)
    try:
        user_menu = int(input("Choose menu number: "))
        user = User()
        if user_menu == 1:
            user.add_balance()
            show_user_menu()
        elif user_menu == 2:
            user.history_balance()
            show_user_menu()
        elif user_menu == 3:
            user.history_product()
            show_user_menu()
        elif user_menu == 4:
            user.buy_product()
            show_user_menu()
        elif user_menu == 5:
            invite_menu()
        elif user_menu == 6:
            user.profile()
            show_user_menu()
        elif user_menu == 7:
            auth.logout()
            print("Logout Successful")
            show_auth()
        else:
            print("Wrong menu number")
            show_user_menu()
    except ValueError:
        print("Wrong menu number")
        show_user_menu()


@log_decorator
def show_admin_menu():
    text = '''
1. Pricing
2. Show sold
3. Show all users
4. Logout
    '''
    print(text)
    try:
        admin = Admin()
        user_menu = int(input("Choose menu number: "))
        if user_menu == 1:
            admin.pricing()
            show_admin_menu()
        elif user_menu == 2:
            admin.show_sold()
            show_admin_menu()
        elif user_menu == 3:
            admin.show_all_users()
            show_admin_menu()
        elif user_menu == 4:
            auth.logout()
            print("Logout Successful")
            show_auth()
        else:
            print("Wrong menu number")
            show_admin_menu()
    except ValueError:
        print("Wrong menu number")
        show_admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_admin_menu()


@log_decorator
def invite_menu():
    text = '''
1. My invites
2. Invite friend
3. Back
    '''
    print(text)
    try:
        user = User()
        user_menu = int(input("Choose menu number: "))
        if user_menu == 1:
            user.my_invite()
            invite_menu()
        elif user_menu == 2:
            user.offer()
            invite_menu()
        elif user_menu == 3:
            show_user_menu()
        else:
            print("Wrong menu number")
            invite_menu()
    except ValueError:
        print("Wrong menu number")
        invite_menu()
    except Exception as e:
        print(f'Error: {e}')
        invite_menu()


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    show_auth()

