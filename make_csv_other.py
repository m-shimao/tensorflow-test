import pandas
import time
import sys
import csv

race_id = 0
df = pandas.read_csv('other_results.csv')
# for i, row in df.iteritems():
count = 1
prev_ymd = 0
prev_race = 0
for i, v in df.iterrows():
  if prev_ymd != 0 and prev_ymd != v['ymd']:
    count += 1
  if prev_race != 0 and prev_race != int(v['race']):
    count += 1
  prev_ymd = v['ymd']
  prev_race = v['race']
  race_id = '{0:06d}'.format(count)
  ymd = str(v['ymd'])

  list = [int(v['no']), '{:.2f}'.format(v['odds'])]
  list2 = [int(v['no']), int(v['order'])]
  with open('odds/' + str(int(v['race'])) + race_id + '_' + ymd[:4] + '.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(list)
  with open('result/' + str(int(v['race'])) + race_id + '_' + ymd[:4] + '.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(list2)
