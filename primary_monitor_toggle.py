#!/usr/bin/env python
# file: primary_monitor_toggle


import re, subprocess


def main():
    xrandr = subprocess.run(['xrandr'],
                        check=True,
                        capture_output=True)

    lines = xrandr.stdout.decode('utf-8').strip().splitlines()
    lines_grepped = []
    devices = []
    make_primary = ""

    for line in lines:
        if re.search(' connected ', line):
            devices.append(line.strip().split()[0])
            lines_grepped.append(line)

    for line in lines_grepped:
        col1 = line.split()[0]
        col3 = line.split()[2]
        if col3 != 'primary':
            make_primary = col1

    print(f"make_primary: {make_primary}")

    subprocess.run(['xrandr', '--output', make_primary, '--primary'])


if __name__ == "__main__":
    main()
