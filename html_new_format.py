import pandas as pd

df=pd.read_csv("TimesNow_tweets.csv")
df.to_html("TimesNow_tweets.html")
