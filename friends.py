Input = ["Ryan", "Kieran", "Jason", "Yous"]


def friend(friends):
    friend_list = []
    for name in friends:
        if len(name) == 4:
            friend_list.append(name)
    return friend_list


print(friend(Input))
