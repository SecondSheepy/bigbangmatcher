# bigbangmatcher

A Python script to read from a Google Sheet and return a list of exchange matches.

## requirements

* Authenticate into someone's Google account
* Read directly from a given Google Sheets file
* The tab to match from should be selectable.
* Matching: a person should recieve their highest non-taken choice, based on ranked choice.
* No one should get their second choice if their first choice is available and no one else requested it as their first choice.
* Ties should be resolved by whichever person submitted their request first.
* Ties should only occur if two or more people requested the same option as the same ranked choice.
* No priority is given to people who have made fewer choices.
* There should then be an output: a new tab showing who has matched to what, and a new sheet showing any unmatched options and unmatched people.
* OPTIONAL: since we're logged into someone's Google account anyway, prompt whether they want to send an automatic email warning someone they're unmatched.
* OPTIONAL: GUI/UI, rather than a simple command line tool.
