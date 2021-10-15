import os

import labelimg_xml

title, table = labelimg_xml.read_xml(os.getcwd() + '/', 'sample.xml')

print(table)
sizes = []
for cell in table:
    if cell[0] == 'RBC':
        size = cell[3] + cell[4] - cell[1] - cell[2]
        print(cell, 'len :', size)
        sizes.append(size)

size_stats = [min(sizes), max(sizes), int(sum(sizes)/len(sizes))]

print(size_stats)