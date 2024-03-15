解いた問題だったので解法は知っていた.

# step1

time: 09:30

とりあえず O(N^2)案は思いつく.

表れた数字を set に持っておけば, 数字を見たときに target-num がすでに表れてるか O(1)でチェックできる.

time complexity は O(N)

space complexity は O(N)

only one valid answer exists とのことなので error 処理は考えなくて良い. しかし return None はいかがなものか

命名が不安だ, set まで変数名に含めるべきか.

indices というのを見ていなくて 1 エラー. それに伴い set も hashmap に変更.

# step2

他の人の解法などを見て改善点を考える.

return None は type annotation と合わないので[]を採用することにした. 実務上本来どうするべきなのかはまだ分からない.

ほかは appeared_number_to_index の命名だが, \_table としている人もいた. table であることは{}で初期化しているためなくても良いかと思い, そのままにした.
