# SuperSDR  Wrapper
Easy fuzzyfinder and list sorter to use with SuperSDR

## Why a wrapper for SuperSDR?
SuperSDR is a lightweight and functional client for using the global network of KiwiSDR receivers. There are about 600 radios available for anyone to use, with with various locations and reception quality. SuperSDR Wrapper works in two modes: selecting receivers (servers) and tuning specific stations (bookmarks).  As a server selector, the script can read a list of KiwiSDRs, sort them according to sensitivity, and present the user with a fuzzy-searchable menu of the ones with top rankings. The chosen KiwiSDR opens for streaming in SuperSDR. As a bookmark picker, the script opens a KiwiSDR server geographically proximate to a desired station or frequency of interest.

SuperSDR wrapper saves time. Do you really want to bumble around with a long string of command line arguments when you could already be listening to the BBC or Brother Stair?? With this wrapper, you can have a receiver streaming signals to you in seconds.

#### Usage

A mode argument must be given: --bookmarks, --servers, --map, or --kill. With no other arguments, the list will be produced in the terminal by fzf:
```bash
$  supersdr-wrapper --bookmarks
```

To pull up a list of servers in Rofi, use the _--gui_ argument:
```bash
$  supersdr-wrapper --servers --gui
```

To see a map of currently online SDRs, use the _--map_ argument:
```bash
$  supersdr-wrapper --map
```

If SuperSDR freezes or locks up, eliminate the processes with the _--kill_ argument:
```bash
$  supersdr-wrapper --kill
```

To force an update to the SDR data, use the stripper utility:
```bash
$  stripper
```

#### Dependencies

```
Python3
Bash
Rofi
fzf
dyatlov map maker
```

SuperSDR Wrapper requires a minimum of Python3 and Rofi. Selecting KiwiSDR servers on the command line requires fzf. It is suggested to also install the Dyatlov SDR Map maker to plot servers on a map in your web browser. The map maker also keeps an updated list of KiwiSDRs, sourced from their primary server database.

#### IMPORTANT
Scripts _supersdr-wrapper_ and _stripper_ should be placed in your *path* and made *executable*.

Inside the scripts, you must edit the proper paths for the data files and lists. Data wrangling happens in directory _kiwidata_. Processed data must be written to the file _kiwiservers_ in directory _kiwidata_ or _supersdr_. You can keep directories _supersdr_ and _kiwidata_ anywhere you want, but be sure to set proper paths in the scripts.
