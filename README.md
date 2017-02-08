# RSS >>> [publish]

## CAUTION!!!

If you clone this down, and run it with the proper credentials it may start sending tweets.
Before running, make sure line ~190 in scripts.py (`api.update_status(status=tweet_text`) is commented out.

## Introduction

This app takes an RSS feed and checks to see if there are any new stories in the list. If there are, then you can do stuff with those new stories. To start, I've set it up to send a tweet.

The theory is that you set this up on a cron to run every two minutes and it checks every two minutes for a new story.

`*/2	*	*	*	*	python main.py twitter-news`

The argument given after main.py corresponds to a directory which has a config file, an id file and log files.

## First time here?

* Clone repo to your machine
* Make virtualenv
* `pip install -e .` to install requirements listed in setup.py
* `pytest` and make sure tests are working correctly
* You may or may not need to create a directory called "logs" in the module directory, if so you'll get an error like this:
`IOError: [Errno 2] No such file or directory: '/Users/rdenton/github/registerguard/rssonpublish/twitter-sports/logs/twitter-sports.log'`
* Create secrets.json file that has this sort of structure:

```json
{
	"twitter-news": {
		"consumer_key": "asdf",
		"consumer_secret": "asdf",
		"access_token":"asdf",
		"access_token_secret":"asdf"
	},
	"bitly": {
		"access_token": "asdf"
	},
	...
}
```

Ok, now you're pretty close to being ready to run. This is the danger area where you want to make sure that line ~190 of scripts.py is commented out so that you don't spam tweet your followers.

### Walk you through

If you run `python main.py twitter-news` the script will go look for a `twitter-news` directory and child config.py file. This config file will set a number of variables needed in the script, including the link and url paramaters for the RSS feed.

From there, the script will go get the RSS feed you specified and loop over the entries.

For each entry, the script compares the id of the story to a list of ids that have already been tweeted. Of course, if this is your first time running the script, all of the ids will be new and it will want to tweet all of the stories in the feed. This is important when you push changes to live, as you don't want to spam followers. I would suggest running the script once with api.update_status() commented out to set a base list, then uncomment it when you set up the cron.

From here, the script tests to see if the headline is bad or not, does any fixing it needs to. If there is a headline and link, then it sends the tweet and writes the list of ids to the id file

### A note about logging

* Set logging level in main.py (DEBUG for testing, ERROR for go live)
* You can also uncomment `streamHandler()` to print to console

## Make a new module

To make an new instance, create a new directory and give it the necessary files.

The config file is technically the only one you need. (Maybe the logs directory too?) With the config file set up, your id file and log file should be created automatically.

## How to push changes live

* Make changes locally and commit/push to Github
* `ssh newsoper@wave.guardnet.com`
* `cd Envs/rssonpublish/rssonpublish`
* `git remote update && git status`
* `git pull && git status`

## Calculating length for trimming headline

For testing purposes, I am going off of current TweetDeck standards (AKA: I'm using the TweetDeck character count to see how long headlines can be).

### Characters left: 140

Let's start by removing the url, since that should be a constant length. While the Twitter documentations says that links are [20 characters at the most](https://dev.twitter.com/basics/tco#how-do-i-calculate-if-a-tweet-with-a-link-is-going-to-be-over-140-characters-or-not), TweetDeck has that count at 23. That means that no matter the length of the URL (full RG or bit.ly), that the link should only count for 23 characters in Twitter's eyes. We also need to account for one additional character for the space in front of the link. That leaves...

### Characters left: 116

Moving on, the publisher would like to include hashtags in these tweets. They will be either #rgnews or #rgsports for either process. This sorting will be handled by a conditional testing the script type. For consistency, let's assume that all hashtags will be at least 9 characters (although, some checking of type could change that). With one space in front, that leaves...

### Characters left: 106

Now, we have 106 characters left for the headline. We need to test to see if the length of the string is less than 106 characters, and if it is, cut it off and add an ellipsis on the end. The ellipsis should be a true one, not three periods, or else we'll lose two characters and go over. The whole thing looks like this:

[ headline ][...][ ][#hashtag][ ][url] = This is a really long headline that is too long for Twitter because of the extreme detail in the … #rgsports http://bit.ly/2kRz18N
[  < 106   ][ 1 ][1][   9    ][1][23 ] = headline ellipsis hashtag url

## Go-live email

All,

Please be aware that I have re-written the mechanism that sends automatic tweets for @registerguard and @rgsports. The main process will be the same: When an update is published to local news or sports a tweet with the headline and a link will be sent within 2 minutes. These tweets will now include the appropriate hashtag (#rgnews or #rgsports). If the length of the tweet becomes too long, the headlines will be trimmed and an ellipsis will be appended to the last visible word. Here's an example:

A long headline like this...
DA says teenager killed in Coos County wreck may have been racing another car before crashing into OSP trooper
...is too long with hashtag and shortlink so it is trimmed and tweeted out as:
DA says teenager killed in Coos County wreck may have been racing another car before crashing into OSP… #rgnews http://rgne.ws/2jVg6Zz

As always, if you see anything odd please let me know immediately.
