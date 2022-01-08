import csv
import pandas as pd 
import statistics

df = pd.read_csv("data.csv")
genderlist = df["gender"].to_list()

gendermean = statistics.mean(genderlist)
gendermedian = statistics.median(genderlist)
gendermode = statistics.mode(genderlist)
genderstd = statistics.stdev(genderlist)

g1stdevs, g1stdeve = gendermean-genderstd, gendermean+genderstd
g2stdevs, g2stdeve = gendermean - (2*genderstd), gendermean + (2*genderstd)

gldi1std = [result for result in heightlist if result>g1stdevs and result<g1stdeve]
print("Percentage of data lies between two std is ", len(genderlist)*100.0/len(genderlist))

gldi2std = [result for result in heightlist if result>g2stdevs and result<g2stdeve]
print("Percentage of data lies between two std is ", len(genderlist)*100.0/len(genderlist))