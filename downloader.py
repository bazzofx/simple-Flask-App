from pytube import YouTube

#print("Type the URL of the video to download")
#video_link = input("URL:")
def downloadmp3(video_link):
    try:
        # video_link = "https://www.youtube.com/watch?v=99j0zLuNhi8"

        video = YouTube(video_link)
        stream = video.streams.filter(only_audio=True).first()
        print(stream)
        file = stream.download(filename=f"{video.title}.mp3")
        print(f"Downloading:{video_link}")
        return file
        
    except Exception as e:
        print(f"Something went wrong: {e}") 

downloadmp3("https://www.youtube.com/watch?v=99j0zLuNhi8")

def test(test):
    print(test)

test("Fantastic")