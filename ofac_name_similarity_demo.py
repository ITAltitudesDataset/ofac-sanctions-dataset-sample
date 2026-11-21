"""Educational entity-name similarity demo. Not a sanctions-screening system."""
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / 'ofac_primary_50.csv', dtype=str).fillna('')
df = df[df['SDN_Name'].str.strip().ne('')].reset_index(drop=True)
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4), lowercase=True)
X = vectorizer.fit_transform(df['SDN_Name'])
model = NearestNeighbors(n_neighbors=min(6, len(df)), metric='cosine', algorithm='brute').fit(X)

# Holdout-like query constructed from an existing name; demonstration only.
query = df.loc[0, 'SDN_Name'].replace(' ', '')
q = vectorizer.transform([query])
distances, indices = model.kneighbors(q)
results = pd.DataFrame([{'Query':query, 'Entity_ID':df.loc[i,'Entity_ID'],
    'Matched_Name':df.loc[i,'SDN_Name'], 'Similarity_Score':round(float(1-d),4)}
    for d,i in zip(distances[0],indices[0])])
results.to_csv(ROOT / 'ofac_name_similarity_results.csv', index=False)
print('Training rows:',len(df)); print('Query:',query); print(results.to_string(index=False))
print('\nScores are text similarities, NOT identity confidence or compliance decisions.')
