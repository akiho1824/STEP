## Code Review for Shiori San

実行目的：Googleから渋谷へ至る経路があるか探す


実行結果：
Googleから渋谷へ至る経路検索成功！！（BFSもDFSも）
```
bfs search finished!
True
dfs search finished!
True
```

# データの読み込みと準備
```
# question1では、Googleから渋谷へ至る経路があるか探します

import re
from collections import deque

# graghを隣接リストの形で保持する
# idと名称のセットを辞書で保存する

graph = {}
id_to_name = {}
name_to_id = {}
```
変数名はすごくわかりやすいです！ Great!

```
with open("./data/links.txt") as f:
    for line in f:
        # とりあえず2つの数字をlistにして読み込む
        line = line.replace('\n','')
        line_mod = re.sub('\s+',' ',line) # 正規表現を用いて、空白の数を一つに揃えている
        relative_nodes = list(map(int,line_mod.split(' ')))
        #print(relative_nodes)

        # 隣接リストに追加
        for i, node_id in enumerate(relative_nodes):
            if node_id in graph:
                graph[node_id].append(relative_nodes[1-i])
            else:
                graph[node_id] = [relative_nodes[1-i]]

#print(graph.keys())


with open("./data/pages.txt") as f_:
    for line in f_:
        line = line.replace('\n','')
        id, name = line.split('\t')
        id = int(id)   
        id_to_name[id] = name
        name_to_id[name] = id

#print(id_and_name)
```
以上の部分で、```re.sub```などの私が知らなかった関数が使われていましたので、すごく勉強になりました！

## DFSの実装
とても分かりやすくて、綺麗にまとまっています！　Nice!
探索済みかどうかを保持するための```visited_list```の作り方がすごく面白いです！
```
# idを使ってbfs
def id_dfs(graph,start_id,target_id):
    stack = []
    # 探索済みかどうかを保持
    visited_list = [False]*(max(graph.keys())+1) 

    #初期値を入れる
    stack.append(start_id)
    visited_list[start_id] = True

    while len(stack) > 0: # stackに入ってるノードがなくなるまで続ける
        node = stack.pop(-1) # 全てのノードを最大1度ずつ見るので、これを繰り返すことによる計算量は合計O(V)

        if node == target_id: # 処理の終了条件
            return True
        
        for next_node in graph[node]: # 全てのエッジを最大1度ずつ見るので、これを繰り返すことによる計算量はO(E)
            if visited_list[next_node] == False:
                visited_list[next_node] = True
                stack.append(next_node)

    return False
```


## BFSの実装
とても分かりやすくて、綺麗にまとまっています！　Nice!
```
# idを使ってbfs
def id_bfs(graph,start_id,target_id):

    # データ構造を初期化
    visited_list = [False]*(max(graph.keys())+1)
    queue = deque([])

    #初期値を入れる
    visited_list[start_id] = True
    queue.append(start_id)

    while len(queue) > 0: # キューに入ってるノードがなくなるまで続ける
        node = queue.popleft()

        if node == target_id: # 処理の終了条件
            return True
         
        for next_node in graph[node]:
            if visited_list[next_node] == False:
                visited_list[next_node] = True
                queue.append(next_node)

    return False
 ```

最後にまとめて回すところも非常に分かりやすかったです！
```
# 名称からidを抽出
def name_dfs(graph,start_name,target_name):
    # 名称をidに変換
    start_id = name_to_id[start_name]
    target_id = name_to_id[target_name]

    # 探索
    reachable = id_dfs(graph,start_id,target_id)
    print('dfs search finished!')

    return reachable


def name_bfs(graph,start_name,target_name):
    # 名称をidに変換
    start_id = name_to_id[start_name]
    target_id = name_to_id[target_name]

    # 探索
    reachable = id_bfs(graph,start_id,target_id)
    print('bfs search finished!')

    return reachable

"""
多分ここにlinks_small,pages_smallでテストするコードを入れたほうが良い気がしました…
"""
print(name_bfs(graph,'Google','渋谷'))
print(name_dfs(graph,'Google','渋谷'))
```

## 全体的な感想

とても分かりやすかったです！
そして、私はPythonの初心者レベルでしたので、シオリさんのコードから色々勉強できました！
これからもよろしくお願いします〜
