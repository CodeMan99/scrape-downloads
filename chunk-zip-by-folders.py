#!/usr/bin/env python3

import math
import os
import shutil

def main():
    files = sorted(
        filter(os.path.isfile, os.listdir('.')),
        key=os.path.getsize
    )

    count = math.ceil(len(files) / 30)
    for folder_name in range(1, count + 1):
        os.mkdir(str(folder_name))

    for num, file in enumerate(files):
        print(file, '->',
            shutil.move(file, str(num % count + 1))
        )

if __name__ == "__main__":
    main()
