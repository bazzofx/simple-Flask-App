from pytube import YouTube
#print("Type the URL of the video to download")
#video_link = input("URL:")
try:
    video_link = "https://www.youtube.com/watch?v=99j0zLuNhi8"
    video = YouTube(video_link)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f"{video.title}.mp3")
except KeyError:
    print("Something went wrong")



