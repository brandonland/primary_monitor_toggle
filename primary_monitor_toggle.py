#!/usr/bin/env python
# file: primary_monitor_toggle

import re, subprocess

def main():
    ps = subprocess.run(['xrandr'],
                        check=True,
                        capture_output=True)

    output = subprocess.run(['grep', ' connected '],
                            input=ps.stdout,
                            capture_output=True)

    devices = []
    make_primary = ""

    lines = output.stdout.decode('utf-8').strip().splitlines()
    if len(lines) != 2:
        exit("You do not have two monitors.")

    for line in lines:
        device_id = line.split()[0]
        devices.append(device_id) 
        
    for monitor in devices:
        ps = subprocess.run(['xrandr', '--listmonitors'],
                            check=True,
                            capture_output=True)

        output = subprocess.run(['grep', monitor],
                                input=ps.stdout,
                                capture_output=True)

        columns = output.stdout.decode('utf8').strip().split()
        column_primary = columns[1]
        if "*" not in column_primary:
            make_primary = monitor

    subprocess.run(['xrandr', '--output', make_primary, '--primary'])



if __name__ == "__main__":
    main()
