
import sys
import tweetutil
import re

 

def getStateSentiment(initial_state_sentiment):
    state_sentiment = {}
    for key, value in initial_state_sentiment.items():
        average = sum(value) / len(value)
        state_sentiment[key] = average
    
    return state_sentiment


def getStateSentimentMap(scores, tweet_jsons):
    initial_state_sentiment = {}
    for tweet_json in tweet_jsons:
        score = 0
        if tweet_json.get('place') and tweet_json['place']['country_code'] == 'US' and tweet_json.get('text'):
            city_state = tweet_json['place']['full_name'].encode('utf8').split(', ')
            tweet_text = tweet_json['text'].encode('utf8').split()
            for word in tweet_text:
                if re.match("^[A-Za-z0-9_-]*$", word):
                    score += scores.get(word, 0)
            
            initial_state_sentiment.setdefault(city_state[1], []).append(score)
    
    return initial_state_sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = tweetutil.initScores(sent_file)
    tweet_jsons = tweetutil.readTweetsAsJSON(tweet_file)

    initial_state_sentiment = getStateSentimentMap(scores, tweet_jsons)

    state_sentiment= getStateSentiment(initial_state_sentiment)

    print max(state_sentiment, key=state_sentiment.get)

if __name__ == '__main__':
    main()
