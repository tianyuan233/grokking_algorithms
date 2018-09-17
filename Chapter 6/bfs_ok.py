graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searchd = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searchd:
            if person_is_seller(person):
                print('{} is a mongo sessler'.format(person))
                break
            else:
                search_deque += graph[person]
                searchd.append(person)
                print(searchd)


search("you")