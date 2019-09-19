def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    print({yourLeft, yourRight})
    return (max(yourLeft, yourRight) == max(friendsLeft, friendsRight)) and (min(yourLeft, yourRight) == min(friendsLeft, friendsRight))

print(areEquallyStrong(20, 15, 5, 20))