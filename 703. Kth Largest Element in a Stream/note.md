# step 1

time: 23:50

k 番目よりあとの数字は持たなくて良い.
まず最初にソートは必要.
ソートされていれば二分探索は可能だが追加に O(k)かかる.
max heap を使おう.

heap で k 番目の要素って取れるっけ？無理だ.
だから上から k-1 個の heap と k 番目の値を持っておいて, 新しい数字が来たら heap に投入, それで...けどそれで飛び出た一番下の値がわからないな.

やはり min heap を使う. 最初は上から k 個で min heap を作り, 新しい数が来るたびに min との大小関係をチェック, 新しい数が大きいなら heap に投入して pop, 新しい min を返せば良い.

初期化のときにソートしてから heappush すべきか, それとも heappush して小さい要素を pop すべきか. heapq.nlargest があるが, "The latter two functions perform best for smaller values of n. For larger values, it is more efficient to use the sorted() function."とのこと. 一旦ソートしてから push することにする.

heapify はなぜ O(n)? → 根までの距離の分だけ入れ替えをするが, 各深さごとのノードの数で重みを付けて和を取ると O(N)となる.

len(nums)を N, add の回数を M とすると, time complexity は O(NlogN + K + MlogK). ただし N >= K - 1 である. 最初にソートせずに heapify すれば, O(N + (N - K)logN + MlogK). space complexity は O(N).

# step 2

参考にした回答, コメント.

- https://discord.com/channels/1084280443945353267/1195700948786491403/1198906989070258277
  - "priority queue は一回実装しておいてください。" → 実装します.
  - priority queue と heap の違いって何と思って調べたら, priority queue は abstract data type であり, heap はその実装の一つだということだった.
  - あと[quick sort の常識](https://discord.com/channels/1084280443945353267/1200089668901937312/1203725416645271582)についても把握しておく.
- https://discord.com/channels/1084280443945353267/1200089668901937312/1219685867409510670
  - init が O(NlogK). こちらのほうが早い.
  - priority queue の imeplementation がある.
- https://discord.com/channels/1084280443945353267/1192736784354918470/1192793071264473180
  - priority queue の implementation がある.
- https://discord.com/channels/1084280443945353267/1201211204547383386/1203283569493938186
  - 最初に heapify 使うより, 定義した add 使うほうが良いよねってコメントがあるので自分もそうする.
  - priority queue ある.
- [参考 priority queue 実装](https://discord.com/channels/1084280443945353267/1192736784354918470/1194613857046503444)

heap を実装してみるが, エラー処理やどこまでメソッド化するかが難しい.
実装した MyHeap を用いて step2 を実装.
