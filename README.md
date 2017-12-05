# Vivo Sentinel

### Follow the installation steps below or the official Vivo sentinel guide: https://www.vivocrypto.com/vivo-technologies/masternodes/sentinel-guide/


Sentinel is an all-powerful toolset for Vivo.

Sentinel is an autonomous agent for persisting, processing and automating Vivo V12.1 governance objects and tasks, and for expanded functions in upcoming releases.

Sentinel is implemented as a Python application that binds to a local version 12.1 vivod instance on each Vivo V12.1 Masternode.

This guide covers installing Sentinel onto an existing MasterNode in Windows

Use at your own risk, it has been compiled exactly as the Github repo says

Kaspersky scan results:
![sen​t​i​n​e​l​-​v​i​v​o​-​w​i​n​6​4​.​exe scan results](/sentinel-scan.jpg?raw=true "sen​t​i​n​e​l​-​v​i​v​o​-​w​i​n​6​4​.​exe scan results")


## Installation

### 1. Install

1. Close your wallet.

2. Download the sentinel-vivo-win64.exe and place it into a folder.

2. create a folder and name it "database" inside the folder you placed your executable.

3. Copy the sentinel.conf to the folder where your sentinel-vivo-win64.exe resides
https://github.com/ajkagy/sentinel/blob/master/sentinel.conf

### 3. Configure & Test Your Configuration

Open sentinel.conf

Uncomment the #vivo_conf line, at the top of the file, then adjust the path to your Masternode’s vivo.conf. Save the file then close it.

    vivo_conf=C:\path\to\vivo.conf

Now run sentinel-vivo-win64.exe