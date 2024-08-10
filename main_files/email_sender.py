import contextlib
import smtplib
import threading
from datetime import datetime

from main_files.decorator_func import log_decorator
from main_files.json_manager import user_manager, message_manager

active_user = user_manager.get_active_user()
from_email = "alamovasad@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_password = "ewid hqql wswp gckm"


# context manager
@contextlib.contextmanager
def login_email():
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, smtp_password)
    yield server
    server.quit()


@log_decorator
def send_email(to_mail, email):
    with login_email() as server:
        server.sendmail(from_email, to_mail, email)


@log_decorator
def invite_friend(to_email: str, code: int) -> bool:
    subject: str = "Invite friend"
    body: str = (f"Hello, your friend invited you to the {active_user['full_name']} water program. "
                 f"You must tell your friend the code to accept the offer. Your code is {code}")
    email = f'Subject: {subject}\n\n{body}'
    try:
        threading.Thread(target=send_email, args=(to_email, email)).start()
        count = 1
        while count <= 3:
            confirm_code: int = int(input("You will be given 3 chances to enter the code sent to your friend: "))
            if confirm_code == code:
                break
            print("Wrong code. Please try again.")
            count += 1

        if count == 4:
            return False
        message_data = {
            'id': code,
            'phone_number': active_user['phone_number'],
            'email': to_email,
            'create_data': datetime.now().strftime("%d/%m/%Y %H:%M:%S").__str__()
        }
        if message_manager.append_data(data=message_data):
            return True
        return False
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False
