#!/usr/bin/env python3

import os
import sys

def main():
    last_page = int(sys.argv[1])

    template = ''
    with open('curl-template.sh', 'r') as curl_template:
        template = curl_template.read().strip()

    with open('get-pages.sh', 'w') as get_pages:
        print('#!/bin/bash', file=get_pages)

        for page in range(1, last_page + 1):
            print(template.format(
                href="/practice/files/p/{}/".format(page),
                filename="page{}.html".format(page)
            ), file=get_pages)

    os.chmod('get-pages.sh', 0o755)

if __name__ == "__main__":
    main()
