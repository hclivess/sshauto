import sys
import os
import subprocess
import json

pathname = os.path.abspath(os.path.dirname(sys.argv[0]))

def load_credentials():
    if os.path.exists("secret.json"):
        cred_file = "secret.json"
    else:
        cred_file = "secret_demo.json"
        
    with open(cred_file) as secret_file:
        credentials = json.loads(secret_file.read())
    return credentials

if __name__ == "__main__":
    creds = load_credentials()
    user = creds["username"]
    password = creds["password"]
    ips = creds["ips"]

    for ip in ips:
        print(f"Working on {ip}")
        command = f"{pathname}\\plink {ip} -l root -pw {password} -m {pathname}\\command.txt"
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
        output = pipe.read().decode()
        pipe.close()
        print(output)