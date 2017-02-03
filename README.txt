ASSIGNMENT 1: LING 406

Arken Ibrahim
netid: amibrah2


Installation Instructions:

1.) clone this repository https://github.com/Arken94/DateEntityRecognizer.git from github (I have added you as a collaborator).

2.) Find the file called “finddates.py” and run “python finddates.py <filename.txt>” in your terminal window to run my code. 

3.) NOTE: you must pass in a file as the first command line argument for the program to work. 

4.)NOTE: I have uploaded all my test files to the github repository. Check those out if you would like!

5.) Thats it! Enjoy my program! I hope I get an A :)




Brief description of code

My code is built completely around pythons “re” library and its RegEx capabilities. I make sure to store all list of proper names that I will need to use in my regex, like month names, day names, written countable integers, etc.. I then use the built-in “findall” function to find all the matches of my RegEx patterns within the file that was passed into my program. A unique feature that I implemented in my code, was that instead of searching through the file numerous times in order to find all possible matches, I wrote one long RegEx pattern using the or ( “|” ) operator then simply used that pattern once on the file. This way, the code is more efficient, it ensures that dates are outputted in the proper order, and it makes the code cleaner in general! I had a lot of fun with this MP and 