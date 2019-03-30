import twitter
from twit_creds import *

# Credentials used to authenticate twitter access
api = twitter.Api(consumer_key=api_key,
                  consumer_secret=secret_key,
                  access_token_key=access_token,
                  access_token_secret=at_secret)

def twitterSearch():
    # gets 100 (the max) english tweets that contain the given term
    # and returns them in a .json form.
    # Slices the .json to grab just the text from the tweet body.
    search = api.GetSearch(term="searchTerm", count=100, lang="en", return_json=True)
    search_words = search['statuses'][0]['text'].split(' ')

    return search_words

def tickerFinder(string):
    # Takes a string of text and locates any stock tickers inside

    possible_stocks = []
    for i in string:
        if len(i) > 0 and i[0] == '$' and len(i) < 6:
            possible_stocks.append(i)

    # List comprehension that makes a list from possible_stocks that
    # only includes stock tickers by getting rid of any terms that have
    # numbers after the first character (a dollar sign)
    stock_list = [i for i in possible_stocks if i[1:].isalpha() == True]

    print("List Of Stock Tickers:")
    print(stock_list)

# ACTIVATION
if __name__ == '__main__':
    tickerFinder(twitterSearch())
