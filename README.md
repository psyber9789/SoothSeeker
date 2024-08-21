# SoothSeeker
Automated encoding/cipher/encryption solver for ARGs, or more generally just quickly figuring out the encoding of data automatically. Mostly to have fun, partly to be useful, and at the same time a good opportunity to hone my Python proficiency.

The inspiration came after joining in on the 'YouWillKnowEventually' (SK9752310) alternate reality game, which is based on cryptic music compliation videos posted to YouTube. Along with a growing community of players in the Discord server and Telegram channel, I've been trying my hand at figuring out the combinations of encodings, ciphers and encryptions the authors employ to obfuscate the fragments of the story as they are unveiled in new video uploads and documents released specifically on Disord and Telegram. It's been a lot of fun and I'll be continuing to join in as the project progresses.

Find out more: https://www.youtube.com/@youwillknoweventually

## Quick setup
```
cd ~
git clone https://github.com/psyber9789/SoothSeeker.git
cd SoothSeeker
python3 -m venv .
source ./bin/activate
pip install -r ./requirements.txt
```

### Run SoothSeeker
```
python main.py
```

## General plan / brain dump
Essentially it'll use a kind of optimising/evolutionary algorithm, to enumerate possible combinations of operations, and for each step there'll be a success score generated according to a set of heuristics to check for meaningful structure in the decryption to estimate if it has worked, needed as there are many key/iv collisions that produce noise output without explicit failure; for example, if output contains regular structure, such as a set of regularly delimited substrings of characters (like octal output, as one video had before), or whether the result contains grammatical structure.

The human factor will still be present, where we'll need to skim for clues and find where information is hidden. These are the real fun bits!

It will do stuff like:
- API to specify more and more intermediary transformations, their options and corresponding option value enumeration functions
- base-n decoding (including base-8 and base-16)
- decryptions - using a specified set of strings, of which we'll enumerate combinations that fit into particular total string lengths (like 8, 16, 24, 32), like a simple bin packing algorithm, generating all possible combinations of key/iv pairs across all modes, and attempting each decryption
- ASCII decoding
- ROT13 (Caesar shift) / substitution cipher - if the structure is grammatical, but there's no dictionary matches for words, this indicates a substition cipher. Could extend this to a generalisation that enumerates all possible substitution ciphers to cover ROT13 and others, measuring effectiveness using a similar dictionary heuristic
- etc., ad absurdum

For each possible enumeration of overall steps (up to some limit), there'll be a fitness function or sorts that produces a "success value", which will essentially be a score of how much the result meets a given set of criteria in the form of set of biases to optimise for some metric of form and structure. For example, if a bias is configured to optimise for presence of substrings that look like non-integer values in decimal notation, or the prescence of a single integer, or the presence of a few delineating characters, or uppercase letters only, or sentence case letters, then this will be likely to catch `MDAGS-31B` and `_Yuvar1_`.

Then, it'll order the results by the success metric and present them to the user. Each one will have printed alongside it a truncated text representation of the each intermediary state. Each will be given a corresponding identifier that will seed the same set of operations, so that specific combinations can be played with. The seed can just be an encoding of instructions with arguments, like a basic instruction set, to reproduce the same state. This way the intermediary states can be analysed more in depth and the set of transformations can be altered manually.

If, for each permutation, there are no sets of additional steps which increase the success metric, the permutation will be taken to be maximally successful. There will be some presumptious look-ahead, to account for where intermediary steps might temporarily decrease the success metric, but for the most part it should follow that each step progressively increases the success metric.

