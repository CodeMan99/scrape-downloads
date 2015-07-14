#!/usr/bin/env python3

import os
import sys

def main():
    template = ''
    with open('curl-template.sh', 'r') as curl_in:
        template = curl_in.read().strip()

    with open('download.sh', 'w') as download:
        print('#!/bin/bash', file=download)

        for href in sys.stdin:
            href = href.strip()
            print(
                template.format(
                    href=href,
                    filename="--".join(
                        href.split('/')[-2:]
                    )
                ),
                file=download
            )

    os.chmod('download.sh', 0o0700)

if __name__ == "__main__":
    main()
