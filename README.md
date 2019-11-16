# sshauto
Automate SSH connections, send bulk commands to multiple servers without having to log in to them individually.

Create `secret.json` from `secret_demo.json` and adjust settings.
If you don't want to store plaintext passwords, enter `"ask"` as your password to be asked during the procedure.

For linux, you need to `apt-get install plink`. For windows, you need the bundled `plink.exe`

To run, `python3.7 sshauto.py` or `python3 sshauto.py` or `python sshauto.py`, depending on your local configuration. In Windows, you run `sshauto.py` in your favorite IDE or the command line Python.

Supports unlimited number of servers and unlimited number of command files per server, as in `["nyzo.txt", "bismuth.txt"]`.

![alt text](thumb.png)

