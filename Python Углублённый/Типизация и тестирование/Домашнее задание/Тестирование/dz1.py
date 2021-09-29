import sqlite3
import smtplib
from datetime import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest import TestCase
from unittest.mock import patch, MagicMock


class Person:
    def __init__(self, full_name, short_name, birthday, email):
        self.full_name = full_name
        self.short_name = short_name
        self.birthday = birthday
        self.email = email

    def get_full_name(self):
        sql = "SELECT * FROM employees WHERE full_name = ?"
        result = cursor.execute(sql, [self.full_name])

        row = result.fetchone()
        user_full_name = row[0]

        print(user_full_name)

    def get_short_name(self):
        sql = "SELECT * FROM employees WHERE short_name = ?"
        result = cursor.execute(sql, [self.short_name])

        row = result.fetchone()
        user_short_name = row[1]

        print(user_short_name)

    def get_age(self):
        sql = "SELECT * FROM employees WHERE birthday = ?"
        result = cursor.execute(sql, [self.birthday])

        row = result.fetchone()
        user_birthday = row[2]

        user_birthday_date = datetime.strptime(user_birthday, "%Y-%m-%d")
        today = datetime.today()

        print(today.year - user_birthday_date.year - (
                (today.month, today.day) < (user_birthday_date.month, user_birthday_date.day)), "лет")

    def __str__(self):
        sql = "SELECT * FROM employees WHERE full_name = ?"
        result = cursor.execute(sql, [self.full_name])

        print(result.fetchall())


conn = sqlite3.connect("persons.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE employees 
(full_name text, short_name text, birthday text, email text)""")

conn.commit()


def send_email(some_person):
    address_from = some_person.email
    address_to = ""  # тут нужно указать свой почтовый адрес (отправка сообщений настроена на Gmail)
    password = ""  # тут нужно указать пароль от своего почтового ящика

    msg = MIMEMultipart()
    msg['From'] = address_from
    msg['To'] = address_to
    msg['Subject'] = "Thanks"

    sentence = ["Thank you for registration,", some_person.short_name]

    body = ' '.join(sentence)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(True)
    server.starttls()
    server.login(address_to, password)
    server.send_message(msg)
    server.quit()


def registration(new_person):
    cursor.execute("""INSERT INTO employees VALUES 
    ('{}', '{}', '{}', '{}')""".format(new_person.full_name, new_person.short_name, new_person.birthday, new_person.email))

    conn.commit()

    send_email(new_person)


def info(some_info):
    sql = "SELECT * FROM employees WHERE full_name LIKE '%" + some_info + "%' OR email = ?"
    result = cursor.execute(sql, [some_info])
    row = result.fetchone()
    data_list = []
    error = ""

    try:
        data_list = [row[0], row[1], row[2], row[3]]
    except TypeError:
        error = "Error"

    if len(data_list) == 0:
        search_result = error + "! No one found"
    else:
        search_result = "Full name: {}, short name: {}, birthday: {}, email: {}".format(row[0], row[1], row[2], row[3])
    return search_result


person1 = Person("Тесленко Никита Алексеевич", "Тесленко Н.О.", "2001-08-20", "nikitateslenko762@gmail.com")
person2 = Person("Петров Игорь Сергеевич", "Петров И.С.", "2000-01-01", "igorpetrov763@gmail.com")

registration(person1)
registration(person2)

print(info("Игорь"))
print(info("Тесленко"))
print(info("Петров"))
print(info("Никита"))
print(info("igorpetrov763@gmail.com"))
print(info("Валерий"))


class SendEmailTest(TestCase):
    @patch("dz1.send_email", return_value=None)
    def test_function(self, mocked_send_email: MagicMock):
        person = Person("Тесленко Никита Алексеевич", "Тесленко Н.О.", "2001-08-20", "nikitateslenko762@gmail.com")
        registration(person)

        self.assertEqual(1, mocked_send_email.call_count)
        mocked_send_email.assert_called_once_with(person)


# после проверки очистить файлы вручную или закомментировать 129-136 строки и расскоментировать 140 строку
# open("persons.db", 'w').close()
