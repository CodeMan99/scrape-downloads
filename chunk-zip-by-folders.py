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
    if count <= 1:
        raise RuntimeError('There are already less than 30 files in current folder.')

    for name in range(count):
        os.makedirs(determine_folder(name, count), exist_ok=True)

    for i, filename in enumerate(files):
        print(i + 1, filename, '->',
            shutil.move(filename, determine_folder(i, count))
        )

def determine_folder(index, folder_count):
     return str(index % folder_count + 1)

if __name__ == "__main__":
    main()
