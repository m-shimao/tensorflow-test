import pandas
import time
pandas.set_option('line_width', 200)


# http://db.netkeiba.com/からデータ取得
for year in range(2004, 2005):
  for month in range(1,12):
    for day in range(1,31):
      for num in range(0, 1500):
        race_id = str(year) + '{0:02d}'.format(month) + '{0:02d}'.format(day) + '{0:04d}'.format(num)
        url = 'http://db.netkeiba.com/race/' + race_id
        fetched_dataframes = pandas.io.html.read_html(url)
        if len(fetched_dataframes) == 0:
          continue
        df = fetched_dataframes[0]
        # race_id追加
        df['race_id'] = race_id

        # csv書き込み
        out = 'results/' + race_id + '.csv'
        df.to_csv(out, header=None, index=None)
      time.sleep(1)
