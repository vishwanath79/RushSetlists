# API sourced from setlist.fm
# Source: <a href="http://www.setlist.fm/>concert setlists on setlist.fm</a> 


import requests
from xml.etree import ElementTree as ET
import codecs
import glob
# query API and pull down all setlists
# , 'apikey':'69cf3056-b765-4aae-a589-ea47afc41c66'
for i in range(1,100):
    setlistPayload= {'artistMbid': '534ee493-bfac-4575-a44a-0ae41e2c3fe4', 'p':i}
    setlist = requests.get("http://api.setlist.fm/rest/0.1/artist/534ee493-bfac-4575-a44a-0ae41e2c3fe4/setlists", params=setlistPayload)
    content =setlist.text
    #b =content.encode('ascii', 'ignore')
    #print b
    # Save each page into separate xml file
    with open("rush"+ str(i)+".xml", "w") as f:
        f.write(b) 
# Search for all cml files
xml1_files = glob.glob("*.xml")
# Append xml to one file
with open("RushFinal.xml", "wb") as outfile:
    for g in xml1_files:
        with open(g, "rb") as infile:
            outfile.write(infile.read())
# Remove xml headers
final = 'RushFinal.xml'
h = open(final)
output = []
for line in h:
    if not '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' in line:
        output.append(line)
h.close()
h = open(final, 'w')
h.writelines(output)
h.close()
# Note may have to append parent tag on xml for conversion to xls