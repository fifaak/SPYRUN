from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


# Authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
docsfile = "map.html"
docsfile.GetContentFile('map.html', mimetype='text/html')
docsfile.Upload()