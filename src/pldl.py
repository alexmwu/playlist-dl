from __future__ import unicode_literals
import youtube_dl
import requests
import sys

class PldlLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def pldl_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

# list of urls
def download(urls):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def get_yt():
    pass

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': PldlLogger(),
    'progress_hooks': [pldl_hook],
}

def usage():
    print 'usage: playlist-dl inputfile'

def main():
    infile = ''
    if len(sys.argv) == 2:
        infile = sys.argv[1]
    else:
        usage()
        return 1


if __name__ == '__main__':
    main()
