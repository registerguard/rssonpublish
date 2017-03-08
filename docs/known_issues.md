# Known issues

* Tweets that get sent with no headline
  * *This is no longer an issue, however since Feb. 2017. Now there is checking for the length of the headline and also for things like "herey". Unfortunately, some Head goes here tweets still get out, but no missing headline tweets get out.*
  * This is so annoying because we should never have a story posted without a headline but it happens at least once a week. The solution would be to do a regex search on feed_title in `utilities/tweet.py` that checks for strings with multiple periods in a single string like `cr.story-slug.1122`. Then figure out how to not include that CMS ID in the file. 
  * This could be a good opportunity to change the way we handle the ID file by appending the list as opposed to big footing the whole thing. But that presents it's own issues.
  * As of right now, this is a nice notification to me (I have Twitter notifications set up on my phone) and I can catch it quick and also deal with the story quickly. The problem is when this happens on the weekends and no one fixes it for hours...