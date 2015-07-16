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
    for folder_name in range(count):
        os.mkdir(determine_folder(folder_name, count))

    for num, file in enumerate(files):
        print(file, '->',
            shutil.move(file, determine_folder(num, count))
        )

def determine_folder(index, folder_count):
     return str(index % folder_count + 1)

if __name__ == "__main__":
    main()
