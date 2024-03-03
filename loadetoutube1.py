#Извините за недопонимание. Вот пример простой программы на Python, которая использует API YouTube для скачивания видео.

#```python
from googleapiclient.discovery import build
import pafy

# Получение API ключа с https://console.cloud.google.com/
api_key = "YOUR_API_KEY"

# Создание объекта YouTube Data API
youtube = build('youtube', 'v3', developerKey=api_key)

# Запрос на поиск видео
search_response = youtube.search().list(
    q='Котики',
    part='id,snippet',
    maxResults=1
).execute()

# Получение ID первого найденного видео
video_id = search_response['items'][0]['id']['videoId']

# Получение ссылки на видео по его ID и скачивание видео
video = pafy.new('https://www.youtube.com/watch?v=' + video_id)
bestaudio = video.getbestaudio()

bestaudio.download()
#```