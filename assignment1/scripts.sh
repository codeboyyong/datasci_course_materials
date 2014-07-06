#1
python twitterstream.py > output.txt
head -n 20 output.txt > problem_1_submission.txt

#2
python tweet_sentiment.py AFINN-111.txt problem_1_submission.txt

#3
python term_sentiment.py AFINN-111.txt  problem_1_submission.txt

#4
python frequency.py problem_1_submission.txt

#5
python happiest_state.py AFINN-111.txt problem_1_submission.txt

#6
python top_ten.py problem_1_submission.txt