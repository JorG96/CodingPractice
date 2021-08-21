'''Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.'''

import re
def validTime(time):
    T=re.search("^([01]?[0-9]|2[0-3]):[0-5][0-9]$",time)
    if T is None or time=="":
        return False
    else:
        return True