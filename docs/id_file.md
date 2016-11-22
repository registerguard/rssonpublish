The process by which we check to see if a story has been tweeted or not is a bit rudimentary but I think it works in the long run. Here are my thoughts.

So, we need something to keep track of what stories are new and should be tweeted versus the old stories since this is running on a cron every few minutes. Without something to keep track of this, all of the updates would get tweeted out every few minutes.

This script uses a plain text file with a text formatted like a Python list to keep track of these stories. When the script runs it checks to see what CMS IDs are in the RSS feed and compares them to the CMS IDs in our ID file. If there is an ID in the RSS feed that isn't in the ID file then it sends a tweet and the ID file gets replaced with the new list of IDs.

Every time the script runs, it re-writes the ID file with the most recent list of IDs. This could be problematic if the script breaks silently in the tweet process and the new ID is written to the file without being tweeted. However, I would rather a tweet not be sent, as opposed to a tweet being duplicated.

When a story is removed from the updates list, the ID is then removed from the ID file the next time the cron runs. This keeps things tidy. Then, if that story is added back into the updates list (this happens a few times a year) then the story is tweeted again. This isn't the end of the world and our stories probably should be tweeted more often anyway.

This ID file format is also nice because you don't need a DB, and we never have more than 10 updates so the file stays small.

Overall, I've seen very few issues with this set up. It's simple, but that's ok because it's hard to break.