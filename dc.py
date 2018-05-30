import shutil
import logging
from hurry.filesize import size
import os
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)



def main():
    free_space_minimum = 54163204864

    for folder in os.listdir("//Volumes"):
        drive_stats("//Volumes//" + folder, free_space_minimum)


def drive_stats(drive_to_check, free_space_minimum):

    print("\nSize Specs for drive: " + drive_to_check)
    total, used, free = shutil.disk_usage(drive_to_check)
    print("Total: " + size(total))
    print("Used: " + size(used))
    print("Free: " + size(free))

    assert free >= free_space_minimum, "Free space is very low on drive: " + drive_to_check



if __name__ == "__main__":
    main()