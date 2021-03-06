from sys import argv
import csv
#import speedtest
import pathlib
import datetime
import os
import subprocess

def get_res():
	#local =os.environ['test']
	#exen = "\\speedtest.exe"
	#final = local + exen
	download = 0
	upload = 0
	print("############ getting results")
	Trec2 = datetime.datetime.now()
	date = Trec2.strftime("%d/%m/%Y")
	time = Trec2.strftime("%H:%M:%S")
	print("JOB St Date: {} Time {}".format(date,time))

	try:	
		output = subprocess.check_output(["speedtest", "-u", "Mbps", "-f", "csv"], stderr=open(os.devnull))
		#output = subprocess.Popen(["speedtest", "-f", "csv"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
	except subprocess.CalledProcessError:
		print('CONECTION ERROR')
		reason = loc() + "_ERROR"
		#['server name','server id','latency','jitter','packet loss','download','upload','download bytes','upload bytes','share url']
		error_data = [f'"{reason}"',',' ,f'"{reason}"',',' ,'"100000000000"', ',','"0"', ',','"100"',',' ,'"0"',',' ,'"0"',',' ,'"0"',',' ,'"0"', ',',f'"{reason}"']
		listToStr = ''.join(map(str, error_data)) 
		error_dataB = str.encode(listToStr)
		fdata = process_data(error_dataB)
		return fdata
	fdata = process_data(output)
	
	return fdata

def process_data(str1):
	
	bTos = str1.decode("utf-8")
	sList = [x.strip('"') for x in bTos.split(',')]
	#['server name','server id','latency','jitter','packet loss','download','upload','download bytes','upload bytes','share url']
	data = {'Download':sList[5], 'Upload':sList[6], 'Latency':sList[2], 'Packet_Loss':sList[4], 'Jitter':sList[3], 'Server_ID':sList[1], 'Server_Name':sList[0], 'share_link':sList[9]}
	return data

def loc():
	try:
		output = subprocess.check_output(["ping", "-n", "2", "192.168.1.1"], stderr=open(os.devnull))
	
	except subprocess.CalledProcessError:
		print("ERROR: cant see router DNS")
		return "router down"
	try:
		output = subprocess.check_output(["ping", "-n", "2", "8.8.8.8"], stderr=open(os.devnull))
	except subprocess.CalledProcessError:
		print("ERROR: cant see google DNS")
		return "ISP down"

def pathing():
	local =os.environ['appdata']
	#create uneque dir
	speed_test_dir1 = f'\\speedtest'
	speed_test_dir2	= '\\results'
	res_csv ='\\speedtest_results.csv'
	root_dir = local + speed_test_dir1 + speed_test_dir2
	
	if pathlib.Path(root_dir).exists() != bool(True):
		os.mkdir(local + speed_test_dir1)
		os.mkdir(root_dir)
	
	final_path = root_dir + res_csv

	return final_path

def write_res(results_dict, final_path):

	Trec = datetime.datetime.now()
	date = Trec.strftime("%d/%m/%Y")
	time = Trec.strftime("%H:%M:%S")
#	data = {'Download':sList[5], 'Upload':sList[6], 'Latency':sList[2], 'Packet_Loss':sList[4] 'Jitter':sList[3]}, 'Server_ID':sList[1], 'Server_Name':sList[0]}
	
	data= [{'Date':date, 'Time':time, 'Download':results_dict['Download'], 'Upload':results_dict['Upload'], 'Ping':results_dict['Latency'], 'Packet_Loss':results_dict['Packet_Loss'], 'Jitter':results_dict['Jitter'], 'Server_ID':results_dict['Server_ID'], 'Server_Name':results_dict['Server_Name'], 'share_link':results_dict['share_link']}]

	if pathlib.Path(final_path).exists():
		csvfile=open(final_path,'a+', newline='')
		fields=list(data[0].keys())
		obj=csv.DictWriter(csvfile, fieldnames=fields)
		print(f"append Date: {date} Time: {time}")

	else:
		csvfile=open(final_path,'w', newline='')
		fields=list(data[0].keys())
		obj=csv.DictWriter(csvfile, fieldnames=fields)
		obj.writeheader()
		print(f"Created Date: {date} Time: {time}")
	
	obj.writerows(data)
	csvfile.close()


def main():
	sresult = get_res()
	spath = pathing()
	write_res(sresult, spath)

main()