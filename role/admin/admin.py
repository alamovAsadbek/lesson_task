from datetime import datetime

from main_files.decorator_func import log_decorator


class Admin:
    def __init__(self):
        self.create_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()

    @log_decorator
    def pricing(self):
        try:
            beginning: int = int(input("The beginning: "))
            ending: int = int(input("The ending: "))
        except KeyError:
            print("Error")
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False
