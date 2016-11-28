from datetime import date
import json
import os
import sys


class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


def create_log(dest):
    log_path = os.path.join(dest, "{}.txt".format(date.today().strftime("%m.%d.%y")))

    with open(log_path, "w+") as log_file:
        log_file.seek(0)
        print("Log file successfully created\n")
    return log_path


def load_settings(src):
    with open(src) as settings_file:
        settings = json.load(settings_file)
    return settings


def save_settings(src, settings):
    with open(src, "w") as settings_file:
        json.dump(settings, settings_file)
    return None


def scan_z(src):
    for subdirs, dirs, files in os.walk(src):
        # print("dirs: {}\tsubdirs: {}\tfiles: {}".format(dirs, subdirs, files))
        for file in files:
            # print(os.path.join(subdirs, file))
            path = subdirs.split('Z Drive\\', 2)
            if len(path) > 1:
                print(path[1].split('\\'))
            else:
                print(path)
    return None


def copy_z(files, dest):
    return None



if __name__ == "__main__":
    settings = load_settings("settings.json")
    # sys.stdout = Logger(create_log(settings["logs"]))

    print("Google Drive Backup Initiated - Created by Mike Altreuter")
    print("Today's Date: {}\nLast Ran: {}\n".format(date.today().strftime("%m/%d/%y"), "Never"))

    scan_z(settings["source"])
