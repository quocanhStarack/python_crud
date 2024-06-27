from typing import override
import pyrebase
from config.firebase_config import FirebaseConfig
from uploader.uploader import AbstractUploader
from firebase_admin import storage


class FirebaseUploader:

    def __init__(self,config):
        self.firebase = pyrebase.initialize_app(config=config)

    def uploadFile(self, path:str):
        storage = self.firebase.storage()
        store = storage.child(f'images/{path}').put(path)
        return storage.child(f'images/{path}').get_url(None)
       
        