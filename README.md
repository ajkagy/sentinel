# Vivo Sentinel

### Follow the installation steps below or the official Vivo sentinel guide: https://www.vivocrypto.com/vivo-technologies/masternodes/sentinel-guide/


Sentinel is an all-powerful toolset for Vivo.

Sentinel is an autonomous agent for persisting, processing and automating Vivo V12.1 governance objects and tasks, and for expanded functions in upcoming releases.

Sentinel is implemented as a Python application that binds to a local version 12.1 vivod instance on each Vivo V12.1 Masternode.

This guide covers installing Sentinel onto an existing MasterNode in Windows

Use at your own risk, it has been compiled exactly as the Github repo says


## Installation

### 1. Install

1. Close your wallet.

2. Download the sentinel-vivo-win64.exe and place it into a folder.

2. Copy database folder from source into the folder where sentinel-vivo-win64.exe executable resides.

3. Copy sentinel.conf to the folder where your sentinel-vivo-win64.exe resides

### 3. Configure & Test Your Configuration

Open sentinel.conf

Uncomment the #vivo_conf line, at the top of the file, then adjust the path to your Masternode’s vivo.conf. Save the file then close it.

    vivo_conf=C:\path\to\vivo.conf

Now run sentinel-vivo-win64.exe

You should see: “vivod not synced with network! Awaiting full sync before running Sentinel.”
This is exactly what we want to see at this stage.

If the wallet has been resynched alreaedy, you will see no output which is what you want to see and it means you can skip the next sync step.

