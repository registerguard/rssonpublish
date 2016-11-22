# Basic flow of a single news story tweet

1. Cron triggers `main/tweet_news.py`
1. `main/tweet_news.py` sets vars specific to news and calls the generic `checknsend()` from `utilities/onpublish.py`
    * `checknsend` is a general function that can be called by any main script and requires a base url, payload parameters to populate the URL GET arguments, and the name of the ID file you want to store your IDs into.
1. `utilities/onpublish.py` does a number of things and is one of the central points of the system; first it calls `getrss()` and passes in the url and payload 
1. `getrss()` is a tertiary script that uses the [Requests](http://docs.python-requests.org/en/master/) and [feedparser](https://pythonhosted.org/feedparser/) to get and parse the RSS feed from DT and returns it to `checknsend()`
1. `checknsend()` then loops through the feed and checks to see if the CMS IDs in the feed match up to CMS IDs that have already been processed. If the ID already in the ID file the script skips it, otherwise it proceeds to send the tweet.
    * Of course, the first time you run this, none of the IDs have been processed so it would send a flutter of tweets. I would advise commenting out the `api.update_status()` line in `utilities/tweet.py` so that you don't spam followers. That's also just a good thing to do for testing. After you've run it once, it should only trigger when there's a new story in the RSS feed. One way to test is by manually manipulating the ID file. See: [docs/id_file.md](https://github.com/robertdenton/python-skeleton/blob/master/docs/id_file.md) for more.
    * The script also checks to see if that file exists before doing any of this, if it does not exist, it will make it for you.
1. Next, `checknsend()` checks to make sure there is both a story title and a url, if both of these exist it calls `sendit()` from `utilities/tweet.py` and passes in the long url and title.
1. `sendit()` first gets the proper Twitter API credentials using the `getSecret()` method from `utilities/secrets.py` and passes in the ID of the credential set we want.
1. `getSecret()` goes into your `secrets.json` file and returns a dictionary that we can parse back in `sendit()`
1. We use those credentials to authenticate against the Twitter API and login.
1. Now we call `getURL()` from `utilities/bitly.py` and pass in the long url.
1. `getURL()` uses `getSecret()` to get our bitly credentials, we login to bitly and convert the long url to a short one.
    * If there is an issue with bitly `getURL()` will simply return the long url which will still allow the program to send the tweet, it's just not ideal.
    * **NOTE:** We use a vanity short url but sometimes we exceed the amount of free vanity urls we get from bitly near the end of the month and bitly will return `http://bit.ly/asd123` urls instead of `http://rgne.ws/asd123` urls. This is OK and the test will pass on either url.
1. With the short url in hand, `sendit()` will format the `tweet_text` string to have the title and short url then try to send it.
    * This is where you want to comment out `api.status_update` during testing. I use the `print tweet_text` as a check.
1. Now we jump back up to `checknsend()` where the ID file is replaced with updated IDs and the program completes.
