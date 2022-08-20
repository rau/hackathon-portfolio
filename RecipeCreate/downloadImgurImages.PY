import imguralbum
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
def downloadImages(imgurLink):
    downloader = imguralbum.ImgurAlbumDownloader(imgurLink)
    print("This albums has %d images" % downloader.num_images())
    downloader.save_images()
    
    return(imgurLink[imgurLink.rfind('/'):].replace('/', ''))
