import pandas
import time
import sys
import csv

race_id = 0
df = pandas.read_csv('results.csv')
# for i, row in df.iteritems():
for i, v in df.iterrows():
  race_id = v['id']
  str_race_id = str(race_id)

  list = [int(v['no']), v['odds']]
  list2 = [int(v['no']), v['order']]
  with open('odds/' + str(race_id) + '_' + str_race_id[:4] + '.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(list)
  with open('result/' + str(race_id) + '_' + str_race_id[:4] + '.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(list2)
