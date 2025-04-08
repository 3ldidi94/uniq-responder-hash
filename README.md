# uniq-responder-hash

Just a quick script to parse the Responder log files to output usernames captured and filter captured hashes to only one per user.

The main objective is to avoid loosing time when cracking because hashcat will try to crack several hashes values for the same password as it is the same user.

Also it can provide a nice view of all users captured, by default it does not show the computer account.
