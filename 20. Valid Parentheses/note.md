# step 1

まず, s の長さが奇数のときは not valid.

閉じカッコは, 一番最後の開きカッコと対応していれば消せる. いちばん最後の閉じカッコまで消せて, なおかつ開カッコがのこってなければ valid.

deque のメソッド名を覚えていない.

あと list と比べてどこが高速か正確に把握してない.

else 節の方に return False の if 節が２つはいるのが少し気持ち悪い

# step 2

見た回答, コメント

- Google docs sample answer
  - 自分のコードも if の後の else が長いので, continue してもいいかも
  - "最後まで行ったら True"というのは分かりやすいかも
  - "チョムスキー階層"
    - 今回の問題はプッシュダウン・オートマトンっぽいので, [wiki](https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC%E9%9A%8E%E5%B1%A4)を参考にするとチョムスキー階層ではタイプ 2 に位置しそう. 数字が大きいほど制約が厳しいので, 今回の問題は比較的単純?といえる.
- https://discord.com/channels/1084280443945353267/1201211204547383386/1202541275115425822
  - 問題を読んで, 文脈自由言語だ, だからプッシュダウンオートマトンで書けそうだぞという順番か.
    - 生成文法において右側に非終端記号が来るのが文脈自由言語?
- https://discord.com/channels/1084280443945353267/1200089668901937312/1205458618036781057
- https://discord.com/channels/1084280443945353267/1206101582861697046/1216810547811450962

deque vs list

- "memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction."
- "Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation."
- deque は双方向 linked list で, list は可変長 array.
- 今回のケースでは stack として使うのでどちらでも良い.
