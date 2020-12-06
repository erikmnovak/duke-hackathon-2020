import numpy as np
import heapq

facebook = [4, 4, 4, 4, 4, 4, 1, 3]
pinterest = [0, 4, 0, 2, 0, 0, 0, 0]
twitter = [2, 3, 3, 4, 4, 4, 4, 1]
instagram = [3, 4, 4, 3, 1, 3, 4, 1]
whatsapp = [4, 2, 2, 0, 4, 0, 0, 4]
tumblr = [1, 3, 3, 4, 2, 3, 1, 3]
skype = [4, 1, 1, 0, 2, 0, 0, 2]
reddit = [0, 3, 3, 4, 4, 4, 1, 3]
youtube = [0, 0, 4, 3, 1, 4, 1, 4]
tiktok = [1, 0, 1, 3, 0, 1, 3, 0]

social_media = [facebook, pinterest, twitter, instagram, whatsapp, tumblr, skype, reddit, youtube, tiktok]
social_media_index = ["facebook", "pinterest", "twitter", "instagram", "whatsapp", "tumblr", "skype", "reddit", "youtube", "tiktok"]

def similar(list):
    # array which will store the difference between the user's responses and each media
    # index 0 is facebook, 1 is pinterest, 2 is twitter, so on and so forth
    difference = [0,0,0,0,0,0,0,0,0,0]

    # list which will be returned, where index 0 is the most similar and 2 is the least
    ret = ["a", "b", "c"]

    for y in range(len(social_media)): 
        # creating a list to store the distance between the media and each question response
        distance_list = [0,0,0,0,0,0,0,0]

        for x in range(len(list)):
            # finding the euclidian distance in question number x
            distance = np.abs((list[x] - social_media[y][x]) * (list[x] - social_media[y][x]))

            # placing the distance in the list
            distance_list[x] = distance
            
        # finding the sqrt
        square_root = np.sqrt(sum(distance_list))

        # saving the the distance
        difference[y] = square_root
    

    ret[0] = difference.index(min(difference))
    difference[difference.index(min(difference))] = 120
    ret[1] = difference.index(min(difference))
    difference[difference.index(min(difference))] = 120
    ret[2] = difference.index(min(difference))

    # look man, it just worked. i cant do ret[0] = social_media_index[ret[0]]
    x = ret[0]
    y = ret[1]
    z = ret[2]

    ret[0] = social_media_index[x]
    ret[1] = social_media_index[y]
    ret[2] = social_media_index[z]

    return ret

example = [3, 3, 3, 2, 4, 4, 1, 3]

print(similar(example))