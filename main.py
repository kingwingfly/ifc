from flask import Flask, render_template, redirect, send_from_directory

IMAGES_DIR = "./images"

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("./index.html")


@app.get("/models/<string:model_name>")
def model(model_name):
    model_dir = "./models"
    return send_from_directory(directory=model_dir, path=f"{model_name}")


@app.get("/worker/<string:file_name>")
def worker(file_name):
    file_dir = "./static/js/worker"
    return send_from_directory(directory=file_dir, path=f"{file_name}")


@app.get("/wasm/<string:file_name>")
def wasm(file_name):
    file_dir = "./static/js/wasm"
    return send_from_directory(directory=file_dir, path=f"{file_name}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848, debug=True)
