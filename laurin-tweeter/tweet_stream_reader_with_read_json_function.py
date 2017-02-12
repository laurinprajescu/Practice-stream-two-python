import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []
    tweets_file = open(tweets_data_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results  = read_json(tweets_data_path)
# create a dataframe
statuses = pandas.DataFrame()

#stores the text values
statuses['text'] = map(lambda status: status['text'], results)

#store the language values
statuses['lang'] = map(lambda status: status['lang'], results)

#sometimes there may not be a place listed in the tweet , so set  to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#']     = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))


print statuses['python'].value_counts()[True]
print statuses['java'].value_counts()[True]
print statuses['c#'].value_counts()[True]
print statuses['ruby'].value_counts()[True]


tweets_by_python = statuses['python'].value_counts()[True]
tweets_by_java = statuses['java'].value_counts()[True]
tweets_by_csharp = statuses['c#'].value_counts()[True]
tweets_by_ruby = statuses['ruby'].value_counts()[True]



slices = [tweets_by_python, tweets_by_java, tweets_by_csharp, tweets_by_ruby]
programming_languages = ['python' , 'java', 'c#', 'ruby']
cols = ['c', 'm', 'r', 'b']
plt.pie(slices,
        labels=programming_languages,
        colors=cols,
        startangle=90,
        shadow=True,
        autopct='%1.1f%%')

plt.show()


