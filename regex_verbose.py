#! python3
# renameDates.py - Renames a bunch of files with US-style dates in the name to 
# have UK-style dates

import shutil
import os
import re

date_pattern = re.compile(
    r"""^(.*?)    # all text before the date
    ((0|1)?\d)-   # an optional 0 or 1 followed by a digit (month) then hyphen
    ([0-3]?\d)-   # an optional 0 to 3 followed by a digit (day) then hyphen
    ((19|20)\d\d) # 19xx or 20xx for the year
    (.*?)$        # other characters
    """, re.VERBOSE
)


# TODO implementation of program
