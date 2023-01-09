
# если не работает, то:  pip install pytube
# $ cd pytube
# $ python -m pip install .

import os
import shutil

import instaloader

import pytube
from pytube import YouTube

from fnmatch import fnmatch


def dowload_inst_stories():  # Скачивания Историй
    USER = ''
    PASSWORD = ''
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    # for story in L.get_stories():
    #     for item in story.get_items():
    #         L.download_storyitem(item, ':stories')

    # Выберем группу для загрузки сторис
    profile = input('Откуда качаем сторисы?))\n1 - muzlo, 2 - vsbattle\nвведи 1 или 2\nНу или свой вариант\n')

    muzlo_gang = 2990056938
    vsbattle_videos = 2295943926

    if profile == 1:
        profile = muzlo_gang
    elif profile == 2:
        profile = vsbattle_videos
    else:
        profile = L.check_profile_id(profile)  # muzlo_gang ^ 2990056938 / vsbattle_videos ^ 2295943926
        print(profile)
    # You can pass multiple ids like [460563723, 460563723, 460563723]
    L.download_stories(userids=[profile])


def delete_inst_stories():  # Удаление старых Сторис
    katalog = "：stories"
    dirname = os.path.dirname(__file__)  # Текущая директория
    filename = os.path.join(dirname, katalog)  # C:\Users\qwera\PycharmProjects\downloader\：stories
    if os.path.exists(filename):
        print("начинается удаление")
        shutil.rmtree(filename)
    else:
        print("Директории нет")


def dowload_youtube(*args):  # Скачивания youtube # https://pytube.io/en/latest/user/streams.html
    video_link = args[0]
    if not video_link:
        video_link = input('Кидай ссыль\n')
    yt = pytube.YouTube(video_link)
    itag = int(input('Выбери тип загрузки:\n22 - 720p / 137 - 1080p\n140 - звук / 251 - странный звук\n'))
    stream = yt.streams.get_by_itag(itag)
    stream.download()


def send_file(filename):
    pass


def send_telegram():
    katalog = "：stories"  # название папки, где лежат сторисы
    pattern = "*.mp4"  # формат файлов для отправки в телегу
    dirname = os.path.dirname(__file__)  # Текущая директория
    filename = os.path.join(dirname, katalog)
    for path, subdirectories, files in os.walk(filename):
        for name in files:
            if fnmatch(name, pattern):
                send_file(filename)


def dowload_choice():
    place = input('Откуда скачиваем?\ny = youtube, i = inst\n')
    if place == 'y' or place == 'youtube':
        dowload_youtube()
    elif place == 'i' or place == 'inst' or place == 'instagram':
        dowload_inst_stories()
    elif place.find('youtube'):
        dowload_youtube(place)
    else:
        print("Отсюда не качаем, напиши на почту: sladovir@mail.ru")

    if input('Загрузить в телегу? (y = yes)\n') == 'y':
        send_telegram()


if __name__ == '__main__':
    dowload_choice()
    # сначала узнать откуда качать
    # что куда
    # грузить?







    '''
     Такс я не понимаю почему у меня сломалост удаление папки, теперь пишет, мол, использование функции rmtree не безопасно
     Канеш, можно без удаления и привязать чекалку имени у файлов, например, если файл загружен сегодня, то это новый файл,
     и его нужно юудет загрузить в телегу, мб можно будет добавить, чтобы отправленные сторичы убирались в другу. папку, 
     А еще можно прикрутить сюда отложенную отправку сторис в телегу(но для этого надо разобраться с телегой)

     Итак, наверно пока что не следует уделять внимание штучкам связанным с хардкодом и лучше уделить внимание изучению 
     новых функций
    '''
    '''
    ояень круто, я сейчас решмл попробовать скачать чторисы не удаляя старую папку и оказывается эта штука сама удалит 
    старую папку и начнет закачивать заного, хотя это мб, только если менять группу, но будет классно, если будет рвботвть 
    без замены группы
    '''
    '''
    чет старые файлы не удаляет прога автоматом.... чет ъуйня какая-то
    '''

    '''
    скачать с youtube
    https://pytube.io/en/latest/user/streams.html

    video_link = "https://www.youtube.com/watch?v=2IGwkJDcIk8&list=RDW_NnpQ36ZRo&index=11"
    yt = pytube.YouTube(video_link)
    stream = yt.streams.get_by_itag(22) #22 - качество??   251 - звук   137-1080p
    stream.download()
    '''

