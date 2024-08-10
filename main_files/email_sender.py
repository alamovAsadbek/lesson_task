from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager


class EmailSender:
    def __init__(self):
        self.active_user = user_manager.get_active_user()
        self.from_email = "alamovasad@gmail.com"
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.password = "ewid hqql wswp gckm"

    # context manager
    @log_decorator
    def login_email(self):
        pass
