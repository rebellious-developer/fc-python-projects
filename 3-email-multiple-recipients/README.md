# Instructions
Prior to running this script please do the following:

1. Install `aiosmtpd` via PIP (if not already installed)
```Bash
pip install aiosmtpd
```

2. Start the process in a new terminal window via:
```Bash
python3 -m aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:1025
```

Feel free to background process it via & if you prefer less terminals.

After running the script you can then see what is being sent to the SMTP server in that terminal winow.