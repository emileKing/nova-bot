from flask import Flask
from flask_cors import CORS

from managers.models import ModelManager
from managers.apps import AppManager
from managers.chat import ChatManager


app = Flask(__name__)
cors = CORS(app)

model_mgr = ModelManager("model", create_on_404=True)
app_mgr = AppManager()
chat_mgr = ChatManager(model_mgr, app_mgr)

from api.routes import *