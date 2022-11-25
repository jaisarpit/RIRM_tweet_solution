from collections import OrderedDict

testcase = int(input())

while testcase:
    users = int(input())
    tweets = {}
    for i in range(0,users):
        inp = input().split(" ")
        tweets[inp[0]] = tweets.setdefault(inp[0], 0) + 1

    max_tweet = max(tweets.values())
    ans = {}
    for key,value in tweets.items():
        if value==max_tweet:
            ans[key] = value
    sorted_ans = OrderedDict(sorted(ans.items()))
    for key,value in sorted_ans.items():
        print(key," ",value)
    testcase -=1