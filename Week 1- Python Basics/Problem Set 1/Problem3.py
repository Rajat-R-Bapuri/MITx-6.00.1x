# Print the longest substring of a string 's' in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print --> Longest substring in alphabetical order is: beggh

### This program is better understood by tracing it ###

curCounter = 0
endIdx = 0
maxLen = 0

for i in range(len(s) - 1):
    if((s[i]) <= (s[i + 1])):
        curCounter += 1
        if(curCounter > maxLen):
            maxLen = curCounter
            endIdx = i + 1
    else:
        curCounter = 0
print('Longest substring in alphabetical order is: ', s[endIdx - maxLen: endIdx + 1])
