import time

import numpy as np
import praw
from textblob import TextBlob

start_time = time.time()

# あなたのAPIキー情報
client_id = "W51EzAo4Ei6q9kpHIcU4xA"
client_secret = "JbOq2nhKJMxqgI9nQ2LJkFApTD530Q"
user_agent = "windows:my_app:v1.0 (by /u/Routine_Show719)"

# PRAWインスタンスを作成
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# ビットコインに関するサブレディットを取得
subreddit = reddit.subreddit("Bitcoin")

polarity_list = []
subjectivity_list = []

# サブレディットの新しい投稿を取得
for submission in subreddit.new(limit=100):
    # TextBlobオブジェクトを作成
    blob = TextBlob(submission.title)
    # 感情分析の結果を取得
    polarity, subjectivity = blob.sentiment
    polarity_list.append(polarity)
    subjectivity_list.append(subjectivity)

# ポジティビティ（極性）と主観性の平均と分散を計算
polarity_np = np.array(polarity_list)
subjectivity_np = np.array(subjectivity_list)

strp = "Polarity - Average: " + str(np.mean(polarity_np)) + " Variance: " + str(np.var(polarity_np))

strs = "Subjectivity - Average: " + str(np.mean(subjectivity_np)) + " Variance: " + str(np.var(subjectivity_np))

print(strp)
print(strs)

with open('data/data.txt', 'a') as f:
    f.write(strp+'\n')
    f.write(strs+'\n')
    f.write('\n')

end_time = time.time()

print("elapsed time="+str(end_time-start_time))
