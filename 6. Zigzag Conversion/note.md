# step1

time: 14:41

block は 2 \* numRows - 2 の文字からなる. ただし numRows が 1 のときは 1. これを block_size とする.

index % block_size の値によって numRows の配列に追加していき, 最後はそれらを結合することでつくれる. time complexity は O(N), space complexity は O(N)必要になってしまう. 配列の配列を用意しないこともできるが, コードも煩雑になる割に O(1)になるだけ(どうせ output 分の O(N)のメモリは必要). 状況に応じて選択する.
