from pytube import YouTube

link = input("Enter link of youtube video: ")
yt = YouTube(link)

#Print the title of the video
print("Title: ", yt.title)

#Print the number of views of the video
print("Views: ", yt.views)

#Print the length of the video
print("Duration: ", yt.length)

#Print the description of the video
keywords = yt.keywords
print("Description: ", yt.streams.desc())

#To get ratings of the video
print("Ratings: ", yt.rating)

#Download the video
# stream = yt.streams.get_lowest_resolution()
# stream.download()
# print("Download completed!!!")

print(yt.streams)