import pytube

link = input("Cole o url do video aqui: ")

youtube = pytube.YouTube(link)
youtube.streams.filter(progressive=True, file_extension='mp3').first().download()
print("Downloaded", link)
