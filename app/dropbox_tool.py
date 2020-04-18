import datetime as dt
import os
from dotenv import load_dotenv
import pyautogui
import dropbox

load_dotenv()

token_dropbox = os.environ.get('token')
dbx = dropbox.Dropbox(token_dropbox)


def take_screenshot():
    screen = pyautogui.screenshot()
    date = str(dt.datetime.now().date()) + str(dt.datetime.now().time()).replace(".", ":").replace(":", "-")
    file_path = "D:/Univer/4 курс/Распределенные/screenshots/screens/{}.png".format(date)
    screen.save(file_path)
    to_dropbox(file_path, date)


def to_dropbox(file_path, date):
    with open(file_path, 'rb') as file:  # открываем файл в режиме чтение побайтово
        # загружаем файл: первый аргумент (file.read()) - какой файл;
        # второй - название, которое будет присвоено файлу уже на дропбоксе
        response = dbx.files_upload(file.read(), "/" + date + ".png")
        print(response)  # выводим результат загрузки
