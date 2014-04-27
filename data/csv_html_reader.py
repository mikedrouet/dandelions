#!/usr/bin/python

import sys
import re
import csv
import os

textfile="/Users/michaeldrouet/migrasuburbs/ACS_11_5YR.csv"
##textfile = "txt.txt"
##f = open(textfile,"w")
##for line in open("txt.out","r"):
##    if re.search('~', line):
##        f.write(line)

##f.close()

data = csv.reader(open(textfile,"rU"),delimiter=',')

htmlfile = open('./korean_village_census.html',"w")

htmlfile.write('<!DOCTYPE html>\n')
htmlfile.write('<html>\n')
htmlfile.write('<body>\n')
htmlfile.write('<table border="1" width="100%">\n')


rownum=0;

for row in data:
    if rownum == 0:
        htmlfile.write('<tr>') # write <tr> tag
        for column in row:
            htmlfile.write('<th>' + column + '</th>') # write header columns
        htmlfile.write('</tr>\n') # write </tr> tag
    else: # write all other rows
        colnum = 1
        if rownum % 2 == 0:
            htmlfile.write('<tr class="color1">')
        else:
            htmlfile.write('<tr class="color2">')
        #htmlfile.write('<tr>')
        for column in row:
            htmlfile.write('<td>' + column + '</td>')
            colnum += 1
        htmlfile.write('</tr>\n')
    rownum += 1
    print row

# write </table> tag
htmlfile.write('</table>\n')
htmlfile.write('</body>\n')
htmlfile.write('</html>\n')

##for item in items:
##  print item