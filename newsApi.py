import requests
from textblob import TextBlob
import numpy as np

# News APIキー
api_key = "0081399fcf0045e1b45b0fe9fda99c3e"

# ビットコインに関するニュース記事を取得
url = (f"https://newsapi.org/v2/everything?q=Bitcoin&language=en&apiKey={api_key}")
response = requests.get(url)
data = response.json()

polarities = []
subjectivities = []

for article in data['articles']:
    # 記事のタイトルを取得
    title = article['title']
    # TextBlobオブジェクトを作成
    blob = TextBlob(title)
    # 感情分析の結果を取得
    polarity, subjectivity = blob.sentiment
    polarities.append(polarity)
    subjectivities.append(subjectivity)

# ポジティビティと主観性の平均と分散を計算
polarity_mean = np.mean(polarities)
polarity_var = np.var(polarities)
subjectivity_mean = np.mean(subjectivities)
subjectivity_var = np.var(subjectivities)

print(f'Polarity Mean: {polarity_mean}, Variance: {polarity_var}')
print(f'Subjectivity Mean: {subjectivity_mean}, Variance: {subjectivity_var}')