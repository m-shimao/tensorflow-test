import pandas
import time


# http://db.netkeiba.com/からデータ取得
for year in range(2007, 2013):
  for month in [1, 3, 5, 6]:
    for day in [1, 2, 3, 5, 6]:
      for num in range(1, 10):
        for race in range(1, 15):
          race_id = str(year) + '{0:02d}'.format(month) + '{0:02d}'.format(day) + '{0:02d}'.format(num) + '{0:02d}'.format(race)
          url = 'http://db.netkeiba.com/race/' + race_id
          fetched_dataframes = pandas.io.html.read_html(url)
          print(url)
          if len(fetched_dataframes) == 0:
            continue
          df = fetched_dataframes[0]
          # race_id追加
          df['race_id'] = race_id

          # csv書き込み
          out = 'results/' + race_id + '.csv'
          df.to_csv(out, header=None, index=None)
