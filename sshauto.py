import sys
import os
import subprocess
import json

pathname = os.path.abspath(os.path.dirname(sys.argv[0]))

def load_data():
    if os.path.exists("secret.json"):
        data_file = "secret.json"
    else:
        data_file = "secret_demo.json"
        
    with open(data_file) as secret_file:
        data = json.loads(secret_file.read())
    return data

if __name__ == "__main__":
    d = load_data()

    for entry in d:

        user = entry["username"]
        password = entry["password"]
        ip = entry["ip"]
        commands = entry["commands"]

        for command in commands:
            print(command)
            print(f"Working on {ip}, {command}")
            command_line = f"{pathname}\\plink {ip} -l root -pw {password} -m {pathname}\\{command}"
            pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
            output = pipe.read().decode()
            pipe.close()
            print(output)