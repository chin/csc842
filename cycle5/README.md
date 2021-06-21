# Cycle 5: Pseudo Random Path Finder
## Motivation
Initially I was trying to figure out psudorandom number generation in such a fashion that I went down a rabbit hole and instead of being able to successfully grab the numbered values in the url of a particular search engines pseudo random website generator, I decided to try my hand at generating a random path myself. Basically it follows what a kid would do (most random thing I could think of), find page and click thing for x many pages available. If it can't reach the randomly chosen x number of things to click, then it errors out. If it goes all the way then it stops after returning the last url.

## Python modules
- random
- re
- requests
- time
- sys

## Future Work
- Refactor, refactor, refactor. This code is pretty ugly and happenstance since I didn't know what the technical name was to google starter code, so I definitely need to make it prettier.
- Figure out what the technical name for making a list of random urls is.
- Command line variables so the user can pick all "random" ranges
- Better error checking
- Contingency to restart script if no path of depth x is found
- Dynamically find the rot urls
