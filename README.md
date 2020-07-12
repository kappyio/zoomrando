# zoomrando
Random Zoom grid position based on participants, screens, rows, columns.
Currently runs on the command line. Written in Python 3.

<h1>How to use:</h1>
<p>If you'd like to use this, you have to download zoomrando.py. It requires
you to <a href="https://docs.python-guide.org/starting/install3/osx/">have Python3 installed on your computer</a> as well. You can then use a terminal application, like "Terminal" in
MacOS to <a
href="https://smallbusiness.chron.com/execute-file-macbook-terminal-49381.html">run the zoomrando.py program</a> as shown in the example below.</p>

<p>There are probably a million better ways to do this, especially if you have an
account with API access that would allow you to access the participants
programmatically. But if you don't have programmatic access to a meeting, this
is one way to pick a random participant using Zoom's "Gallery View", which
presents you with a grid of participants Brady Bunch or Hollywood Squares
style.
</p>


<p>
Note: Generally there are always 5 rows in column view. Columns can vary, it
seems. 
</p>

<p>
Also note: If you have a meeting with 25 people and you're in gallery view, there should be 1 screen with 5 rows and 5 columns = 25 people. But if a 26th person joins, you'll have two screen with 25 people in each screen. 
</p>

<p>
Huh? 
</p>

<p>
Zoom shifts participants around in such a way that in grid view there will always be 25 participants.  So no participant has a fixed place on the grid. Thus you might get repeats, even with random number generators if you use this grid system.
</p>

<p>
Maybe I can write a plugin to do this, since I don't know if they'd bother with
a feature request to pick a random participant. This is something quick and dirty I
wrote to help me with an upcoming meeting.
<p>


Get help / usage info: 

    ./zoomrando.py -h

    usage: zoomrando.py [-h] [-n NUM] participants rows cols

    Produce a list of random grid coordinates for participants in a zoom meeting.
    Uses Zoom's "Gallery View".
    
    positional arguments:
      participants       How many participants are in the meeting?
      rows               How many rows do you see in gallery view?
      cols               How many columns do you see in gallery view?
    
    optional arguments:
      -h, --help         show this help message and exit
      -n NUM, --num NUM  How many results would you like returned? Default
                     behavior is to return all results

<p>
Example Run. Imagine you're in a meeting with 146 participants. You're in grid
view and you see 5 rows and 4 columns. Here's how you'd generate a random list
of participants:</p>

    ./zoomrando.py 146 5 4
    There are 146 participants across 8 screens, 5 rows, and 4 columns
    Screen: 5, Row: 5, Column: 3
    Screen: 7, Row: 2, Column: 2
    Screen: 6, Row: 5, Column: 4
    Screen: 8, Row: 5, Column: 2
    Screen: 1, Row: 3, Column: 4
    Screen: 8, Row: 2, Column: 1
    Screen: 1, Row: 3, Column: 1
    ... etc., etc.

Go to screen 5, row 5, and column 3 and the participant in that square is your first rando. 
Rinse and repeat. Hilarity will ensue.

<p>
Just give me 1 random participant

    ./zoomrando.py -n 1 146 5 4
    There are 146 participants across 8 screens, 5 rows, and 4 columns
    Screen: 1, Row: 3, Column: 1
</p>
