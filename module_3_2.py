# Домашняя работа по уроку "Способы вызова функции"

def send_email(message: str, recipient: str, sender='university.help@gmail.com'):
    if not is_mail_addr(recipient) or not is_mail_addr(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        pass
    elif sender.upper() == recipient.upper():
        print(f'Нельзя отправить письмо самому себе!')
        pass
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        pass
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


def is_mail_addr(string):
    domain_ok: bool = False
    if string.endswith('.com') or string.endswith('.ru') or string.endswith('.net'):
        domain_ok = True
        pass
    if domain_ok and '@' in string:
        return True
    else:
        return False


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
