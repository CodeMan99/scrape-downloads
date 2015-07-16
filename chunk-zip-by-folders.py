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
    for name in range(count):
        os.makedirs(determine_folder(name, count), exist_ok=True)

    for i, filename in enumerate(files):
        print(filename, '->',
            shutil.move(filename, determine_folder(i, count))
        )

def determine_folder(index, folder_count):
     return str(index % folder_count + 1)

if __name__ == "__main__":
    main()
