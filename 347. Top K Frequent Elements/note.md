# step 1

愚直に思いつく方法は, hashmap で出現回数カウントして, 回数でソート, 上から k 個出力. time complexity は O(NlogN).

なんかもっと計算量を改善できる手法がありそう.

ソートせずに, heap で O(N + NlogK)を達成できる.
ヒープにペアを投入していき, K 個を超えた分についてはその場で pop すれば良い.

問題は, どのようにペアのデータを扱うか. 一応タプルを使えば heap として扱える. 独自クラスでやるとなると, cmp とかを定義しないといけなくなりそう.

# step 2

見た回答

- leetcode editorial
  - python の heapq.nlargest を使えば解けたようだ. (O(NlogK))
  - nlargest に key を渡せば, よりきれいにコードを書けるだろう.
  - Hoare's selection algorithm を使えば O(N)で解けそう.
    - quick sort と同様, worst case は O(N^2)となってしまう.
- https://discord.com/channels/1084280443945353267/1183683738635346001/1185656102302523482
- https://discord.com/channels/1084280443945353267/1200089668901937312/1201937181565001748
  - quick select を用いた実装もしている.
  - most_common というメソッドも Counter にはあるとのこと.
    - [CPython の実装](https://github.com/python/cpython/blob/a8e814db96ebfeb1f58bc471edffde2176c0ae05/Lib/collections/__init__.py#L571)を見てみたら, heapq.nlargest 使ってた.
- https://discord.com/channels/1084280443945353267/1201211204547383386/1205149648139063326
- https://discord.com/channels/1084280443945353267/1192736784354918470/1218877363069390969
- https://discord.com/channels/1084280443945353267/1200089668901937312/1221394089287618622
  - 開閉区間で書くのが一般的とのコメントがある. 自分も閉区間で考えがちなので quick select は開閉で書いてみることにする.

quick select の実装もすることにする.

quick select 実装時, pivot をどのように選択するか迷う.

また, quick select の再帰の際渡す引数が間違ってるのか, maximum recursive depth exceeded が出てしまっていた. `selected_index < k`のときに left を`selected_index `ではなく, `selected_index + 1`にすることで解決. 探索範囲が狭まっているかどうかをしっかり理解できていなかったのが問題だったと思う.
