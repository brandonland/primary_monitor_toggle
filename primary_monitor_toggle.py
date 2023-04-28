#!/usr/bin/env python
# file: primary_monitor_toggle


import re, subprocess


def main():
    xrandr = subprocess.run(['xrandr'], capture_output=True)

    lines = xrandr.stdout.decode('utf-8').strip().splitlines()
    lines_grepped = []
    make_primary = ""

    for line in lines:
        if re.search(' connected ', line):
            lines_grepped.append(line)

    for line in lines_grepped:
        col1 = line.split()[0]
        col3 = line.split()[2]
        if col3 != 'primary':
            make_primary = col1

    subprocess.run(['xrandr', '--output', make_primary, '--primary'])

if __name__ == "__main__":
    main()
