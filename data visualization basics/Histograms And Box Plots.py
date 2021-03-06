## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

## 2. Frequency Distribution ##

import pandas as pd
import matplotlib.pyplot as plt
fandango_scores = pd.read_csv('fandango_scores.csv')
fandango_distribution = fandango_scores['Fandango_Ratingvalue'].value_counts().sort_index()

imdb_distribution = fandango_scores['IMDB_norm'].value_counts().sort_index() # sort the df by index

print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig,ax = plt.subplots()
ax.hist(fandango_scores['Fandango_Ratingvalue'],range=(0,5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(fandango_scores['Fandango_Ratingvalue'],bins = 20, range = (0,5))
ax1.set_ylim(0,50)
ax1.set_title('Distribution of Fandango Ratings')

ax2.hist(fandango_scores['RT_user_norm'],bins = 20,range = (0,5))
ax2.set_ylim(0,50)
ax2.set_title('Distributin of Rotten Tomatoes Ratings')

ax3.hist(fandango_scores['Metacritic_user_nom'],bins = 20,range = (0,5))
ax3.set_ylim(0,50)
ax3.set_title('Distribution of Metacritic Ratings')

ax4.hist(fandango_scores['IMDB_norm'],bins = 20,range = (0,5))
ax4.set_ylim(0,50)
ax4.set_title('Distribution of IMDB Ratings')

plt.show()

## 7. Box Plot ##

import pandas as pd
import matplotlib.pyplot as plt
fandango_scores = pd.read_csv('fandango_scores.csv')
fig,ax = plt.subplots()
ax.boxplot(fandango_scores['RT_user_norm'])
ax.set_ylim(0,5)
ax.set_xticklabels(['Rotten Tomatoes'])
plt.show()
             

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig,ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols,rotation = 90)
ax.set_ylim(0,5)
plt.show()
