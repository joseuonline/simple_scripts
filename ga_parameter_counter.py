#This is to count parameters and corresponding pageviews from a GA page download report. Lots of room for improvement...give me a break!

import csv
import re
from collections import defaultdict


params_views = {}
params_unique_views = {}
params_users = {}
with open('<GA PAGE DOWNLOAD FILE NAME.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        try:
            url = row[0]
            #print(url)
            all_params = re.search('\?(.*)', url)
            key_pair = all_params.group(1).split('&')
            #print(key_pair)
            #print(type(key_pair))
            for key in key_pair:
                #print('printing key', key)
                a = key.split("=")[0]
                #print('printing a', a)

                if a in params_views:
                    params_views[a] += int(row[1])
                else:
                    params_views[a] = int(row[1])
                #params_views[key]=row[1]
        except:
            continue

#print('param','pageview')
#for p,count in params_views.items():
#    print( p , count)



params_views = [(k, params_views[k]) for k in sorted(params_views, key=params_views.get, reverse=True)]


with open('results.csv', 'w') as f:  # Just use 'w' mode in 3.x
    writer = csv.writer(f)
    writer.writerow(['params', 'pageviews'])
    for row in params_views:
        writer.writerow(row)

print('''
=====
A new CSV file named "results.csv" has been created or updated. Check it out!
=====
''')
