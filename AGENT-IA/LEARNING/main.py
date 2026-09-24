
import pandas as pd
path = "/Users/olivier/Desktop/python/AGENT-IA/LEARNING/07_Marvel_DC_Comic_Characters.csv"
reviews = pd.read_csv(path)
print(reviews.head(10))
print(reviews[['name', 'APPEARANCES']])

""" df = pd.read_csv("07_Marvel_DC_Comic_Characters.csv").head(2)
df['text'] = df.apply(lambda row: row.to_string(), axis=1)
print(df['text'][1]) """