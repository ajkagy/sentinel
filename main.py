from bin import sentinel
from lib import config
import time
import datetime

from colorama import init
from termcolor import colored

if __name__ == '__main__':
    init()

    text = colored('Using vivo.conf: {}'.format(config.vivo_conf), 'green')
    print(text)
    
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        text = colored('{} Running sentinel'.format(now), 'green')
        print(text)
        try:
            sentinel.main()
        except Exception as e:
            text = colored('Error: {}'.format(e), 'red')
            print(text)
        time.sleep(60) # Wait for a minute