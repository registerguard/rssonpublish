Coming soon...

Notes:

* For installation see: https://github.com/robertdenton/python-skeleton
  * clone, mkvirtualenv, `pip install -e .` (install from setup.py), `pytest`
* Set logging level in scripts.main() (DEBUG for testing, ERROR for go live)
  * You can also uncomment `streamHandler()` to print to console
* Comment out line in scripts.sendit() (line 99?) where `api.update_status(status=tweet_text)` to make ready for go live

Calculating length:

For testing purposes, I am going off of current TweetDeck standards (AKA: I'm using the TweetDeck character count to see how long headlines can be).

## Characters left: 140

Let's start by removing the url, since that should be a constant length. While the Twitter documentations says that links are [20 characters at the most](https://dev.twitter.com/basics/tco#how-do-i-calculate-if-a-tweet-with-a-link-is-going-to-be-over-140-characters-or-not), TweetDeck has that count at 23. That means that no matter the length of the URL (full RG or bit.ly), that the link should only count for 23 characters in Twitter's eyes. We also need to account for one additional character for the space in front of the link. That leaves...

## Characters left: 116

Moving on, the publisher would like to include hashtags in these tweets. They will be either #rgnews or #rgsports for either process. This sorting will be handled by a conditional testing the script type. For consistency, let's assume that all hashtags will be at least 9 characters (although, some checking of type could change that). With one space in front, that leaves...

## Characters left: 106

Now, we have 106 characters left for the headline. We need to test to see if the length of the string is less than 106 characters, and if it is, cut it off and add an ellipsis on the end. The ellipsis should be a true one, not three periods, or else we'll lose two characters and go over. The whole thing looks like this:

[ headline ][...][ ][#hashtag][ ][url] = This is a really long headline that is too long for Twitter because of the extreme detail in the … #rgsports http://bit.ly/2kRz18N
[  < 106   ][ 1 ][1][   9    ][1][23 ] = headline ellipsis hashtag url


