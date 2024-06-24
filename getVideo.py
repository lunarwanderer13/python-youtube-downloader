try:
    from pytube import YouTube
    from colored import fg, attr
except ModuleNotFoundError as err:
    print(f'{fg(1)}ModuleNotFoundError: {err}{attr(0)}')

def getVideo(videoUrl, downloadPath) -> None:
    try:
        # Create a YouTube object
        yt = YouTube(videoUrl)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f'{fg(69)}Downloading {fg(46)}{yt.title}{fg(69)}...{attr(0)}')
        stream.download(downloadPath)
        print(f'{fg(69)}Downloaded {fg(46)}{yt.title}{fg(69)} successfully!{attr(0)}')
    except Exception as err:
        print(f'{fg(1)}An error occurred: {err}{attr(0)}')

if __name__ == '__main__':
    while True:
        # URL of the video you want to download
        videoUrl = input(f'{fg(15)}Enter the YouTube video URL: {attr(0)}')
        # Path where you want to save the video
        downloadPath = 'vids' #input(f'{fg(15)}Enter the download path:  {attr(0)}')

        getVideo(videoUrl, downloadPath)