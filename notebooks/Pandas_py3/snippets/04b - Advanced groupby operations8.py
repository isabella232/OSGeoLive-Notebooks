titles.groupby(titles.year // 10 * 10).size().plot(kind='bar')