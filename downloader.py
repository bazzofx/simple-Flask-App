from pytube import YouTube, Playlist
import time
import os
#print("Type the URL of the video to download")
#video_link = input("URL:")
def downloadmp3Simple(video_link):
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


def downloadmp3(video_link):
    max_retries = 10
    attempt = 0

    while attempt < max_retries:
        try:
            print(f"Attempt {attempt + 1} of {max_retries} for video: {video_link}")
            video = YouTube(video_link)
            stream = video.streams.filter(only_audio=True).first()
            if not stream:
                print("No audio stream found!")
                return None
            file_name = f"{video.title}.mp3"
            download_folder = ".\downloads"
            file_path = os.path.join(download_folder, file_name)
            stream.download(output_path=download_folder,filename=file_name)
            print(f"Successfully downloaded: {file_path}")
            return file_path
            
        except Exception as e:
            attempt += 1
            print(f"Something went wrong: {e}")

            # Handle specific HTTP error 400 case if necessary
            if "HTTP Error 400" in str(e):
                print("Received HTTP Error 400, retrying...")
            else:
                print("Encountered a different error, retrying...")

            # Sleep for a short time before retrying
            time.sleep(2)

    print("Max retries reached. Download failed.")
    return None


#downloadmp3("https://www.youtube.com/watch?v=99j0zLuNhi8")

# downloadmp3("https://www.youtube.com/watch?v=fBOSYnYAqM0&list=PLpqTN7k_5IA7MVQVzEYarY7fPd_ezSTTR&index=2") #Molejo bugado

def downloadPlaylist(url):
    p = Playlist('https://www.youtube.com/watch?v=mxpeK_fiaSA&list=PLpqTN7k_5IA7MVQVzEYarY7fPd_ezSTTR')

    for url in p.video_urls[:3]:
        print (f"Downloading {url}")
        downloadmp3(url)
        print("------------------")

#downloadPlaylist()
    