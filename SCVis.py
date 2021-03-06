
#import scipy.io.wavfile, numpy, sys, subprocess
import soundcloud
#import urllib.request
import youtube_dl
import os
import traceback

# def make_savepath(title, savedir):
#     return os.path.join(savedir, "%s.mp3" % (title))

def main(url):
    # create directory
    savedir = "directory"
    if not os.path.exists(savedir):
        os.makedirs(savedir)



    options = {
        'format':'bestaudio/best',
        'extractaudio': True,
        'audioformat': "mp3",
        'outtmpl': '%(id)s',
        'noplaylist': True,}
    ydl = youtube_dl.YoutubeDL(options)

    with ydl:

            ydl.download([url])

            savedir = '/Downloads/'

            print("Downloading...")

            # download video
            try:
                result = ydl.extract_info(url, download=True)

                # for i in result :
                #     print(i)

                #filename = make_savepath(result['title'], savedir)

                #filename =  result['title'] + ".mp3"

                filename = "TEMPSONG.mp3"

                os.rename(result['id'], filename)
                print("Downloaded and converted successfully!")

            except Exception as e:
                print("Can't download audio! %s\n" % traceback.format_exc())
