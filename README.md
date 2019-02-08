[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
# Installation

Install pypresence with **`pip`**

### `pip install pypresence`
Then clone this repo

# Setup

### Turning on the web interface
In your Kodi settings navigate to `Settings → Services → Control → Allow remote control via HTTP`

Turn on `Allow remote control via HTTP`

For more help go to the [Kodi wiki](https://kodi.wiki/view/Web_interface)

**By default the port should be set to 8080.** If you have changed it, please specify in `main.py` on line 3 the new port



## Advanced setup

If you are extremely confident with what you are doing, you can use the [Autoexec.py](https://kodi.wiki/view/Autoexec.py) file to run this code on startup. This method is not recommended as the code is not designed to be ran as a module.

## Running

Make sure Kodi is running and run `main.py`

Nb: the "time remaining" section may display a random time ie 19 hours. However this will just be for yourself. Other users will see the correct time remaining
