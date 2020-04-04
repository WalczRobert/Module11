enter_menu = None
#Program Loop to accept only 1-4 for the menu
while enter_menu not in ("1", "2", "3", "4"):
    #start menu
    enter_memu = input("What do you want to do ?\nPress 1 for adding a note\nPress 2 for searching a note\nPress 3 to display the cache\nPress 4 to clear the cache Note\nPress other keys to exit\n: ")
    #Choice 1 Insert a note in DB
    if enter_memu == "1":
        enter_note = input("Enter your note\n")
        cache_file = open("data/notapp_cache.txt", "a")
        cache_file.write(enter_note + "\n---\n")
        cache_file.close()
    #Choice 2 Display the line in search DB
    elif enter_memu == "2":
        enter_search = input("Enter the text to search\n")
        cache_file = open("data/notapp_cache.txt")
        content_cache = cache_file.read()
        cache_file.close()
        result_search = content_cache.find(enter_search)
        #check if the word exist
        if result_search != -1:
                #Loop to search the line to print       
                for line in open("data/notapp_cache.txt"):
                    if enter_search in line:
                        print (line + "\n----")
                        cache_file.close()
        #If the word not exist
        else:
            print ("No search Notes in DB")
    #Choice 3 Display the content DB        
    elif enter_memu == "3":
        cache_file = open("data/notapp_cache.txt")
        content_cache = cache_file.read()
        cache_file.close()
        print(content_cache)
    #Choice 4 Clear de cache DB
    elif enter_memu == "4":
        cache_file = open("data/notapp_cache.txt", "w")
        cache_file.close()
    #If you do't select 1 - 4 the program exit
    else:
        quit()


