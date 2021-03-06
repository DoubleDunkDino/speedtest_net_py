# speedtest_net_py
A python script to monitor network bandwidth over time creating a basic CSV file. leveraging the ookla speed command line test tool.

Purpose:
A very simple python script to test the internet connection over time and log the results to a csv file. further detect if the outage is due to downed wifi or DNS error.

Setup:
1. obtain the command line client by ookla and ensure its accessable by the commandline path https://www.speedtest.net/apps/cli
2. using a cmd or powershell run the scheduler script. run using py .\scriptsceduler.py

Notes:
uses the ookla command line as its writen in a lower level language. I found the python derived network speed tools where unable to accuratly record network speeds.
I did not use the inbuilt csv output to the ookla speed test command as i wanted to drive the CSV with ping test to indicate if the ISP or router had dropped out in line.

Why create this script:
Suffered from dropping out interenet and needed to prove to my landlord and ISP the quality and consistancy of the internet, and it has been ages since i created anything. I like custom csv files...

opperating system:
Windows (tested on windows 10). With some minor changes to the script it should be able to work on other operating systems (changing back slashes to forward, etc), just need to also download the apropiate command line client from ookla.
