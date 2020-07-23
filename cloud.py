import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# text_file = open("text1.txt", "w")
# n = text_file.write(text.lower())
# text_file.close()

dataset = pd.read_csv("review5.csv")
text = ''
for item in dataset['comment']:
    text = text + item
text = text.lower()

###########
stopwords = set(STOPWORDS)
stopwords.update(["vacuum", "shark", "the", "year", "even", "one"])
cloud = WordCloud(stopwords=stopwords).generate(text)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

cloud.to_file("wordcloud5.png")
