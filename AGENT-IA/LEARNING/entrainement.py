import pandas as pd

df = pd.read_csv("07_Marvel_DC_Comic_Characters.csv")

print(len(df))
print(df['APPEARANCES'].isnull().sum())
df = df[pd.notnull(df['APPEARANCES'])]


df['question'] = df.apply(lambda row: f"Combien d'apparitions a {row['name']} ?", axis=1)
df['reponse'] = df['APPEARANCES'].astype('int').astype('str')
print(df[['question', 'reponse']].head(2))

df[['question', 'reponse']].to_json(
    "dataset_entrainement.jsonl",
    orient='records',
    lines=True,
    force_ascii=False
)






