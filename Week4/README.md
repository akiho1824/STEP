
# **WEEK4 HOMEWORK**

Goal: Look for a path from ”Google” to ”Shibuya” using DFS & BFS

## Data files
Data files we need here is ```links.txt``` and ```pages.txt```.

These two files should be under ```STEP/Week4/data```.

### How to use
To run this Python3 file, first we should set the directory.
```
$ cd ../STEP/Week4
```

To run the program, the command should be in this format:

```python3 wiki.py``` + ```the method of searching(dfs or bfs)``` + ```start wikipage``` + ```goal wikipage```

Sample command:
```
$ python3 wiki.py bfs Google ロボット工学三原則
```
The result will be like:
```
$ ロボット工学三原則 10038
$ Google 457783
$ The path from "Google" to "ロボット工学三原則" is ['Google', 'ロボット', 'ロボット工学三原則']
$ The length of the path is 2.
$ The total number of searching is 23.
$ The interesting thing is that the total number of searching changes randomly.
```
This is a result running on ```links_small.txt``` and ```pages_small.txt```.
The result might be different with the result of running it on ```links.txt``` and ```pages.txt```.

<!-- ## Look for the path from ”Google” to ”Shibuya” using DFS & BFS -->


