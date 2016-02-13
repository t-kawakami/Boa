# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'
import collections

list_1 = [1, 2, 3, 4, 5, 6]
# xrangeはrangeに比べてメモリの消費量が少なく速いらしい
for index in xrange(len(list_1)):
    print 'xrange loop:', index, list_1[index]
# enumerateで簡単に書く
for index, value in enumerate(list_1):
    print 'enumerate loop:', index, value

# zip処理を試す
list_1, list_2 = [2, 4, 6, 8], [3, 6, 9, 12]
for num_1, num_2 in zip(list_1, list_2):
    print 'zip:', num_1, num_2

# zipとenumerateの組み合わせ
for index, (num_1, num_2) in enumerate(zip(list_1, list_2)):
    print 'enumerate & zip:', index, num_1, num_2

# yieldを試す
def iteration_list(list_1, batch=2):
    for index in xrange(0, len(list_1), batch):
        yield list_1[index: index + batch]

# ここでの変換は、[2,4,6,8]→[2,4],[6,8]にすること
for obj in iteration_list(list_1):
    print 'yield:', obj
# ただし、このままでは出力できない
print iteration_list(list_1)
# batchを3にした場合[2,4,6,8]→[2,4,6],[8]
for obj in iteration_list(list_1, batch=3):
    print 'yield:', obj

# loopの内包表現
print 'inner loop:', [index for index in xrange(10)]
print 'inner loop if:', [num for index, num in enumerate(list_1) if index == 2]

# list内の要素をカウントする。
counter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'い', 'a', '', '', 'b', 'a', 'e', 'あ', 'あ']
counter = collections.Counter(counter_list)
print 'counter:', counter
print 'counter a:', counter['a']
print 'counter あ:', counter['あ']

# counterは配列は無理
# counter_list_2 = [[1,2,3,4], [1,2,3], [1,2], [1,2], [1,2,3]]
# counter_2 = collections.Counter(counter_list_2)
# Tupleはできる。順序も見る
counter_tuple_list = [(1, 2, 3), (1, 2), (1, 2), (2, 1), ('a'), ('a', 'b')]
counter_tuple = collections.Counter(counter_tuple_list)
print 'counter tuple:', counter_tuple
print 'counter tuple(1,2):', counter_tuple[(1, 2)]
# 辞書は無理
# counter_dict_list = [{1, 2, 3}, {1, 2}, {1, 2}, {2, 1}]
# counter_dict = collections.Counter(counter_dict_list)

# 辞書に存在しない場合の初期値を投入
dictionary = {}
if 'a' in dictionary:
    dictionary['a'] = 1
else:
    dictionary['a'] = 2
print 'dictionary normal:', dictionary
# defaultdictを使う
dictionary = collections.defaultdict(int)
dictionary['a'] += 3
print dictionary
dictionary['a'] += 3
print dictionary

# sort
sort_list = [1, 3, 7, 4, 5, 9, 8, 2, 6]
sort_list_word = ['d', 'e', 'v', 'x', 'q', 'd', 's', 'a']
print 'sort_list:', sorted(sort_list)
print 'sort_list_word:', sorted(sort_list_word)
print 'sort_list reverse:', sorted(sort_list, reverse=True)
print 'sort_list_word reverse:', sorted(sort_list_word, reverse=True)

# 辞書のsort
dict = {'b': 2, 'c': 4, 'x': 1, 'a': 3}
print dict  # そのまま出力
print dict.keys()  # keyのみ出力
print sorted(dict)  # keyのみソートして出力
print dict.values()  # valueは後ろから出力する
print sorted(dict.values())  # valueのみソートして出力
print dict.items()  # key, valueをtuple(?)で出力
print sorted(dict.items())  # keyでソート
print sorted(dict.items(), key=lambda x: x[0])  # keyでソート
print sorted(dict.items(), key=lambda x: x[1])  # valueでソート

# if文の連結
list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
for index, value in enumerate(list_1):
    if 2 < index < 5:
        print index, value
# inステートメント
search_word = 'c'
if search_word in list_1:
    print 'find!'