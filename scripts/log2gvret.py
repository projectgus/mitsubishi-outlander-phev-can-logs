#!/usr/bin/env python
import csv
import sys
import os
import os.path
import re

def main(from_path, to_path):
    if os.path.realpath(from_path) == os.path.realpath(to_path):
        raise RuntimeError(f"from and to are the same file: {from_path}")
    with open(from_path, "r") as fr:
        with open(to_path, "w", newline='') as to:
            writer = csv.writer(to)
            writer.writerow(['Time Stamp','ID','Extended','Bus','LEN','D1','D2','D3','D4','D5','D6','D7','D8'])
            for line in fr:
                m = re.match(r'Timestamp: *([\d\.]+) *ID: ([\da-f]+) *([S]) Rx *DLC: *(\d+) *([\da-f ]{23}) *Channel: (\d)', line)
                if m:
                    timestamp, canid, idtype, dlc, data, channel = m.groups()
                    # currently canalystii python-can returns units of 100us
                    timestamp = int(float(timestamp)) * 100
                    dbytes = data.upper().split(" ")
                    assert len(dbytes) == 8
                    extended = idtype != 'S'  # bit hacky
                    canid = int(canid, 16)

                    writer.writerow([timestamp,
                                     f'{canid:08X}',
                                     str(extended).lower(),
                                     channel,
                                     dlc] + dbytes)


if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        main(sys.argv[1], os.path.splitext(sys.argv[1])[0] + '.csv')
