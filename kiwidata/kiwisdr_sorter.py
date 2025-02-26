#!/usr/bin/env python3

# This script updates and sorts a list of the KiwiSDRs with the best SNR scored
# and writes to a list usable for a local html page and SuperSDR.

from kiwisdr_stripped import dictlist

# supersdr database
supersdr_file = "/usr/local/src/kiwidata/kiwiservers"
default_freq = "10000.00"

# assigm freq limits (Hz)
freq_range = (10000, 29999999)

listcount = 150
min_snr = 19
mykeys = ("url", "loc")

# pass receivers with a lower limit below our lowest frequency (Hz)
dictlist = list(
    filter(
        lambda site: int(site["bands"].split("-")[0]) < freq_range[0],
        dictlist,
    )
)
# pass receivers with an upper limit above our highest frequency (Hz)
dictlist = list(
    filter(
        lambda site: int(site["bands"].split("-")[1]) > freq_range[1],
        dictlist,
    )
)

# filter the list of dictionaries by snr
dictlist = list(
    filter(lambda site: int(site["snr"][:2].replace(",", "")) > min_snr, dictlist)
)
# exclude sites with no available channels
dictlist = list(
    filter(lambda site: float(site["users"]) < float(site["users_max"]), dictlist)
)

# sort the list of dicts by snr and truncate
dictlist.sort(key=lambda item: item.get("snr"), reverse=True)
dictlist = dictlist[0:listcount]

# generate an SDR list of locations and urls
sdrlist = ([entry.get(item) for item in mykeys] for entry in dictlist)

# build the SuperSDR database
payload_3 = "# KiwiSDR bookmark format is...\n# server port frequency description\n"
for element in sdrlist:
    output = f'"{element[1]}" {element[0]} {default_freq}\n'
    payload_3 += output.replace("http://", "").replace(":", " ")

# Opening a text file in write
# mode using the open() function
with open(supersdr_file, "w") as file:
    file.write(payload_3)
