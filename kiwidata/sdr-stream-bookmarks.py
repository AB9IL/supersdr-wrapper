#!/usr/bin/env python3

import datetime
import random

import pandas as pd
from kiwisdr_stripped import dictlist

station_file = "/usr/local/src/kiwidata/stations"
region_file = "/usr/local/src/kiwidata/regions"
band_file = "/usr/local/src/kiwidata/bands"
target_file = "/usr/local/src/kiwidata/sdr-stream-bookmarks"
raw_serverfile = "/usr/local/src/dyatlov/kiwisdr_com.js"


# create dataframes from csv files
def csv_to_dataframe(file, columns):
    df = pd.read_csv(file, names=columns, header=None)
    return df


# Define stationdata and column names
station_cols = [
    "description",
    "region",
    "url",
    "frequency",
    "mode",
    "sdrtype",
]
stationdata = csv_to_dataframe(station_file, station_cols)

# Define regiondata and column names
region_cols = [
    "region_match",
    "south_latlimit",
    "north_latlimit",
    "west_lonlimit",
    "east_lonlimit",
    "day_freq",
    "night_freq",
    "utc_offset",
]
regiondata = csv_to_dataframe(region_file, region_cols)

# Define bands and receiver parameters for
# snr and frequency range per band (kHz):
band_cols = [
    "band",
    "snr_limit",
    "freq_bot",
    "freq_top",
]
bandparams = csv_to_dataframe(band_file, band_cols)
bandparams.set_index("band", inplace=True)

# filter the list of dictionaries by latitude longitude
# use geographic boxes bounded by: (south, north, west, east)
# frequencies(day, night)
# time offset from UTC


def make_link(dictlist, index, area):
    output = ""
    if area["region_match"] == thisregion and "kiwi" == sdrtype:
        # assign lat / lon boundaries
        lat_range = (area["south_latlimit"], area["north_latlimit"])
        lon_range = (area["west_lonlimit"], area["east_lonlimit"])
        # first freq is for daytime, second freq for night
        monitor_freqs = (area["day_freq"], area["night_freq"])
        listcount = 5
        local_hour = area["utc_offset"] + datetime.datetime.now(datetime.UTC).hour
        # select day or night frequency
        local_freq = area["night_freq"]
        if local_hour >= 7 and local_hour < 18:
            local_freq = area["day_freq"]
        # filter the list according to lat / lon boundaries
        dictlist = list(
            filter(
                lambda site: float(site["gps"].split(",")[0][1:]) > lat_range[0],
                dictlist,
            )
        )
        dictlist = list(
            filter(
                lambda site: float(site["gps"].split(",")[0][1:]) < lat_range[1],
                dictlist,
            )
        )
        dictlist = list(
            filter(
                lambda site: float(site["gps"].split(",")[1][:-1]) > lon_range[0],
                dictlist,
            )
        )
        dictlist = list(
            filter(
                lambda site: float(site["gps"].split(",")[1][:-1]) < lon_range[1],
                dictlist,
            )
        )
        # exclude sites with no available channels
        dictlist = list(
            filter(
                lambda site: float(site["users"]) < float(site["users_max"]), dictlist
            )
        )
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
        # filter the list by snr
        dictlist = list(
            filter(
                lambda site: int(site["snr"][:2].replace(",", "")) > min_snr, dictlist
            )
        )
        # sort the list of dicts by snr
        dictlist.sort(key=lambda item: item.get("snr"), reverse=True)
        # truncate the list
        dictlist = dictlist[0:listcount]
        # build the list of servers
        sdrlist = [entry.get("url") for entry in dictlist]
        random.shuffle(sdrlist)
        # For the bookmarks, we want only the SDR URL
        try:
            output = (
                f"{description},{band},{sdrlist[0]}/,{frequency},{mode},{sdrtype}\n"
            )
        except Exception:
            # output = f"{description},http://example.com:8073/,{frequency},{mode},{sdrtype}\n"
            pass

    # Non-Kiwi tupes of SDRs are not filtered by region.
    # Use index == 0 to prevent duplication during iterations through regions.
    elif "web" == sdrtype and index == 0:
        output = f"{description},{band},{url},{frequency},{mode},{sdrtype}\n"

    elif "phantom" == sdrtype and index == 0:
        output = f"{description},{band},{url},{frequency},{mode},{sdrtype}\n"

    elif "openwebrx" == sdrtype and index == 0:
        output = f"{description},{band},{url},{frequency},{mode},{sdrtype}\n"

    else:
        output = ""
    if len(output) > 3:
        yield output
    else:
        yield


out_data = ""
# Determine required SDR parameters from the station data. For each station,
# assign minimum snr and frequency range according to the band.
for index, row in stationdata.iterrows():
    thisregion = row["region"]
    description = row["description"]
    url = row["url"]
    # get the kHz frequenct and convert to Hz
    frequency = row["frequency"]
    frequency_hz = int(f"{frequency}000")
    mode = row["mode"]
    sdrtype = row["sdrtype"]
    # determine band and assign parameters
    for index, row in bandparams.iterrows():
        if frequency_hz >= row["freq_bot"] and frequency_hz <= row["freq_top"]:
            band = index
            min_snr = row["snr_limit"]
            # assign min and max frequency parameters for desired band
            min_hz = int(row["freq_bot"])
            max_hz = int(row["freq_top"])
            freq_range = [min_hz, max_hz]

    # For each row in region data, scan the dictionaies for SDRs meeting
    # geographic bounds, snr score, and other parameters. The generator should
    # yield a formatted comma separated string for each station bookmark.
    # Bookmarks will be skipped if no SDRs pass the filters.
    with open(target_file, "w") as file:
        for item in (
            make_link(dictlist, index, row) for index, row in regiondata.iterrows()
        ):
            item = next(item)
            # Build the bookmarks variable by appending
            # lines then print it to a file.
            try:
                out_data += item
            except Exception:
                pass

        # print(out_data)
        file.write(out_data)
