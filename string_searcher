# I wrote this because I needed to understand the target redirect URL from a bunch of pages. Not the best, but it did the job.
# This script has not try-catch so it will crash when not finding a URL, expected expressions, etc. I'll improve someday when needed. 

from urllib.request import urlopen
import re
import pandas as pd
import time


l = 0

#Download the list of links URLs and format appropriately.
links = [ 
"http://site.com/page1"
,"http://site.com/page1"
]
redirects = []
UA_list = []


for link in links:
    l=l
    f = urlopen(link)
    print ('fetching link...')
    myfile = f.read().decode()
#for_debug     print(myfile)
    type(myfile)

    url = re.search('http(.?):(.*?)\'',myfile)
    url = url.group(0)
    url = url[:-1]
#for_debug     print (url)
    redirects.append(url)

    UA = re.search('UA-(.*?)\'',myfile)
    UA = UA.group(0)
    UA = UA[:-1]
#for_debug     print (UA)
    UA_list.append(UA)
#for_debug     time.sleep(1) #for troubleshooting

# print (links)    
# print (redirects)
# print(UA_list)

df = pd.DataFrame({
    "links": links,
    "UA": UA_list,
    "redirects": redirects,
})

# print(df.to_string())



export_csv = df.to_csv (r'C:\<FILE PATH>\export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
print('Done!')
