# step1

time: 30:28

解法は２つ思いつく.

一つは linked list と数字の相互変換メソッドを定義してそれらを使用する方法. time complexity は O(N+M). space complexity は O(1).

もう一つは同時に２つの linked list をたどりつつ新しい linked list を作る方法. time complexity は O(max(N, M)), space complexity は O(1).

わかりやすさをとるか, 定数倍の性能差をとるか.

多分求められているのは後者の方だと思う&前回は前者で実装したので後者で実装してみる. carry に注意. full adder みたいなものになりそう.

l1, l2 が None じゃないかで 2 x 2 = 4 通りある時の条件分岐の書き方がいつもわからない. 素直に 4 つ書くのが無難か.

変数の取り扱いが難しい. node を付け足す処理を共通化するなら digit_sum = None として事前に定義し後々値を入れればいいが, 考慮忘れの条件分岐に進んだとしたら None のままになっているのが怖い.

あと l1 = l1.next しても良いのか. 呼び出し元の l1 が変化してしまうのではないのか. Python の参照渡しとかリテラルに対する勉強が足りない.

l1, l2, carry ともに None のときは, sum_cursor の prev の next 変数を None にしないといけないが, そのためには sum_cursor_prev のような形で以前の位置の cursor を持っておく必要がある. うまく表現できないが, その一つのケースのために prev を持つのは複雑度が増して気持ち悪い感じがする. 代替案として, sum_root_node の一番最初の node は dummy の node を置いて, l1.val + l2.val + carry > 0 の場合はケツに node を追加するような実装にすれば問題なさそう.

なんとかできたが, すごい読みにくいコードな気がする. やはり前者の実装方式のほうが良かったな.

# step2

leetcode の解答を見た感じ, dummy head を用いるというアイデアは良かった.
None を 0 とすることでコードを簡潔にできそうだ.
あと部分問題に分けることで, recursive に解くこともできる.

また, l1 = l1.next としても良いのか問題だが, l1 に再代入しているため問題ない.

https://github.com/Mike0121/LeetCode/tree/main/Arai60/02.%20Add%20Two%20Numbers
https://github.com/hayashi-ay/leetcode/pull/24/files
こちらを参考に, recursive と loop 版で実装してみる.

recursive で実装するときに, carry を考慮した関数を作るが, これはどこに置けばいいだろうか. メソッド内に関数を書くのはあまり経験がないので違和感を感じるが, carry を考慮した関数は外から呼び出すことはないので, メソッド内に書くのが良いのかもしれない.

条件分岐もなくなり, digit_sum = None と初期化する問題も解消された.
