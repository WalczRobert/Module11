#open the file
data_file = open("data/data_zen.txt")
#read the file 
content_text_file = data_file.read()
#close the file
data_file.close()

# put the file in two variable
content_text_file_count = content_text_file
content_text_file_replace = content_text_file


#remove "."
removed_character = content_text_file_count.replace(".", "")
#remove "-"
removed_character = removed_character.replace("-", "")
#remove "!"
removed_character = removed_character.replace("!", "")
#replace "'" by " "
removed_character = removed_character.replace("'", " ")
#remove "*"
removed_character = removed_character.replace("*", "")
#remove ","
removed_character = removed_character.replace(",", "")
#replace new line (enter) by " "
removed_character = removed_character.replace("\n", " ")
#replace "  " by " "
removed_character = removed_character.replace("  ", " ")
##for the test print the result
#print (removed_character)

#count words
count_words = len(removed_character.split())
#print count
print ("Number words in file: " + str(count_words))
# print "---------------"
print ("--------------------------")

#replace in variable the word "is" by "should be"
replace_text = content_text_file_replace.replace ("is", "should be")

#print the result in upper case in the terminal
print (replace_text.upper())


