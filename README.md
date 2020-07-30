# madplot
yaml形式のファイルを読み込んでmatplotlibで作図するための自作スクリプト。

**現段階ではcsv形式しかサポートしてません。**

example_dataに存在するファイルを参考

# 必要環境
python3以降 (3.8推奨)

# 使い方
## ダウンロード

```
git clone git@github.com:naka345/madplot.git
```

もしくは、githubのトップページ -> code -> Download ZIP をクリック


## インストール
pandasやfireなどを使用しているため依存ライブラリをインストールする

* pipenv

```
pipenv install
pipenv shell
```

* pip

```
pip install -r requirement.txt
```

## データファイルの設置
csvファイルをyamlファイルで指定した場所に設置する。

初期値だと`example_data`に置けば`output`に出力される。

エラーバー出力のための偏差値の計算は、読み込みに指定したファイルで行う

## コマンド

* 初期値で使う場合

```
python main.py madplot
```

* 設定ファイルを個別に指定する場合
```
python main.py madplot --config_path example.yaml
```

* エラーバーの有無
デフォルトは `True`
```
python main.py madplot --std_err False
```


# 設定ファイル
config_template.ymlを元に説明。

使用時はconfig_template.ymlからコピーし `--config_path` オプションを使用するのが望ましい。

`rcParams`キー以下の設定値の詳細に関しては[公式のサンプル](https://matplotlib.org/tutorials/introductory/customizing.html#matplotlibrc-sample)を参考にされたし

また、matplotlibを使う上では `figure`,`axes`などのオブジェクト指向を避けて通れないので
[Matplotlib 1.5.1のFAQ > Usage](https://matplotlib.org/1.5.1/faq/usage_faq.html#parts-of-a-figure)を参考

```
datafile:
  filedir: example_data   # データファイルがあるディレクトリ
  files: '*.csv'          # ファイル名。*でディレクトリ内部のファイ全指定。複数指定の場合は ","区切りで指定
figure:
  rcParams:
    figure.figsize: 6.4, 4.8    # 横幅, 縦幅 (インチ)
    figure.dpi: 300             # 解像度
    figure.facecolor: white     # 図の表面の配色
    figure.edgecolor: white     # 図の淵の配色
  linewidth: 0    # 淵の太さ
font:
  rcParams:
    font.family: Arial    # 文字フォント
    font.size: 10.0       # 文字サイズ
axes:
  title:
    specific: False           # 図のタイトルの明記の有無。Falseなら読み込んだファイル名を使用。
    name: same_input_filename # specificが Trueの場合のみ、ここで指定したタイトルを使用する。
  rcParams:
    axes.titlesize: large   # タイトルサイズ。数値で直接指定も可
    axes.titlecolor: auto   # タイトルの配色
  scale:
    xscale: linear                  # x軸の線形・対数スケールの指定
    yscale: log                     # y軸の線形・対数スケールの指定
    ticker: LogFormatterExponent    # 目盛りの表記の指定。matplotlib.ticker参照
lines:
  rcParams:
    lines.marker: o           # 線上のマーカーの形状
    lines.linewidth: 1.0      # 線の太さ
    lines.linestyle: solid    # 線の形状
errbar:
  elinewidth: 0.5     # エラーバーの線の太さ
  ecolor: black       # エラーバーの配色
  capsize: 4.0        # 矢尻の幅
  capthick: 1.0       # 矢尻の厚さ
  barsabove: False    # エラーバーをマーカーに重ねるか否か
legend:
  legend: True    # 凡例の有無
axis:
  xlabel: Hours post infection          # x軸のラベル名
  ylabel: Virus titer (log10 PFU/mL)    # y軸のラベル名
output:
  dir: output                       # 作図出力先のディレクトリ
  title:
    specific: False                 # ファイル名の明記の有無。Falseなら読み込んだファイル名を使用。
    filename: same_input_filename   # specificが Trueの場合なら指定したタイトルを使用する。複数出力する場合は連番表記
  extension: png                    # ファイルの拡張子の指定
```

## rcParamsの追加変更
[matplotlibrc](https://matplotlib.org/tutorials/introductory/customizing.html#matplotlibrc-sample)で変更できる項目に限り

以下のようにyamlファイルを編集することで変更が可能。

```
custom:
  rcParams:
    figure.hoge: fuga
    lines.hoge: fuga
...
```
