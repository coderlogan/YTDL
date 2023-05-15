from youtube_search import YoutubeSearch
import yt_dlp

def print_info(z):
    print("Name: " + z['title'])
    print("Uploaded: " + z['publish_time'])
    print("Channel: " + z['channel'])
    print("Duration: " + z['duration'])
    print("ID: " + z['id'])
    print("\n")

x = input("Download or type anything else to search\n")
if x == "Download":
  y = input("ID: ")
  ytdowmload = yt_dlp.YoutubeDL()
  ytdowmload.download("http://youtube.com/watch?v=" + y)
elif x == "SearchChannel":
  c = input("Channel: ")
  n = int(input("How many results: "))
  y = YoutubeSearch(c, n).videos
  r = 0
  for z in y:
    if z['channel'] != c:
      r += 1
  y = YoutubeSearch(c, n + r).videos
  for z in y:
    if z['channel'] != c:
      y.remove(z)
  print("\n")
  for v in y:
    print_info(v)
else:
  y = YoutubeSearch(x, int(input("Number of results: "))).videos
  print("\n")
  for v in y:
    print_info(v)