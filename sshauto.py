import subprocess
import json
import argparse
from getpass import getpass as gp
import logging.handlers


def load_data(file="demo.json"):

    data_file = file
    with open(data_file) as config_file:
        data = json.loads(config_file.read())
    return data


if __name__ == "__main__":
    password = None
    parser = argparse.ArgumentParser()


    parser.add_argument("--conf", help="Server configuration file")
    args = parser.parse_args()

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)
    fileHandler = logging.FileHandler(f"log.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    d = load_data(args.conf)

    askonce_entered = False
    for entry in d:

        user = entry["username"]

        if not askonce_entered:

            password = entry["password"]

            if password == "askonce":
                password = gp("Enter your password: ")
                askonce_entered = True

            elif password == "ask":
                password = gp("Enter your password: ")

        ip = entry["ip"]
        commands = entry["scripts"]

        for command in commands:

            try:
                rootLogger.info(command)
                rootLogger.info(f"Working on {ip}, {command}")
                command_line = f"plink {ip} -l {user} -pw {password} -m {command} -batch"
                pipe = subprocess.Popen(
                    command_line, shell=True, stdout=subprocess.PIPE
                ).stdout
                output = pipe.read().decode()
                pipe.close()
                rootLogger.info(output)

            except Exception as e:
                rootLogger.info(f"Error: {e}")
