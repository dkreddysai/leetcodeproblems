import pandas as pd
data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
invalid_tweet=tweets[tweets['content'].str.len()>15]
result= invalid_tweet[['tweet_id']]
print(result)