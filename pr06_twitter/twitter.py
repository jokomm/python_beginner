"""Twitter."""

import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    fastest_growing = {}
    for tweet in tweets:
        fastest_growing[tweet.retweets / tweet.time] = tweet
    return fastest_growing[max(fastest_growing)]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    tweets_by_popularity = sorted(tweets, key=lambda x: (x.retweets, -x.time), reverse=True)  # Use lambda functions when an anonymous function is required for a short period of time.
    return tweets_by_popularity

#Sort’ organizes elements in ascending order


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    tweets_with_hashtag = {}  # findall(): Kui tekstis on rohkem kui üks regulaaravaldisele vastav alamsõne saab kõikide vastete järjendi moodustada funktsiooniga findall()
    pattern = r"#\w+"  # \w : tähed, numbrid, alakriips, + : 1 või rohkem
    for tweet in tweets:  # r"string" on "raw" tüüpi string, mis tähendab, et kurakaldkriipsud("\") jäetakse teksti alles.
        find_hashtag = re.findall(pattern, tweet.content)  # word:\w\w\w. Regulaaravaldisele vastab täpne sõne "word:" ning sellele järgnevad 3 suvalist tähte.
        if find_hashtag:
                tweets_with_hashtag.setdefault(ht, []).append(tweet)
    return tweets_with_hashtag[hashtag]


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    hashtags_by_popularity = {}
    pattern = r"#\w+"
    for tweet in tweets:
        find_hashtag = re.findall(pattern, tweet.content)
        if not find_hashtag:
            continue
        else:
            for ht in find_hashtag:
                hashtags_by_popularity.setdefault(ht, []).append(tweet.retweets)
    print(hashtags_by_popularity)
    for k, v in hashtags_by_popularity.items():
        hashtags_by_popularity[k] = sum(v)
    print(hashtags_by_popularity)
    sorted_ht = sorted(hashtags_by_popularity.items(), key=lambda x: x[-1], reverse=True)
    print(hashtags_by_popularity)
    return [ht[0] for ht in sorted_ht]


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
