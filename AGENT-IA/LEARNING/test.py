import pandas as pd

# Une toute petite table : 2 lignes, 2 colonnes
df = pd.DataFrame({
    'name': ['Spider-Man', 'Batman'],
    'publisher': ['Marvel', 'DC']
})

print("--- AVANT ---")
print(df)

df['text'] = df.apply(lambda row: row.to_string(), axis=1)

print("--- APRES ---")
print(df)
print("--- CONTENU DE LA CASE 0 ---")
print(df['text'][0])