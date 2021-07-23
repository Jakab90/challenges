# This is a looped version of my array madlib

realArray = input(" Give an 1. adjective, 2. a noun, 3. a funnier noun, 4. a better adjective and 5. a proper noun, all separated by commas.")

realArray = realArray.split(", ")

while len(realArray) == 5: 
        
        print (f"Twas brillig in the " + realArray[0] + " toves did " + realArray[1] + " and " + realArray[2] + " in the wabe; all " + realArray[3] + " were the " + realArray[4] + ", and the mome wraths out grabe." )
        
        realArray = input(" Give an adjective, two nouns, another adjective and a proper noun separated by commas.")
        realArray = realArray.split(", ")
