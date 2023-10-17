import csv
import os

# # Read the data from the file
# with open('exampleTh', 'r') as file:
#     lines = file.readlines()

# # Extract the data and format it for CSV
# data = [line.split() for line in lines[1:]]

# # Write the data to a CSV file
# with open('output2.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Elapsed time", "CPU (%)", "Real (MB)", "Virtual (MB)"])
#     writer.writerows(data)


def writeToCSV(inFile, outFile, type):

    # Read the data from the file
    with open(inFile, 'r') as file:
        lines = file.readlines()

    # Extract the data and format it for CSV
    if type == 'cpu':
        data = [line.split() for line in lines[1:]]
    else: 
        data = [line.split() for line in lines[2:]]
    
    

    # Write the data to a CSV file
    with open(outFile, 'w', newline='') as file:
        writer = csv.writer(file)
        if type == 'cpu':
            writer.writerow(["elapsed_time", "CPU", "Real_(MB)", "Virtual_(MB)"])
        else: 
            writer.writerow(["time", "KB/s_in", "KB/s_out"])
        writer.writerows(data)

pathCPU = "/home/alex/Desktop/benchmark_analysis/results/cpu"
pathThroughput = "/home/alex/Desktop/benchmark_analysis/results/throughput"
pathCPUOut = "/home/alex/Desktop/benchmark_analysis/results_csv/cpu"
pathThroughputOut = "/home/alex/Desktop/benchmark_analysis/results_csv/throughput"


for file in os.listdir(pathCPU):
    inpath = os.path.join(pathCPU, file)
    outpath = os.path.join(pathCPUOut, file)
    outpath = os.path.splitext(outpath)[0]+".csv"
    writeToCSV(inpath, outpath, "cpu")

for file in os.listdir(pathThroughput):
    inpath = os.path.join(pathThroughput, file)
    outpath = os.path.join(pathThroughputOut, file)
    outpath = os.path.splitext(outpath)[0]+".csv"
    writeToCSV(inpath, outpath, "dsadasfgdsbjkdhasl;sl")


