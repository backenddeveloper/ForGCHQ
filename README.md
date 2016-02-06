#Webcrawler vs GCHQ puzzle

This is the tale of the day I (legally) hacked a GCHQ challange page to get the answers to a puzzle...

The puzzle was part two of five[?] challanges the British Government Communications HeadQuarters published online in the hopes of attracting brilliant minds to work for them.

The puzzle entry point can be found here: [http://www.gchq.gov.uk/puzz/pages/index.aspx] and consists of a set of six very difficult, and some a little subjective, questions designed to enthuse people with the prospect of working in a code-breaking environment.

A simple example of one of the questions is Q5. What comes after 74, 105, 110, 103, 108, 101, 98, 101, 108, 108? 

a) 108

b) 101

c) 115

d) 123

e) 111

f) 103

The answer is discovered by converting each number from its decimal form into its ASCII counterpart, spelling "JINGLEBELL", the obvious following character is "S" or 155 or (c). 

You cick on each question's answer in turn and are taken to the next page, containing the next question, at the end, if you haven't answered all of the questions correctly you are taken to a page with a message reading "Sorry - you did not get all the questions correct.".

So I was on about my third attempt at the questions when I noticed that the URL of the page I was currently visiting contained my previous answers! At this point the solution to the exercise dawned on me.

There are six questions, each having a set of six possible answers (46656 possible combinations), the failure message is embedded into the page for 46655 of these... python and BASH time - see script.py.

Although slightly convoluted, creating and removing temporary files in the process, it works quite well, putting the following into output.txt in the working directory: DEFACE.html

Thus, without needing to answer the questions we are able to take from the server the correct answer.

A final note is that judging by the fact that this part of the puzzle was outsourced to Amazon's Simple Storage Service, and hosted on a high-availability platform with stupidly fast peering, this is the intended way to solve this puzzle.
