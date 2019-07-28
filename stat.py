import os
import re


dirs = list()

statName = re.compile('\[.*\]')
timeStudied = re.compile('([0-9]?\.?[0-9]?\s?hours)')

statDict = dict()

for elem in os.listdir():
    if elem[:1] == '.': #if it is secret folder
        continue
    if os.path.isdir(elem):
        dirs.append(elem)

for dir in dirs:

    files = os.listdir(dir)
    for file in files:
        print(dir + '/' + file)
        f = open(dir + '/' + file, 'r')
        text = f.readlines()
        f.close()
        for line in text:
            stat = statName.findall(line)
            hours = timeStudied.findall(line)  

            if len(stat) != 0:
                hours[0] = hours[0].replace(' ', '')
                hours[0] = hours[0][:-5]

                if stat[0] not in statDict:
                    statDict[stat[0]] = float(hours[0])
                else:
                    statDict[stat[0]] += float(hours[0])

output = 'Since 2019-07-26\n'

for stat in statDict:
    output += '### {} : {} hours\n\n'.format(stat, statDict[stat])
    
print(output)
f = open('stat.md', 'w+')
f.write(output)
f.close()
