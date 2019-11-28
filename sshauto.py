import subprocess
import json
import argparse
from getpass import getpass as gp
import logging
from logging.handlers import RotatingFileHandler

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
    print(f"Selected configuration file: {args.conf}")

    logger = logging.getLogger('my_logger')
    handler = RotatingFileHandler(f'{args.conf}', maxBytes=2000, backupCount=10)
    logger.addHandler(handler)

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
            print(command)
            print(f"Working on {ip}, {command}")
            command_line = f"plink {ip} -l root -pw {password} -m {command} -batch"
            pipe = subprocess.Popen(
                command_line, shell=True, stdout=subprocess.PIPE
            ).stdout
            output = pipe.read().decode()
            pipe.close()
            logger.warning(output)
