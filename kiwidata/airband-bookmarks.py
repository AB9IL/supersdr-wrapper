#!/usr/bin/env python3

import datetime
import random
from kiwisdr_stripped import dictlist

source_file = "/usr/local/src/kiwidata/airband-template"
target_file = "/usr/local/src/kiwidata/airband-bookmarks"

# filter the list of dictionaries by latitude longitude
# use geographic boxes bounded by: (south, north, west, east)
# frequencies(day, night)
# time offset from UTC

# Tokyo (JP)
Tokyo = ("Tokyo", 34.8, 36.9, 138.7, 141.0, 121500, 121500, 9)
# Hokkaido
Hokkaido = ("Hokkaido", 41.1, 46.0, 138.0, 150.0, 121500, 121500, 9)
# Moscow
Moscow = ("Moscow", 54.0, 58.0, 34.0, 45.0, 121500, 121500, -5)
# Ottawa
Zurich = ("Zurich", 46.0, 48.5, 6.0, 10.5, 121500, 121500, -5)

regions = (
    Tokyo,
    Hokkaido,
    Moscow,
    Zurich,
)


def make_link(dictlist, area):
    # assigm freq limits (Hz)
    freq_range = (108100000, 137900000)
    # assign lat / lon boundaries
    lat_range = (area[1], area[2])
    lon_range = (area[3], area[4])
    # first freq is for daytime, second freq for night
    monitor_freqs = (area[5], area[6])
    listcount = 10
    min_snr = 1
    local_hour = area[7] + datetime.datetime.now(datetime.UTC).hour
    # select day or night frequency
    local_freq = area[6]
    if local_hour >= 7 and local_hour < 18:
        local_freq = area[5]
    dictlist = list(
        filter(lambda site: int(site["snr"][:2].replace(",", "")) > min_snr, dictlist)
    )
    # sort the list of dicts by snr
    dictlist.sort(key=lambda item: item.get("snr"), reverse=True)
    # filter the list by frequency range
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
    # filter the list according to lat / lon boundaries
    dictlist = list(
        filter(
            lambda site: float(site["gps"].split(",")[0][1:]) > lat_range[0], dictlist
        )
    )
    dictlist = list(
        filter(
            lambda site: float(site["gps"].split(",")[0][1:]) < lat_range[1], dictlist
        )
    )
    dictlist = list(
        filter(
            lambda site: float(site["gps"].split(",")[1][:-1]) > lon_range[0], dictlist
        )
    )
    dictlist = list(
        filter(
            lambda site: float(site["gps"].split(",")[1][:-1]) < lon_range[1], dictlist
        )
    )
    # exclude sites with no available channels
    dictlist = list(
        filter(lambda site: float(site["users"]) < float(site["users_max"]), dictlist)
    )
    # truncate the list
    dictlist = dictlist[0:listcount]
    # build the list of servers
    sdrlist = [entry.get("url") for entry in dictlist]
    random.shuffle(sdrlist)
    # For the bookmarks, we want only the SDR URL
    try:
        output = (area, sdrlist[0])
    except Exception as e:
        print(area[0], e)
        output = (area, "http://example.com:8073")
        pass
    yield output


with open(source_file, "r") as file:
    oldstuff = file.read()

# open the template and read the data
# the generator should return one URL for each area
# replace strings: area for URL
for item in (make_link(dictlist, area) for area in regions):
    item = next(item)
    # substitute a URL for area placeholder
    string1 = f'"{item[0][0]}'
    string2 = f'"{item[1]}/'
    oldstuff = oldstuff.replace(string1, string2)

with open(target_file, "w") as file:
    file.write(oldstuff)
