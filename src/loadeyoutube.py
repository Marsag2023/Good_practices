from pytube import YouTube
import yt_dlp
ydl_opts = {'format': 'bestvideo+bestaudio/best'}
URLS = ['https://www.youtube.com/watch?v=vmGDlF3u_d4']
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)