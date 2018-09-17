graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

search_deque = deque()

search_deque += graph["you"]


def person_is_seller(name):
    return name[-1] == 'm'

while search_deque:
    person = search_deque.popleft()
    if person_is_seller(person):
        print('{} is a mongo sessler'.format(person))
        # return True
        break
    else:
        search_deque += graph[person]
        # return False



