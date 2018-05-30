import shutil
import logging
from hurry.filesize import size
import os
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)



def main():
    for folder in os.listdir("//Volumes"):
        drive_stats("//Volumes//" + folder)


def drive_stats(drive_to_check):

    print("\nSize Specs for drive: " + drive_to_check)
    total, used, free = shutil.disk_usage(drive_to_check)
    print("Total: " + size(total))
    print("Used: " + size(used))
    print("Free: " + size(free))


if __name__ == "__main__":
    main()