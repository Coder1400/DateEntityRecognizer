import re, sys

# extract contents from file
if len(sys.argv) < 2:
    print "Plese pass in the name of a file!"
    sys.exit()
filename = sys.argv[1]

f = open(filename) # open the file using python's standard file library
text = f.read() # extract the file's contents to a string, in order to match the regex against it!


# List of months that take into account shortened versions of each month name (with or wihout a '.')
months = [
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
            "Jan\.?", "Feb\.?", "Mar\.?", "Apr\.?", "May\.?", "Jun\.?", "Jul\.?", "Aug\.?", "Sept\.?", "Oct\.?", "Nov\.?", "Dec\.?"
          ]



# written out numbers that could be used to formulate dates
first_dates = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelvth",
               "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "thirtieth"]
second_dates = ["twenty", "thirty"]



# days of the week that could also be used to formulate dates. This list includes all abbreviations for each day of the week
# with an optional "." following the abbreviation
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
        "Th\.?", "Thu\.?", "Thur\.?", "Thurs\.?", "Tu\.?", "Tue\.?", "Tues\.?", "Sat\.?", "Sun\.?", "Mon\.?", "Fri\.?"
        ]


# let's catch all 'em holidays too :) LOL. This is just a list of holidays that we will try to match with a RegEx pattern as usual. 
holidays = [ 
    "New Year's","New Years", "Martin Luther King, Jr. Day", "Memorial Day", "Independence Day", "Labor Day", "Columbus Day", "Veterans Day", "Thanksgiving",
    "Christmas"
]

match = re.findall(
    
                    # next to each RegEx line, I write an example date format that it catches. Please note: anything in
                    # paranthese means the RegEx will work with or without it.
                    
                    
                    r'(?:'+'|'.join(days)+'),?\s\d{1,2}(?:st|nd|rd|th)?\s(?:'+ '|'.join(months) +'),?\s+?(?:\d{2,4})?' +   # ex. Sunday(,) 12(th) Jan(,) (2004)
                    
                    r'|(?:'+'|'.join(days)+'),?\sthe\s\d{1,2}(?:st|nd|rd|th)(?:\sof\s(?:'+ '|'.join(months) +'))?(?:,?\s\d{2,4})?' + # Sunday(,) the 23rd of Dec(,) (2016)
                    
                    r'|(?:'+'|'.join(days)+'),?\sthe\s(?:'+'|'.join(first_dates)+')(?:\sof\s(?:'+ '|'.join(months) +'))?(?:,?\s\d{2,4})?' + # Sunday(,) the ninth of Dec(,) (2016) 
                    
                    r'|(?:'+'|'.join(days)+'),?\sthe\s(?:'+'|'.join(second_dates)+')(?:-|\s)(?:'+'|'.join(first_dates)+')(?:\sof\s(?:'+ '|'.join(months) +'))?(?:,?\s\d{2,4})?' + # Sunday(,) the twenty(-)first of Dec(,) (2016) 
                    
                    r'|(?:'+'|'.join(days)+'),?\s(?:'+ '|'.join(months) +')\s\d{1,2}(?:st|nd|rd|th)?(?:,?\s?\d{2,4})?' #ex. (monday)(,) Jan 12(,) (2004)
                    
                    r'|(?:'+ '|'.join(months) +')\s\d{1,4}(?:st|nd|rd|th)?,?(?:\s\d{2,4})?' +   # January 2(nd)(,) (2014)
                    
                    r'|\d{1,2}(?:st|nd|rd|th)?\sof\s(?:'+ '|'.join(months) +')(?:,?\s\d{2,4})?' +   # 21st of June(,) (2014)
                   
                    r'|(?:'+'|'.join(second_dates)+')(?:-|\s)(?:'+'|'.join(first_dates)+')\sof\s(?:'+ '|'.join(months) +')(?:,?\s\d{2,4})?'  # Twenty(-)Fifth of Nov(,) (2014)
                   
                    r'|(?:'+'|'.join(first_dates)+')\sof\s(?:'+ '|'.join(months) +')(?:,?\s\d{2,4})?' + # Nineteenth of Nov(,) (2014)
                   
                    r'|\d{4}\s(?:'+ '|'.join(months) +')(?:\s\d{1,2})(?:st|nd|rd|th)?' +    # 1990 Nov. 12(th)
                   
                    r'|(?:'+ '|'.join(["\\b"+m+"\\b" for m in months]) +')' +     # matches any string in 'months' list
                   
                    r'|(?:'+ '|'.join(["\\b"+d+"\\b" for d in days]) +')' +     # matches any string in 'days' list
                    
                    r'|(?:'+ '|'.join(["\\b"+h+"\\b" for h in holidays]) +')' + # matches any string in 'holidays' list
                   
                    r'|\d{1,2}(?:/|-)\d{1,2}(?:/|-)(?:\d{2}|\d{4})' +   # 12/12/2014, 12-12-2014, 
                   
                    r'|(?:\d{2}|\d{4})(?:/|-)\d{1,2}(?:/|-)\d{1,2}' +   # 2014/12/12, 2014-12-12
                   
                    r'|(?:\d{2}|\d{4})/\d{1,2}' +           # 2014/2
                   
                    r'|\d{1,2}/(?:\d{2}|\d{4})' +           # 12/2014
                   
                    r'|1[8-9][0-9][0-9]|20[0-1][0-9]'     # years from 1800 - 2019
                   
                   , text, flags = re.IGNORECASE) # catch all occurences of any of these regexs DISREGARDING case sensitivity!

#print '|'.join(["\\b"+d+"\\b" for d in days])
for date in match: print date  # print out the dates in order seen from file.
f.close()   # close the file that was previously opened for reading


# "ARKEN OUT!" ... (drops mic, walks off stage, everyone claps)  





