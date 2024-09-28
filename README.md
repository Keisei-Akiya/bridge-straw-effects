# 離島架橋の介入効果

## 著者

穐谷慶成

## プロジェクトの概要

離島架橋は離島の人口にどういった影響を与えるのか．

## ディレクトリ構造の説明

```text
bridge_straw_effects/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── figures/
│   ├── manuscript/
│   └── tables/
├── references/
├── results/
└── src/
    ├── data_cleaning/
    ├── analysis/
    └── visualization/
```

### ディレクトリの説明

- `src/`: すべてのソースコードを格納

  - `data_cleaning/`: データの前処理用スクリプト
  - `analysis/`: 統計分析用スクリプト
  - `visualization/`: 図表作成用スクリプト

- `data/`: データファイルを格納

  - `raw/`: 元のデータセット
  - `processed/`: クリーニング済みのデータセット

- `docs/`: 論文関連のファイルを格納

  - `manuscript/`: 論文本体のマークダウンファイル
  - `figures/`: 論文に使用する図表
  - `tables/`: 論文に使用する表

- `results/`: 分析結果の出力ファイルを格納

- `references/`: 参考文献や引用文献のリストを格納

## 依存関係

本プロジェクトの依存関係は `pyproject.toml` ファイルに記載されている．
主な依存関係は以下の通り:

- Python 3.10 以上
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- scikit-learn
- pymc

詳細な依存関係とバージョン情報については `pyproject.toml` ファイルを参照．

### 環境のセットアップ

1. Poetry がインストールされていることを確認．
2. プロジェクトのルートディレクトリで以下のコマンドを実行し，依存関係をインストールする:

   ```bash
   poetry install
   ```

3. 仮想環境を有効化するには，以下のコマンドを使用する．

   ```bash
   poetry shell
   ```

これにより，プロジェクトに必要なすべての依存関係がインストールされ，適切な環境が設定される．
