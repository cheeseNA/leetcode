# step1

time: 17:37

またもや inplace と not inplace の 2 種類あるが, inplace で解く.

ある node について考える(その前の node は考えている node と違う値を持つと仮定する). すると, その node を入れるかどうかは, 次の node も同じ値を持つかで決定できる. もし同じ値の場合は違う値か None になるまでループして, 再検証する. 違う場合は, 現在の一番ケツの next をそのノードにして, さらに次のノードを検証する.

最初の node が取り除かれるケースもあるから, sentinel のようなものを用意しておくのが良いだろう.
dummy_head の magic number は何が良いだろうか. いつも magic number の選択で悩む. 今回は dummy_head.val にアクセスしないからなんでもいいか.

一応 step1.py かけたが, もう少しきれいな形になると思う.

dummy_head, current_tail の next を None とし,

```python
if not cursor:
    current_tail.next = None
    break
```

を除いた step1_2.py を書いた.

# step2

参考にした回答, コメント

- Google docs の sample answer 01
  - 自分のコードは cursor を動かして current_tail に適宜追加していく形だが, このコードは currentNode を動かしつつ currentNode.next を張り替えている.
- https://discord.com/channels/1084280443945353267/1195700948786491403/1196681161498447982
  - 綺麗にまとまっているコード. curr と curr.next が同じ値の場合, curr.next が curr と違う値になるように付け替え, last_unique_node.next = curr.next としている. 自分としては, last_unique_node.next がこの時点では unique ではない場合があるのが結構気になる. 後の else 節で last_unique_node = curr と上書きしているから動作上は問題なさそう?
- https://discord.com/channels/1084280443945353267/1195700948786491403/1196701558382018590
  - 上の回答に対するコメント.
  - value_to_remove を使用したスキップはわかりやすくて良い.
  - 一方で, previous = current という代入や, previous の表すものがわかりにくく感じる.
  - 車両の例えがわかりやすい.
- https://discord.com/channels/1084280443945353267/1196472827457589338/1196472926862577745
- https://discord.com/channels/1084280443945353267/1201211204547383386/1201574675638137016
  - while の下に if-else があるときは if で continue したほうが読む負荷が低い, とのこと. 意識する.
- https://discord.com/channels/1084280443945353267/1192736784354918470/1201887965182435368
  - 個人的にしっくり来るが, inplace ではない.
- https://discord.com/channels/1084280443945353267/1192728121644945439/1204829923705884702
- https://discord.com/channels/1084280443945353267/1200089668901937312/1206627151969787985
  - 自分のコードと近いと感じる. わかりやすい.
  - continue を使うのも場合による.
  - 自分の step1.py も, このコードの 2nd-1 のように`if not cursor`の部分を while と同じインデントに下げればきれいに見えるだろう.
  - モジュール化するコメントが参考になる.
  - 1 重ループも読みやすく感じる.
  - C と D の長さで continue を入れたほうが良いかが変わる. また, 関数でくくることで current_value を隠蔽できて良いという指摘. 参考になる.
  - "名前は~長ければ可読性が高いわけじゃない"

step2 に取り組むにあたって

- 2 重ループと１重ループ両方書いてみる.
- モジュール化を試す
- conitune に気をかける
