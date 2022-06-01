# How to use: python3 wiki.py bfs Google ロボット工学三原則

from cgi import test
from collections import deque
import sys

def main(method, start_name, goal_name):
    pages = {}
    links = {}

    with open('data/pages_small.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('data/links_small.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
            # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}

    for k, v in pages.items():
        if v == start_name: # 'Google'
            print(start_name, k)
            start = k
        if v == goal_name:  #'ロボット工学三原則'
            print(goal_name, k)
            target = k
    
    if method == 'dfs':
        # print(dfs(links, start, target, pages, set()))
        path_dfs = dfs_path(start,target,links)
        if path_dfs != 'No path found':
            path_dfs = [pages[i] for i in path_dfs]
        print(f'The path from "{start_name}" to "{goal_name}" is {path_dfs}')
    if method == 'bfs':
        path_bfs = bfs_path(start,target,links)
        if path_bfs != 'No path found':
            path_bfs = [pages[i] for i in path_bfs]
        print(f'The path from "{start_name}" to "{goal_name}" is {path_bfs}')
        print_info


def print_info():
    print(f'The length of the path is {length_path}.')
    print(f'The total number of searching is {total_search}.')
    print('The interesting thing is that the total number of' \
        ' searching changes randomly.')


def bfs(start,target,links):
    global path_rec_bfs 
    global total_search
    container = deque()
    container.append(start)
    visited = {}
    total_search = 0
    visited[start] = True
  # while container is not empty
    while container:
        v = container.popleft()
        total_search += 1
        if v == target:
            return True
        elif v in links:
            for to_visit in links[v]:
                if not visited.get(to_visit):
                    visited[to_visit] = True
                    path_rec_bfs[to_visit] = v
                    container.append(to_visit)
    return False

def bfs_path(start,target,links):
    global length_path
    global path_rec_bfs
    path_rec_bfs = {}
    length_path = 0

    if bfs(start,target,links):
        # print(path_rec_bfs)
        path_bfs = []
        index = target
        while index != start:
            length_path += 1
            path_bfs.append(index)
            index = path_rec_bfs[index]
        path_bfs.append(index)
        path_bfs.reverse()
        return path_bfs
    return 'No path found'


# def dfs(start, target, links):
#     # stack
#     global path_rec_dfs 
#     global total_search
#     container = deque()
#     container.append(start)
#     visited = {}
#     total_search = 0
#     visited[start] = True
#   # while container is not empty
#     while container:
#         v = container.pop()
#         total_search += 1
#         if v == target:
#             return True
#         elif v in links:
#             for to_visit in links[v]:
#                 if not visited.get(to_visit):
#                     visited[to_visit] = True
#                     path_rec_bfs[to_visit] = v
#                     container.append(to_visit)
#     return False

# def dfs_path(start,target,links):
#     global length_path
#     global path_rec_dfs
#     path_rec_dfs = {}
#     length_path = 0

#     if dfs(start,target,links):

#         path_dfs = []
#         index = target
#         while index != start:
#             length_path += 1
#             path_dfs.append(index)
#             index = path_rec_dfs[index]
#         path_dfs.append(index)
#         path_dfs.reverse()
#         return path_dfs
#     return 'No path found'

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
