import pytube
from pytube import YouTube

def download_youtube(*args):  # Скачивания youtube # https://pytube.io/en/latest/user/streams.html
    video_link = args[0]
    if not video_link:
        video_link = input('Кидай ссыль\n')
    yt = pytube.YouTube(video_link)
    i_tag = int(input('Выбери тип загрузки:\n22 - 720p / 137 - 1080p\n140 - звук / 251 - странный звук\n'))
    stream = yt.streams.get_by_itag(i_tag)
    stream.download()  # надо выяснить что это и можно ли через ссыль как-то
    '''
    кста, мб есть апи на ютуб и тогда ниче качать не надо будет и можно будет загрузить ссылку на видео
    мб даже пролсто как-то .answer_video(file = link)
    тогда мб сделать allsaverbot и дальше уже докручивать и тик токи и рутубы и прочие приколюхи))
    '''


if __name__ == '__main__':
    print('Поехали')
    video_link = 'https://www.youtube.com/watch?v=vt14fmyyDiE&ab_channel=%D0%9A%D1%80%D0%B5%D0%BC%D0%BD%D0%B8%D0%B5%D0%B2%D0%B0%D1%8F%D0%B4%D0%BE%D0%BB%D0%B8%D0%BD%D0%B0%D0%9A%D1%80%D1%83%D0%B6%D0%BE%D0%BA%D0%B2%D0%BA%D1%80%D1%83%D0%B3%D0%B5'
    yt = pytube.YouTube(video_link)
    i_tag = 22
    stream = yt.streams.get_by_itag(i_tag)
    file_link = stream.url
    print('Готовимся)')
    stream.download()
    print('Приехали)')
