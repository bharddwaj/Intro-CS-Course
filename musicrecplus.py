'''
Created on Apr 13, 2019

@author: Bharddwaj Vemulapalli
username: bvemulap

I pledge my honor that I have abided by the Stevens Honor System.
'''
DB_file = "musicrecplus.txt"
'''''''''''''''''''''HELPER FUNCTIONS'''''''''''''''''''''''''''''''''''''''
def num_matches(list1,list2):
    '''Returns the number of elements that the two lists have in common'''
    list1.sort()
    list2.sort()
    matches = 0
    counter1 = 0
    counter2 = 0
    while counter1 < len(list1) and counter2 < len(list2):
        if list1[counter1] == list2[counter2]:
            matches += 1
            counter1 += 1
            counter2 += 1
        elif list1[counter1] < list2[counter2]:
            counter1 += 1
        else:
            counter2 += 1
    return matches

       

def keep_matches(list1,list2):
    '''returns the common elements in both lists'''
    list1.sort()
    list2.sort()
    matches = []
    counter1 = 0
    counter2 = 0
    while counter1 < len(list1) and counter2 < len(list2):
        
        if list1[counter1] == list2[counter2]:
            matches.append(list1[counter1])
            counter1 += 1
            counter2 += 1
        elif list1[counter1] < list2[counter2]:
            counter1 += 1
        else:
            counter2 += 1
    return matches


def drop_matches(list1,list2):
    '''Returns the list that contains no matches between elements of list1 and list2'''
    list1.sort()
    list2.sort()
    results = []
    counter1 = 0
    counter2 = 0
    while counter1 < len(list1) and counter2 < len(list2):
        if list1[counter1] == list2[counter2]:
            counter1 += 1
            counter2 += 1
        elif list1[counter1] < list2[counter2]:
            results.append(list1[counter1])
            counter1 += 1
        else:
            results.append(list2[counter2])
            counter2 += 1
    while counter1 < len(list1):
        results.append(list1[counter1])
        counter1 += 1
    while counter2 < len(list2):
        results.append(list2[counter2])
        counter2 += 1
    return results
    

def menu(user):
    '''Displays the various options that the user has available to them
    and allows the user to do the action they want based on their input '''
    
    print('Enter a letter to choose the option: ')
    print('e - Enter preferences')
    print('r - Get recommendations')
    print('p - Show most popular artists')
    print('h - How popular is the most popular')
    print('m - Which user has the most likes')
    print('q - Save and quit')
    ans = input()
    
    if ans == 'e':
        enter_preferences(user)
        
        #this block of code is copied from the save and quit because that's what the html file shows essentially
        '''
        f = open(DB_file,'w')
        alphabetize = []
        for x in user_to_artists.keys():
            alphabetize.append(x)
        alphabetize.sort()
        
        for key in alphabetize:
            total_artists = ''
            user_to_artists[key].sort()
            for j in user_to_artists[key]:
                total_artists += j +','
            f.write(key + ':' + total_artists + '\n')
        f.close()
        '''
        
        return menu(user)
            
    elif ans == 'r':
        the_recommendation = get_recommendations(user)
        
        if isinstance(the_recommendation, list):
            for x in the_recommendation:
                print(x)
        else:
            print(the_recommendation)
            
        return menu(user)
    elif ans == 'p':
        call = show_most_popular_artists()
        if isinstance(call, list):
            call.sort()
            for x in call:
                print(x)
        else:
            print(call)
        return menu(user)
    elif ans == 'h':
        print(most_popular())
        return menu(user)
    elif ans == 'm':
        call = user_with_most_likes()
        if isinstance(call, list):
            call.sort()
            for x in call:
                print(x)
        else:      
            print(call)
        return menu(user)
    
    elif ans == 'q':
        
        f = open(DB_file,'w')
        alphabetize = []
        for x in user_to_artists.keys():
            alphabetize.append(x)
        alphabetize.sort()
        
        for key in alphabetize:
            total_artists = ''
            user_to_artists[key].sort()
            for j in user_to_artists[key]:
                total_artists += j +','
            f.write(key + ':' + total_artists[:-1] + '\n')
        f.close()
        print('Done')
    else:
        print('You did not enter one of the choices listed')
        print('please pick from one of the choices')
        return menu(user)

   
def user_with_most_likes():
    '''Returns user(s) who like the most artists'''
    filtered_keys = list(filter(lambda x: '$' != x[-1],user_to_artists.keys()))
    num_likes = 0
    key = ''
    for x in filtered_keys:
        if len(user_to_artists[x]) > num_likes:
            num_likes = len(user_to_artists[x])
            key = x
        elif len(user_to_artists[x]) == num_likes:
            key += ',' + x
    if num_likes == 0:
        return 'Sorry, no artists found'
    return key.split(',')
def most_popular():
    '''Returns the number of likes the most popular artist(s) has'''
    likes = 0
    for v in artists_count.values():
        if v > likes:
            likes = v
            
    if likes == 0:
        return 'Sorry, no artists found'
    else:
        return likes
def get_recommendations(user):
    everyone_else = list(filter(lambda x: x!= user and x[-1] != '$',user_to_artists.keys()))
    most_matches = [0,''] #most matches and the key
    if len(everyone_else) > 0:
        for x in everyone_else:
            matches = num_matches(user_to_artists[user], user_to_artists[x])
            #print(matches)
            if matches > most_matches[0] and (matches != len(user_to_artists[x]) and matches != len(user_to_artists[user])):
               
                most_matches[0] = matches
                most_matches[1] = x
        #print(most_matches)
        recommendations = list(filter(lambda x: x not in user_to_artists[user] ,drop_matches(user_to_artists[user], user_to_artists[most_matches[1]]) ) )
    if most_matches[0] == 0 or len(recommendations) == 0:
        # if filtered list is equal to 0 the length of artists is the exact same
        return 'Sorry, No recommendations available for ' + user
    #the reason for the filter is you don't care about artists that you already have
    return recommendations
            

def show_most_popular_artists():
    '''Returns the most popular artist(s) '''
    
    count = 0 
    key = ''
    for k,v in artists_count.items():
        if v > count:
            count = v
            key = k
        elif v == count:
            key += f'\n{k}'
    if count == 0:
        return 'Sorry, no artists found'
    else:
        return key.split('\n')
                
        
    
def enter_preferences(user):
    '''Prompts user for their favorite artists and returns a list of their artists. 
    This function also reduces the artists (the user previously preferred) counts in the artists_count dictionary down by 1.'''
    fav_artists_complete = ''
    fav_artists = ' '
    fav_artists_list = []
    
    if user in user_to_artists.keys():
        for x in user_to_artists[user]:
            artists_count[x] -= 1
    #when I'm changing the user preferences i have to reduce the count in the artists count dictionary
    
    while fav_artists != '':
        fav_artists = input('Enter an artist that you like (Enter to finish): ')
        if fav_artists not in artists_count.keys() and '$' != user[-1] and fav_artists != ' ' and fav_artists != '':
            artists_count[fav_artists] = 1
        elif '$' != user[-1] and fav_artists != ' ' and fav_artists != '':
            artists_count[fav_artists] += 1
        if fav_artists != ' ' or fav_artists != '':
            #have to add this condition because i am getting spaces and null strings loaded into my data
            fav_artists_complete += fav_artists + ','
            fav_artists_list.append(fav_artists)
    #print(fav_artists_list) #don't understand why empty string is being appended even with the if statement
    user_to_artists[user] = fav_artists_list
    return fav_artists_complete[:-2] #the last two indexes are going to be commas



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
user_to_artists = {}
artists_count = {}
#we pull data from the file if anything is previously loaded
f = open(DB_file,'r')
for line in f:
    line = line.strip()
    if len(line) == 0:
        continue
    user, artists = line.split(':')
    artists = artists.split(',')
    for i in range(len(artists)):
        artists[i] = artists[i].strip()
        if artists[i] not in artists_count.keys() and '$' != user[-1] and artists[i] != ' ' and artists[i] != '':
            artists_count[artists[i]] = 1
        elif '$'!= user[-1] and artists[i] != ' ' and artists[i] != '':
            artists_count[artists[i]] += 1
    user_to_artists[user] = list(filter(lambda x: x != '' and x!= ' ', artists))
f.close()
#print(user_to_artists)
#print(artists_count)

first_question = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
if first_question not in user_to_artists.keys():
    enter_preferences(first_question)
    menu(first_question)
else:
    #print("now it's just menu")
    menu(first_question)

        
    