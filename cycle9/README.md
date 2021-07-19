# Cycle 9: Random Password Generator v2
## Usage
python pwgen.py -l # 
python pwgen.py -t bytes
python pwgen.py -t hex
python pwgen.py -t url

## Motivation
A coworker has been complaining about generating passwords that match up to complexity standards in each of the environments we work in. Obviously, we should also use different passwords for each account type in use. I told them I'd script a password generator for their personal use. Based on the feedback I got from my classmates, I thought I would put out a version 2 free of infinite loops and more possibilities for password types. I was able to clean up the existing code pretty significantly in terms of functionality/error checking and added the use of token generation which is the secrets module 'most used'. I also attempted to time the length of time it takes to return the password generated through length the old fashioned cycle 7 way.

## Python modules
- getopt
- secrets
- string
- sys
- time

## Future Work
- Define and Control the exact number of complexities not just min for "at least as many"
- Take user input to generate pseudo-random pwds based on input phrases
- GUI!?
