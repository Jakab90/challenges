# This is a solution where the given input is received as csv, then split by comma to an array where the data stored at each index location is printed in the corresponding madlib area.

realArray = input(" Give an adjective, two nouns, another adjective and a proper noun separated by commas.")

realArray = realArray.split(", ")
print (f"Twas brillig in the " + realArray[0] + " toves did " + realArray[1] + " and " + realArray[2] + " in the wabe; all " + realArray[3] + " were the " + realArray[4] + ", and the mome wraths out grabe." )
