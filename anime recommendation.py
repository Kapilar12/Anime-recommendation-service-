import numpy as np
import pandas as pd
animes_df = pd.read_csv('E://anime.csv')
ratings_df = pd.read_csv('E://ratings.csv')
df = animes_df.merge(ratings_df, on='anime_id')
anime=input()
rcmd_animes = []
animedatabase = df[df['name'] == anime]\
            .sort_values(by='rating', ascending=False)
for user in animedatabase.iloc[:5]['u_id'].values:
    ranimes = df[df['u_id'] == user]
    ranimes = ranimes[ranimes['name'] != anime]\
                    .sort_values(by='rating', ascending=False)\
                    .iloc[:5]
    rcmd_animes.extend(list(ranimes['name'].values))
    
rcmd_animes = np.unique(rcmd_animes)
    
for i in rcmd_animes:
    print(i)
anime_genres_split = df[df['name'] == anime].iloc[0]['genre'].split(',')
scores = {}

for i in rcmd_animes:
    anim = df[df['name'] == i].iloc[0]
    anime_genres = anim['genre'].split('|')
    score = 0
    for k in anime_genres_split:
        if k in anime_genres:
            score += 1  
    scores[i] = score
rcmd_animes = sorted(scores, key=lambda x: scores[x])[::-1]
for animee in rcmd_animes:
    print(animee)
