from flask import Flask

from SalesControl.ext import dao
from SalesControl.ext import config

app = Flask(__name__)

dao.init_app(app)
config.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
