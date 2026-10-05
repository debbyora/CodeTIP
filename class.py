def find_needle(haystack, needle):
    # Write your code here
    index = 0 
    counter = False
    for i in range(len(needle)):
        for j in range(len(haystack)):
            if needle[i] == haystack[j]:
                index = i
                count = index
    while(needle[count] == haystack[count]):
        counter = True
        count +=1 
    if counter:
        return index
    else:
        return -1

find_needle("sadbutsad","sad")
