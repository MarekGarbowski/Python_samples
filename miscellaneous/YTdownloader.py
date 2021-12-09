from pytube import YouTube


link = input('Enter youtube url: ')
yt = YouTube(link)
videos = yt.streams
video = list(enumerate(videos))

for movie in video:
    print(movie)

print("Enter the number of video to download")
dn_option = int(input('Choose option: '))
dn_video = videos[dn_option]
dn_video.download()

print('Downloaded finished')
