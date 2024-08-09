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


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
    show_auth()

