## Python 環境

```
python -m venv cordinate-matching
source cordinate-matching/bin/activate
```

## run1

- シンプルな方法
  - タスクをそのまま実装する

- 条件を満たすレコードの数をカウントする
- 簡単のために、(x,y) のそれぞれが取りうる範囲を `[0, 512)` から `[0, 8)` に変更している
  - これはヒットする件数が 512 だとあまりに少なかったため
  - この値の範囲自体は計算コストに影響は与えないはず
- 簡単のために、条件の座標マッチング数を 50 に変更している
  - これはヒットする件数が 80 だとあまりに少なかったため
  - この値自体は計算コストに影響は与えないはず

- 一致の条件は次の通り

```
sqrt(power(var.x - xi, 2) + power(var.y - yi, 2)) <= 50
```

- 結果（N=30）

```
結果: 1000000 -> 93681 (0.094)
run took 0.92611312s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.88726629s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89997054s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.85944538s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.86084054s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.87665304s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.86311421s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.88739363s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.91842471s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89189683s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89926633s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90185354s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90598867s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89053767s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.88408371s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89140388s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.91663854s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.92787146s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89164583s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.93433479s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.92709746s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90941300s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90783817s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90397029s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89552712s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.90323237s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.87904379s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.86699058s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.85702925s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.86260525s to execute
結果: 1000000 -> 93681 (0.094)
run took 0.89894404s to execute
平均：0.8933440446853638, 標準偏差：0.021127797663211823
```

## run2

- 「距離が2以内」という条件でかつ「座標が整数」なので、L2 距離を使わなくても L1 距離で適切に絞り込むことができる

- 結果（N=30）
  - 実行時間が 86.5 % になったが、標準偏差がやや高くなった

```
run took 1.07975808s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.97385979s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.97027942s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.72767633s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.72145246s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.83378067s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.85937354s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.93805300s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.70749454s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69379604s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69510021s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.68349996s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69134175s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.75488042s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.97472442s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.72903154s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.87849971s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.99005179s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.73195387s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69446367s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69741096s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.68880462s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69156567s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.70167946s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.71201558s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69485588s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.70567033s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.91702017s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.71200779s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.69388454s to execute
結果: 1000000 -> 82252 (0.082)
run took 0.74127833s to execute
平均：0.7735168933868408, 標準偏差：0.10721087455749512
```

## run3

- GPUを使うパターン
  - 今回は m2 macbook でテストしているので、`mps` にしているが、NVIDIA など使うのであれば `cuda:0` など使う

- 結果
  - run2 と比べて実行時間が 22.3 % になった

```
結果: 1000000 -> 76059 (0.076)
run took 1.56014771s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.33377871s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16999112s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.17310967s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16594700s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16676708s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16607708s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16575042s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16564250s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16661908s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16590004s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16583021s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16642283s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16602717s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16575050s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16584138s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16555392s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16580546s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16640192s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16550658s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16591471s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16746971s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16902333s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16773858s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16676754s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16639296s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16558946s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16667475s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16690971s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.17399042s to execute
結果: 1000000 -> 76059 (0.076)
run took 0.16836804s to execute
平均：0.1725853979587555, 標準偏差：0.03051469288766384
```

### run3-2

- GPU を使うパターン
  - Google Colab の T4 GPU を使った

- 結果
  - run3 と比べて実行時間が 56.4 % になった

```
結果: 1000000 -> 84262 (0.084)
run took 0.10246847s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09815738s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09806870s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09730842s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09724911s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09722216s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09710515s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09718760s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09722531s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09729785s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09717734s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09709418s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09784549s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09720748s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09727443s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09798980s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09715848s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09706216s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09716949s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09722239s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09727548s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09714040s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09691630s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09699612s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09714911s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09722277s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09723583s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09696302s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09714557s to execute
結果: 1000000 -> 84262 (0.084)
run took 0.09720837s to execute
平均：0.0974581390619278, 標準偏差：0.0009954659035429358
```