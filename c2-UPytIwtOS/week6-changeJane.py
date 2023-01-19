#!/usr/bin/env python3

import sys
import subprocess

old_file = sys.argv[1]
with open(old_file, "r") as file:
    for line in file.readlines():
        old_str = line.strip()
        new_str = old_str.replace("jane", "jdoe")
        subprocess.run(["mv", old_str, new_str])
    file.close()

