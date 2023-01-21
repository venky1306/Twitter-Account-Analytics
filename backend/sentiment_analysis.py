from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(sentence):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence)
    return(vs)
