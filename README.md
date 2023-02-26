# SuperSDR  Wrapper
Easy fuzzyfinder and list sorter to use with SuperSDR

## Why a wrapper for SuperSDR?
SuperSDR is a lightweight and functional client for using the global network of KiwiSDR receivers. There are nearly 500 radios available for anyone to use, with with various locations and reception quality. SuperSDR Wrapper can read a list of KiwiSDRs, sort them according to sensitivity, and present tue user with a fuzzy-searchable menu of the ones with top rankings. The chosen KiwiSDR opens for streaming in SuperSDR.

A wrapper saves time. Do you really want to bumble around with a long string of command line arguments when you could already be listening to the BBC or Brother Stair?? With this wrapper, you can have a receiver streaming signals to you in seconds.

#### Usage

With no command line arguments, the list will be produced by fzf:
```bash
$  supersdr-wrapper
```

To pull up a list of servers in Rofi, use the _gui_ argument:
```bash
$  supersdr-wrapper gui
```

If SuperSDR freezes or locks up, eliminate the processes with the _kill_ argument:
```bash
$  supersdr kill
```

To update the list, use the stripper utility:
```bash
$  stripper
```

#### Dependencies

```
Python3
Bash
Rofi
fzf
```

SuperSDR Wrapper requires a minimum of Python3 and Rofi. Selecting KiwiSDR servers from the command line requires fzf.

#### IMPORTANT
Scripts _supersdr-wrapper_ and _stripper_ should be placed in your *path*.

Inside the scripts, you must edit the proper paths for the data files and lists. Data wrangling happens in directory _kiwidata_. Processed data must be written to the file _kiwiservers_ in directory _supersdr_. You can keep directories _supersdr_ and _kiwidata_ anywhere you want, but be sure to set proper paths in the scripts.
