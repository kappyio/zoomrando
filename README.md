# zoomrando
Random Zoom grid position based on participants, screens, rows, columns

Get help / usage info: 

    ./zoomrando.py -h
    usage: zoomrando.py [-h] participants rows cols
    
    Produce a list of random grid coordinates for participants in a zoom meeting.
    Uses Zoom's "Gallery View".
    
    positional arguments:
      participants  How many participants are in the meeting?
      rows          How many rows do you see in gallery view?
      cols          How many columns do you see in gallery view?
    
    optional arguments:
      -h, --help    show this help message and exit

Example Run: 

    ./zoomrando.py 146 5 5
    There are 146 participants across 6 screens, 5 rows, and 5 columns
    Screen: 2, Row: 5, Column: 5
    Screen: 2, Row: 1, Column: 5
    Screen: 3, Row: 5, Column: 2
    Screen: 4, Row: 3, Column: 2
    Screen: 5, Row: 4, Column: 4
    Screen: 2, Row: 4, Column: 1
    Screen: 4, Row: 5, Column: 1
    Screen: 2, Row: 5, Column: 3
    ... etc. etc.
