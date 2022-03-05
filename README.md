# notion-mindmap

Framework for developing and visualizing mind maps in notion.

### **WORK IN PROGRESS** - Forked from [here](https://github.com/davidAmiron/notion-mindmap) on 4 Mar 2022

## Setup
1. Clone this project and install prereqs, preferably in a venv and run `pip install -r requirements.txt`
2. Get your notion token, see [here](https://developers.notion.com/docs/getting-started) and place it in the `./token` file.

## Setup (For Beginners)
1. This code is written in [Python](https://www.python.org/downloads/), and it's best to use [Pip](https://pip.pypa.io/en/stable/installation/) for package management and [virtualenv](https://pip.pypa.io/en/stable/installation/) for virtual environments (see more below)
1. Clone this repo onto your computer with `git clone https://github.com/EricTurner3/notion-mindmap`, or use the Download ZIP feature and enter into the directory with Command Prompt or Powershell
1. Virtual environments help prevent conflictions if you have multiple projects that require different versions of the same library. `virtualenv venv` will create a `./venv` folder for you to use
1. With `./venv` created, run:
    - Windows:  `. .\venv\Scripts\activate.ps1`
    - *nix: `source /venv/bin/activate`
1. Your terminal will display `(venv)` as a prefix now to indicate you are in the virtual environment. Run `pip install -r requirements.txt` to install all the requirements to use this project
1. Now read the directions [here](https://developers.notion.com/docs/getting-started) to grab your token and place it in the `./token` file



