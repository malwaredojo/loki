import sys

colors = True
machine = sys.platform.lower()
if machine.startswith(('os', 'win', 'darwin', 'ios')):
    colors = False

white = green = red = yellow = blue = end = back = info = que = bad = good = run = res = sarcastic = ''
if colors:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[1;34m'
    end = '\033[0m'
    back = '\033[7;91m'
    info = '\033[1;93m[!]\033[0m'
    que = '\033[1;94m[?]\033[0m'
    bad = '\033[1;91m[-]\033[0m'
    good = '\033[1;32m[+]\033[0m'
    run = '\033[1;97m[*]\033[0m'
    res = '\033[1;92m[✓]\033[0m'
    sarcastic = '\033[1;91m[-_-]\033[0m'
