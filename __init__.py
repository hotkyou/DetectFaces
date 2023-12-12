import os
from DetectFaces.facemesh import *
from DetectFaces.createconfig import *
from DetectFaces.detectfaces import *

CONFIG_FILE = "config.ini"

def loadConfig():
    if not os.path.exists(CONFIG_FILE):
        print("config.ini ファイルが存在しません")
        CreateConfig.createini()

loadConfig()
