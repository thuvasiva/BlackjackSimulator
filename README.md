## Blackjack Simulator

### Introduction
This repository contains the source code and tests for a Blackjack simulator, written for the BBC Software Engineering Graduate Scheme tech test. The repository makes use of the provided starter code and does not have any external dependencies outside of the Python standard library. Hence, running the source code and tests require the same setup and steps as for the starter code, as specified in the 'Running The Application' section.

### Overview of Application
- The source code implements a working Blackjack simulator where 1-4 players (and optional bot) compete to build the highest scoring hand without exceeding 21. Players take turns deciding to 'hit' (draw a card from the dealer) or 'stand' (receive no further cards). 

- If a player's score exceeds 21, they go bust and are eliminated. The player with the highest score at or below 21, after all players have either decided to stand, gone bust, or reached 21, is declared the winner. In the event of a tie for the highest score, all tied players are declared winners.  

- The game is text-based, with playing cards represented in text. Users are prompted for input during the game to set up the game and make decisions during gameplay. Users also have an additional option to enable a bot (computer-controlled player) to compete with them, which makes hit or stand decisions based on its score.

### Running The Application
- To run the source code:
    - If you have Python 3 installed:
        - Open a terminal window and navigate to the folder containing this `README.md`.
        - Type `python3 blackjack.py`
    - If that doesn't work, check your setup and download Python 3 if needed:
        - https://wiki.python.org/moin/BeginnersGuide/Download
    
- To run the tests:
    - From the same terminal window, type `python3 -m unittest discover test`.

    



