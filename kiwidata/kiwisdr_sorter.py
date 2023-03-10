#!/usr/bin/env python3

# Copyright (c) 2023 by Philip Collier, github.com/AB9IL
# This script is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version. There is NO warranty; not even for
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# This script updates and sorts a list of the KiwiSDRs with the best SNR scored
# and writes to a list usable by SuperSDR and possibly other applications. You
# change the criteria for the sorting or add more filters!

from kiwisdr_stripped import dictlist

# supersdr database
supersdr_file = "/home/user/kiwidata/kiwiservers"

# default frequency for SDR startup
default_freq = "10000.00"

###############################################################################
#       Edit the variables above; avoid editing the code below
###############################################################################

# filter the list of dictionaries by snr
listcount = 70
min_snr = 19
mykeys = ['url', 'loc']
sdrlist = []
filtered_dict = list(filter(lambda site: int(site["snr"][-2:].replace(',', ''))
                            > min_snr, dictlist))

# Filter by latitude & longitude -- reserved

# sort the list of dicts by snr and truncate
filtered_dict.sort(key=lambda item: item.get("snr"), reverse=True)
filtered_dict = filtered_dict[0:listcount]

# look at filtered_dict
# pp(filtered_dict)
for entry in filtered_dict:
    result = []
    for item in mykeys:
        val = entry.get(item)
        result.append(val)
    sdrlist.append(result)

# build the SuperSDR database
payload_3 = "# KiwiSDR bookmark format is...\n# server port frequency description\n"
for element in sdrlist:
    output = "\"" + element[1] + "\" " + element[0] + " " + default_freq + "\n"
    payload_3 = payload_3 + output
    payload_3 = payload_3.replace("http://", "")
    payload_3 = payload_3.replace(":", " ")

# Opening a text file in write
# mode using the open() function
with open(supersdr_file, 'w') as file:
    file.write(payload_3)
