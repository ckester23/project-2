"""
John Doe Cheyanne Kester's Flask API.
"""

from flask import Flask
import os
import configparser

app = Flask(__name__)

def parse_config(config_paths):
    # from project-0 hello.py
    #todo read debug and port num
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def find_file(filename):
    path = ".web/pages/"

    cnt = 0

            # to access the files in our directory, use getcwd()
            for file in os.listdir(path):

                # I don't want non-useful files
                if file.endswith(".html") or file.endswith(".css"):

                    # check if the file we have matches the one requested
                    if ("/" + file) == filename:
                        # transmit(STATUS_OK, sock)

                        # now send the file's contents to display
                        opened = open(file, "r")
                        for line in opened.readlines():
                            # transmit(line, sock)
                        opened.close()

                        cnt += 1 # this will help us in the next line

            # if we never found a matching file:       
            if cnt == 0:
                transmit(STATUS_NOT_FOUND, sock)
                transmit("Oops! I could not find that file\n", sock)


@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

if __name__ == "__main__":
    # config = parse_config(["credentials.ini", "default.ini"])
    # #message = config["DEFAULT"]["message"]
    # options = config.configuration()

    # DEBUG = options.DEBUG
    # PORT = options.PORT
    app.run(debug=True, host='0.0.0.0')
