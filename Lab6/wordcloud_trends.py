import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# load Kaggle dataset
data = pd.read_csv("2021_August_all_trends_data.csv")

# keep only the columns we need
trends = data[['trend_name', 'tweet_volume']]

# remove rows where tweet_volume is missing
trends = trends.dropna()

# convert tweet_volume to integer
trends['tweet_volume'] = trends['tweet_volume'].astype(int)

# create dictionary of word frequencies
freq = dict(zip(trends['trend_name'], trends['tweet_volume']))

# generate word cloud with default background_color
wordcloud = WordCloud().generate_from_frequencies(freq)

# save the image
wordcloud.to_file("twitter_wordcloud.png")

# display it
plt.imshow(wordcloud)
plt.axis("off")
plt.show()