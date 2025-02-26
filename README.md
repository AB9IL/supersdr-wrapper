# SuperSDR Wrapper

Easy fuzzyfinder and list sorter to use with SuperSDR

## Why a wrapper for SuperSDR?

SuperSDR is a lightweight and functional client for using the global network of KiwiSDR and Web-888 receivers. There are about 900 radios available for anyone to use, with with various locations and reception quality. SuperSDR Wrapper works in three modes: selecting receivers (servers), tuning specific stations (bookmarks), and starting the SDR Map (if installed). As a server selector, the script can read a list of SDRs, sort them according to sensitivity, and present the user with a fuzzy-searchable menu of the ones with top rankings. The chosen KiwiSDR or Web-888 SDR opens for streaming in SuperSDR. As a bookmark picker, the script opens an SDR server geographically proximate to a desired station or frequency of interest.

SuperSDR wrapper saves time. Do you really want to bumble around with a long string of command line arguments when you could already be listening to the BBC or Brother Stair?? With this wrapper, you can have a receiver streaming signals to you in seconds.

SuperSDR Wrapper is now able to sort receivers by frequency bands in addition to SNR score, sothere is now a VHF-Airband list (also usable for VHF weather satellite downlinks and ISS communications).

#### Usage

A mode argument must be given: --bookmarks, --servers, --map, or --kill. With no other arguments, the list will be produced in the terminal by fzf:

For a list of KiwiSDR and Web-888 SDR servers:

```bash
$  supersdr-wrapper --bookmarks
```

For a list of airband / Wxsat / 2-meter VHF SDRs:

```bash
$  supersdr-wrapper --airband
```

To see a list of servers in Rofi, use the _--gui_ argument:

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
yad
dyatlov map maker
```

SuperSDR Wrapper requires a minimum of Python3, Yad, and Rofi. Selecting SDR servers on the command line requires fzf. It is suggested to also install the Dyatlov SDR Map maker to plot servers on a map in your web browser. The map maker also keeps an updated list of KiwiSDRs, sourced from their primary server database. Dyatlov includes a server list updater.

An updated list of Web-888 servers is available from this repository; automatic updating is in the works, to be published here in the future.

#### Keybinds

SuperSDR Wrapper may be launched from your keyboard if you set up proper bindings. Here is example code to launch it using the Simple X Hotkey Daemon (SXHKD):

```
# Launch SuperSDR Wrapper with Super + s and ctrl / shift / alt keys
super + s + {shift,ctrl,alt}
    {radiostreamer gui,supersdr-wrapper --bookmarks --gui,supersdr-wrapper --servers --gui,supersdr-wrapper --airband --gui}
```

#### IMPORTANT

Scripts _supersdr-wrapper_ and _stripper_ should be placed in your _path_ and made _executable_.

Inside the scripts, you must edit the proper paths for the data files and lists. Data wrangling happens in directory _kiwidata_. Processed data must be written to the file _kiwiservers_ in directory _kiwidata_ or _supersdr_. You can keep directories _supersdr_ and _kiwidata_ anywhere you want, but be sure to set proper paths in the scripts.
