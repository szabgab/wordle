import requests
from bs4 import BeautifulSoup
import re


def main():
    error = 0
    with open('README.md') as fh:
        for row in fh:
            match = re.search(r'\(([^\)]*)\)', row)
            if match:
                url = match.group(1)
                print(url)
                headers = {
                    'User-Agent': 'Wordle checker https://wordle.szabgab.com/',
                }
                rv = requests.get(url, headers=headers)

                if rv.status_code == 200:
                    dom = BeautifulSoup(rv.content,  'html.parser')
                    print(dom.title)
                else:
                    print(f"ERROR: {url}  {rv.status_code}")
                    error += 1
                print()
    exit(error)

main()

