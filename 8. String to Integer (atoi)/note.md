# old.py

以前解いたときのコードです

# step1.py

time: 17:33

言われたことをやれば実装できそうな問題. time complexity は O(n)で, space complexity は O(1).

処理をどこまで細かくメソッド化すべきかが難しい. clamp は分けたが, leading space の処理も同様に分けるべきかどうか.
他に同じようなパーサーっぽいメソッドがあれば共通化するべきだろう.

エラー処理については, raise や None を返すなどいくらか手法が考えられるが 今回は None を返すことにする.
