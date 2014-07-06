import json

def lines(fp):
    print str(len(fp.readlines()))

def printArray(array):    
    for t in array:
        print t
 
def printTermScore(new_terms):
    for w in new_terms:
        print w, new_terms[w]         

def initScores(words):
    scores = {}
    for line in words:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    return scores

def readTweetsAsTexts(tweets):
    tweet_text = []
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text'].lower()
            tweet_text.append(text.encode('utf-8'))
    
    return tweet_text

def readTweetsAsJSON(tweets):
    tweet_json = []
    for line in tweets:
        tweet = json.loads(line)
        tweet_json.append(tweet)
    
    return tweet_json

def getTweetSentiment(scores, tweet):
    sentiment = 0
    breakdown = tweet.split()
    for word in breakdown:
        if scores.has_key(word):
            sentiment = sentiment + scores[word]
    
    return sentiment