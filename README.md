Coming soon...

Notes:

* Set logging level in scripts.main() (DEBUG for testing, ERROR for go live)
  * You can also uncomment `streamHandler()` to print to console
* Comment out line in scripts.sendit() (line 99?) where `api.update_status(status=tweet_text)` to make ready for go live
