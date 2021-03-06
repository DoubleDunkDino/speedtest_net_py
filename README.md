# speedtest_net_py
A python script to monitor network bandwidth over time creating a basic CSV file. leveraging the ookla speed command line test tool.

purpose:
A very simple python script to test the internet connection over time and log the results to a csv file. further detect if the outage is due to downed wifi or DNS error.

setup:
1. obtain the command line client by ookla and ensure its accessable by the commandline path
2. using a cmd or powershell run the scheduler script.

notes:
uses the ookla command line as its writen in a lower level language. I found the python derived network speed tools where unable to accuratly record network speeds.
I did not use the inbuilt csv output to the ookla speed test command as i wanted to drive the CSV with ping test to indicate if the ISP or router had dropped out in line.
