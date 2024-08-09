from main_files.auth import Auth
from main_files.decorator_func import log_decorator


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
                pass
            elif login['role'] == 'user':
                pass
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
    '''
    print(text)
    try:
        user_menu = int(input("Choose menu number: "))
        if user_menu == 1:
            pass
        elif user_menu == 2:
            pass
        elif user_menu == 3:
            pass
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
    '''
    print(text)
    try:
        user_menu = int(input("Choose menu number: "))
        if user_menu == 1:
            pass
        elif user_menu == 2:
            pass
        elif user_menu == 3:
            pass
        else:
            print("Wrong menu number")
            show_admin_menu()
    except ValueError:
        print("Wrong menu number")
        show_admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        show_admin_menu()


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    show_auth()
