# step1

time: 14:41

block は 2 \* numRows - 2 の文字からなる. ただし numRows が 1 のときは 1. これを block_size とする.

index % block_size の値によって numRows の配列に追加していき, 最後はそれらを結合することでつくれる. time complexity は O(N), space complexity は O(N)必要になってしまう. 配列の配列を用意しないこともできるが, コードも煩雑になる割に O(1)になるだけ(どうせ output 分の O(N)のメモリは必要). 状況に応じて選択する.

# step2

見た実装, コメント

- https://discord.com/channels/1084280443945353267/1196472827457589338/1196472926862577745
  - "python で string の append は O(N)かかるので, list を使うべき"というのは気づいていなかった…
    - 実装は[ここ](https://github.com/python/cpython/blob/b8d808ddd77f84de9f93adcc2aede2879eb5241e/Objects/unicodeobject.c#L11115)かな
- https://discord.com/channels/1084280443945353267/1199984201521430588/1200685871649787944
  - 自分と同じような形で実装していて, "二重ループのほうが素直では"とコメントされている.
    - 確かに二重ループのほうが, block の中の行きと帰りがわかりやすく表現されるかも?
- leetcode editorial
  - numRows が大きすぎるときは, numRows == 1 の場合と同様直ちに返せば早いしメモリも使わない.

実装してみて, 二重ループのほうが中に break の条件が入って分かりづらく感じた.
