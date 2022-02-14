import json
import requests
import time
import os.path
import argparse
import csv
from datetime import datetime

timeBetweenRequests = 900

#Gets the command line args
parser = argparse.ArgumentParser(description='Retrieve data from TomTom on a road every 5 minutes')
parser.add_argument('csvFile', help='The file to load segments data from')
parser.add_argument('apiKey', help="A TomTom API key")
parser.add_argument('-v', '--verbose', action='store_true', help='Output collected data to terminal')

args = parser.parse_args()
if args.verbose:
    print("This will be verbose")


while(True):
    with open(args.csvFile) as f:
        reader = csv.reader(f, delimiter=',')
        if args.verbose: print("Making requests")
        for row in reader:
            if args.verbose: print(row)
            #make the request
            r = requests.get('https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key='+args.apiKey+'&point='+row[1])
            jsondata = r.json()
            #print the data to console
            if args.verbose: print(("Id: ", str(row[0]), "Current Speed: ", int(jsondata['flowSegmentData']['currentSpeed']), "Free Flow Speed",
                int(jsondata['flowSegmentData']['freeFlowSpeed']), "Current Travel Time: ",int(jsondata['flowSegmentData']['currentTravelTime']), 
                "Free Flow Travel Time: ",int(jsondata['flowSegmentData']['freeFlowTravelTime']),"Confidence: ",
                float(jsondata['flowSegmentData']['confidence'])))
            with open('./CSVs/'+str(row[0])+'.csv', mode='a') as data:
                writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")), float(jsondata['flowSegmentData']['currentSpeed']), float(jsondata['flowSegmentData']['confidence'])])
        time.sleep(timeBetweenRequests)
