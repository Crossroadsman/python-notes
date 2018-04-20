# Convenience functions etc for working with dates
import datetime

# See: https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior

# This is a dictionary of named datetime formats
datetime_formats = {
    'iso 8601 full': '%Y-%m-%dT%H:%M:%S.%f%z', # 2018-04-19T19:00:05.012345-07:00
    'iso 8601 date': '%Y-%m-%d', # 2018-04-19
    'US long' : '%B %d, %Y', # April 19, 2018
    'US short': '%m/%d/%y', # 04/19/18
    'UK long' : '%d %B %Y', # 19 April 2018
    'UK short': '%d/%m/%y', # 19/04/18
    'day name': '%A', # Thursday
    'microsecond': '%f' # 000001
}

# This is a dictionary that sets which date format should be used for which
# interface elements.
# This way, the UI code only shows the semantic display descriptions and abstracts away the implementation.
# It also makes localisation easier. instead of remapping every instance of 'UK long' to 'US long' (for example)
# we can simply change 'display' to point at 'US long' instead of 'UK long'
semantic_date_formats = {
    'default' : 'iso 8601 date',
    'full' : 'iso 8601 full',
    'display' : 'UK long',
}
