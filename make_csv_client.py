import csv
import os
import json

ciphers = ["AES128-GCM-SHA256", "AES256-GCM-SHA384", "ECDHE-RSA-AES128-GCM-SHA256", "ECDHE-RSA-AES256-GCM-SHA384"]

empty = True
def writeToCSV(outFile, data):
    # Write the data to a CSV file

    if os.path.exists(outFile):
        empty = False
    else: 
        empty = True
    with open(outFile, 'a', newline='') as file:
        writer = csv.writer(file)
        if empty:
            writer.writerow(["TLS_type", "throughput"])
        writer.writerow(data)

pathIN = "/home/alex/Desktop/benchmark_analysis/results_client"
pathOUT = "/home/alex/Desktop/benchmark_analysis/results_client_csv"



for file in os.listdir(pathIN):
    for cip in ciphers: 
        if file.startswith(cip):
            if "_TLS_" in file:
                with open(os.path.join(pathIN, file) , "r", encoding='utf-8') as f: 
                    outpath = os.path.join(pathOUT, cip)+file[len(cip)-1:][5:][:-7]+".csv"
                    #outpath = os.path.splitext(outpath)[0]+".csv"
                    thr = json.load(f)["throughput"]*1000
                    data = ["TLS",thr]
                    writeToCSV(outpath,data)
            if "cpu_kTLS_" in file:
                with open(os.path.join(pathIN, file) , "r", encoding='utf-8') as f: 
                    outpath = os.path.join(pathOUT, cip)+file[len(cip)-1:][10:][:-7]+".csv"
                    #outpath = os.path.splitext(outpath)[0]+".csv"
                    thr = json.load(f)["throughput"]*1000
                    data = ["sw_kTLS",thr]
                    writeToCSV(outpath,data)
            if "hw_kTLS_" in file:
                with open(os.path.join(pathIN, file) , "r", encoding='utf-8') as f: 
                    outpath = os.path.join(pathOUT, cip)+file[len(cip)-1:][9:][:-7]+".csv"
                    #outpath = os.path.splitext(outpath)[0]+".csv"
                    thr = json.load(f)["throughput"]*1000
                    data = ["hw_kTLS",thr]
                    writeToCSV(outpath,data)
