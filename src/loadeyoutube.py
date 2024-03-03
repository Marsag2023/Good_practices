from pytube import YouTube
import yt_dlp
#ydl_opts = {'format': 'bestvideo+bestaudio/best'}
# ydl_opts = {'format': MP4}
# URLS = ['https://www.youtube.com/watch?v=VIDEO_ID']
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(URLS)
#
#yt = YouTube('https://www.youtube.com/watch?v=VIDEO_ID') #ссылка на видео.
# yt.stream показывает какое видео ты можешь скачать
# (mp4(720) + audio или только mp4(1080) без звука).
# Сейчас стоит фильтр по mp4.
# i = 0
# for i in range(len(yt.streams.filter(file_extension='mp4'))):
#     print(yt.streams.filter(file_extension='mp4')[i])
#
# stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
# stream.download() #загружаем видео.


# Вставьте ссылку на видео с YouTube
video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'

yt = YouTube(video_url)
video = yt.streams.get_highest_resolution()

# Скачивание видео
video.download('путь_для_сохранения')

print('Видео успешно скачано!')