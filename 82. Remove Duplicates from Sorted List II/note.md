# step1

time: 17:37

またもや inplace と not inplace の 2 種類あるが, inplace で解く.

ある node について考える(その前の node は違う値を持つと仮定する). すると, その node を入れるかどうかは, 次の node も同じ値を持つかで決定できる. もし持っていた場合は違う値か None になるまでループして, 再検証する. 持っていない場合は, 現在の先端の next をそのノードにして, 次のノードを検証する.

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
