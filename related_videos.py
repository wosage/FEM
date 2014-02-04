#import the data provided
import json
f = open("CodeAssignmentDataSet.json")
data = json.load(f)
title = []
desc = []
for i in range(0, 474):
    title.append(data[i]['title'])
    desc.append(data[i]["description"])

#break the titles up into words 
split_title = [[] for j in range(474)]
for k in range(0,474):
    split_title[k] = title[k].split()

#break the descriptions up into words 
split_desc = [[] for l in range(474)]
for m in range(0,474):
    split_desc[m] = desc[m].split()

#use proper nouns from description as tag words
tags_desc = [[] for p in range(474)]
for n in range(0, 474):
    words = len(split_desc[n])
    for o in range(0,words):
        split_word = list(split_desc[n][o])
        cap = split_word[0].isupper() 
        if cap is True and len(split_desc[n][o]) > 2:
            letters = len(split_word)
            if split_word[letters-2] != "." and split_desc[n][o] != "The" and split_desc[n][o] != "Watch": 
                tags_desc[n].append(split_desc[n][o])

 #use proper nouns from title as tag words 
tags_title = [[] for q in range(474)]
for r in range(0, 474):
    words_t = len(split_title[r])
    for s in range(0,words_t):
        split_words_t = list(split_title[r][s])
        cap = split_words_t[0].isupper() 
        if cap is True and len(split_title[r][s]) > 2:
            letters = len(split_words_t)
            if split_words_t[letters-2] != "." and split_title[r][s] != "The" and split_title[r][s] != "Watch":
                tags_title[r].append(split_title[r][s])
        
#combine both of the tags lists into one with no repatitions  
tags = [[] for t in range(474)]
for u in range(0,474):
    length = len(tags_desc[u])
    for v in range(length):
        tags[u].append(tags_desc[u][v])
    length_t = len(tags_title[u])
    for w in range(length_t):
        if tags_title[u][w] not in tags[u]:
              tags[u].append(tags_title[u][w])

#open output file
output = open('output.txt', 'w')

#find a match with each title 
for x in range(0, 474):
    print x
    output.write("Related videos for " + title[x] + " are: \n")
    matches = [[] for a in range(474)]
    num_matches = [[] for b in range(474)]
    for y in range(0,474):
        num_tags = len(tags[x])
        for z in range(num_tags):
            if tags[x][z] in tags[y]:
                matches[y].append(tags[x][z])
        num_matches[y] = len(matches[y])
    num_matches_keep = num_matches
    
    #find the 3 best matches not including the same video
    num_matches.remove(max(num_matches))
    best_match_num = max(num_matches)
    best_match = num_matches_keep.index(best_match_num)
    output.write("1)  "+str(title[best_match]) + "\n")
    
    #if statments are to help with two matches with the same number of matching tags
    num_matches.remove(max(num_matches))
    second_best_num = max(num_matches)
    if second_best_num == best_match_num: 
        second_best = (num_matches_keep.index(second_best_num)+1)
        output.write("2)  "+str(title[second_best])+ "\n")
    else: 
        second_best = num_matches_keep.index(second_best_num)
        output.write("2)  "+str(title[second_best])+ "\n")
         
    num_matches.remove(max(num_matches))
    third_best_num = max(num_matches)
    if third_best_num == best_match_num:
        third_best = (num_matches_keep.index(third_best_num)+2)
        output.write("3)  "+str(title[third_best])+"\n")
    elif third_best_num == second_best_num:
        third_best = (num_matches_keep.index(third_best_num)+1)
        output.write("3)  "+str(title[third_best])+"\n\n\n")
    else:
        third_best = num_matches_keep.index(third_best_num)
        output.write("3)  "+str(title[third_best])+"\n\n\n")

#close output file
output.close()   
    
    

                      
    
    
            
            
    

            
            
        
    
    


            

            





            
                    



            
        





 
