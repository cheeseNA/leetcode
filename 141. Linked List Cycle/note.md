# step1

解法は

- slow/fast の２つのカーソルを使う方法
- 訪問済みノードを set で管理しておく方法
  の２つが考えられる.

疑問点

- set には node を入れることができるか？その場合ハッシュ関数はどの様な実装になっているだろうか？Object の`__eq__`はどう実装されているだろうか.

前回は set を使用する方法で解いたので slow/fast で解いてみる.
time comlexity は O(N), space complexity は O(1).

# step2

見たコード, コメント

- google docs の sample answer
  - reStructuredText という docstring の書き方を知った. こちらも命名スタイルと同様色々流派があることを把握して, 基礎的なものについては書けるようになるべき.
  - while の条件文は head と head.next が None でないか確認している. 自分の回答だと head が None の場合早期 return しているが, この条件にするとまとめることができる.
- https://discord.com/channels/1084280443945353267/1195700948786491403/1195720397077880842
  - 代入の仕方に選択の余地があることを確認. 理屈ではなく感覚でしかないが, 自分としては代入演算子が続くことは違和感を覚えるため分けている.
  - wiki の cycle detection のページを見て, Floyd 以外にもバリエーションがあることを知った. 特に Brent のものは周期を高速に知ることができる. ただこの知識が常識に入るかどうかは怪しいと思うので, 高速である必要がある時以外は Floyd のアルゴリズムを選択するのが良いだろう.
- https://discord.com/channels/1084280443945353267/1192728121644945439/1192775334425272390
  - 大域脱出に注意.
- https://discord.com/channels/1084280443945353267/1183683738635346001/1183690412926455868
- https://discord.com/channels/1084280443945353267/1200089668901937312/1205459051631222785
  - Floyd のアルゴリズムにも while 前の初期化のバリエーションなどがあることを確認.

set には ListNode を入れることができる.

https://github.com/python/cpython/blob/main/Objects/classobject.c
ここに hash 関数や eq 関数が実装されていそうだが, 読めず.

実験したところ

```python
o = object()
p = object()
o.__eq__(p) # NotImplemented
```

という挙動. ちなみに hash の値は違った. leetcode で比較ができているのは, どこかで`__eq__`が実装されているからだと思う.

とおもったが, [この記事](https://blog.tiqwab.com/2017/02/26/implement-eq-in-python.html)によるとユーザー定義クラスの`__eq__`は id の比較を行うらしい.
