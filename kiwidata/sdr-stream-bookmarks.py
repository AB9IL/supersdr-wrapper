#!/usr/bin/env python3

import datetime
import random
from kiwisdr_stripped import dictlist

source_file = "/usr/local/src/kiwidata/sdr-stream-bookmarks-template"
target_file = "/usr/local/src/kiwidata/sdr-stream-bookmarks"
# assigm freq limits (Hz)
freq_range = (10000, 29999999)

# filter the list of dictionaries by latitude longitude
# use geographic boxes bounded by: (south, north, west, east)
# frequencies(day, night)
# time offset from UTC

# Newfoundland
Newfoundland = ("Newfoundland", 45.0, 52.0, -66.5, -52.0, 10000, 5000, -5)
# Montreal
Montreal = ("Montreal", 44.5, 47.0, -75.5, -72.0, 10000, 5000, -5)
# Ottawa
Ottawa = ("Ottawa", 44.5, 46.5, -77.0, -74.0, 10000, 5000, -5)
# Oshawa
Oshawa = ("Oshawa", 43.0, 44.5, -81.0, -77.5, 10000, 5000, -5)
# Winnipeg
Winnipeg = ("Winnipeg", 49.0, 51.0, -98.5, -95.5, 10000, 5000, -6)
# Watrous
Watrous = ("Watrous", 50.3, 54.0, -112.0, -103.5, 10000, 5000, -6)
# Edmonton
Edmonton = ("Edmonton", 51.0, 56.0, -117.0, -110.0, 10000, 5000, -7)
# Vancouver
Vancouver = ("Vancouver", 48.0, 50.2, -126.0, -119.0, 10000, 5000, -8)
# New York
New_York = ("NewYork", 39.7, 42.0, -76.4, -72.0, 10000, 5000, -5)
# Wisconsin
Wisconsin = ("Wisconsin", 41.0, 47.3, -93.8, -86.6, 10000, 5000, -6)
# Chicago
Chicago = ("Chicago", 39.5, 42.5, -90.0, -86.0, 10000, 5000, -6)
# Shannon (IE)
Shannon = ("Shannon", 51.2, 54.5, -10.7, -7.4, 10000, 5000, 0)
# Dublin (IE)
Dublin = ("Dublin", 52.3, 55.0, -9.0, -3.0, 10000, 5000, 0)
# Denmark Area
Denmark_Area = ("DenmarkArea", 52.5, 60.5, -3.0, 20.0, 10000, 5000, 1)
# London (UK)
London_UK = ("London", 49.8, 53.5, -5.4, 3.4, 10000, 5000, 0)
# France_Belgium
France_Belgium = ("France_Belgium", 42.0, 52.0, -5.0, 10.0, 10000, 5000, 1)
# Germany Switzerland
Germany_Switzerland = ("Germany_Switzerland", 45.7, 54.9, 6.1, 15.2, 10000, 5000, 1)
# Cyprus
cyprus_area = ("Cyprus", 34.4, 35.9, 31.9, 34.8, 10000, 5000, 0)
# NewSouthWales (AUS)
NewSouthWales_AUS = ("NewSouthWales", -35.5, -32.5, 148.8, 152, 10000, 5000, 11)
# SouthAustralia (AUS)
SouthAustralia_AUS = ("SouthAustralia", -35.5, -32.5, 148.8, 152, 10000, 5000, 10)
# NorthNewZealand (NZ)
NorthNewZealand_NZ = (
    "NorthNewZealand",
    -42.8,
    -34.2,
    172.6,
    178.7,
    5000,
    10000,
    12,
)
# South East Asia
# Newfoundland
South_East_Asia = ("South_East_Asia", -11.0, 18.7, 92.0, 127.0, 10000, 5000, 7)
# Midwest (US)
Midwest_US = ("Midwest", 37.0, 43.5, -91.5, -80.0, 10000, 5000, -5)
# Pennsylvania
Pennsylvania = ("Pennsylvania", 39.7, 42.0, -84.5, -74.5, 10000, 5000, -4)
# Arkansas
Arkansas = ("Arkansas", 31.0, 39.0, -98.0, -86.0, 10000, 5000, -5)
# Utah_Arizona
Utah_Arizona = ("Utah_Arizona", 33.3, 42.0, -114.0, -109.0, 10000, 5000, -7)
# San Francisco
San_Francisco = ("San Francisco", 37.0, 39.0, -123.0, -120.0, 10000, 5000, -7)
# Southeast (US)
Southeast_US = ("Southeast_US", 24.0, 36.5, -91.5, -74.5, 10000, 5000, -4)
# NAT Tracks West
NAT_West_area = ("NAT_West", 40.2, 47.2, -76.9, -52.0, 10000, 5000, -4)
# WATRS
WATRS_area = ("WATRS", 17.0, 42.0, -84.0, -62.0, 10000, 5000, -4)
# CEPAC
CEPAC_area = ("CEPAC", 16.0, 52.0, -163.0, -116.0, 10000, 5000, -9)
# HFGCS Northeast
HFGCS_NE = ("HFGCS_Northeast", 40.9, 46.0, -75.0, -69.0, 10000, 5000, -4)
# HFGCS Northwest
HFGCS_NW = ("HFGCS_Northwest", 38.7, 51.7, -126.0, -103.5, 10000, 5000, -7)
# Bangkok (TH)
bangkok_area = ("Bangkok", 12.4, 14.7, 99.4, 101.9, 10000, 5000, -7)
# Tokyo (JP)
tokyo_area = ("Tokyo", 34.8, 36.9, 138.7, 141.0, 10000, 5000, -7)

regions = (
    Newfoundland,
    Montreal,
    Ottawa,
    Oshawa,
    Winnipeg,
    Watrous,
    Edmonton,
    Vancouver,
    New_York,
    Wisconsin,
    Chicago,
    Shannon,
    Dublin,
    Denmark_Area,
    London_UK,
    France_Belgium,
    Germany_Switzerland,
    NewSouthWales_AUS,
    SouthAustralia_AUS,
    NorthNewZealand_NZ,
    South_East_Asia,
    Midwest_US,
    Pennsylvania,
    Arkansas,
    Utah_Arizona,
    San_Francisco,
    Southeast_US,
    NAT_West_area,
    WATRS_area,
    CEPAC_area,
    HFGCS_NE,
    HFGCS_NW,
    bangkok_area,
    tokyo_area,
    cyprus_area,
)


def make_link(dictlist, area):
    lat_range = (area[1], area[2])
    lon_range = (area[3], area[4])
    # first freq is for daytime, second freq for night
    monitor_freqs = (area[5], area[6])
    listcount = 10
    min_snr = 15
    local_hour = area[7] + datetime.datetime.now(datetime.UTC).hour
    # select day or night frequency
    local_freq = area[6]
    if local_hour >= 7 and local_hour < 18:
        local_freq = area[5]
    dictlist = list(
        filter(lambda site: int(site["snr"][-2:].replace(",", "")) > min_snr, dictlist)
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
