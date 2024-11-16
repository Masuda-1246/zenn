---
title: "XMindファイルをMarkdownに変換するPython作成してみた！〜Mapifyを無料で使い倒す〜"
emoji: "🐡"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "markdown", "生成AI", "mindmap", "mermaid"]
published: true
---
## はじめに
皆さんはマインドマップツール「Mapify」を使ったことがありますか？Mapifyは、プロンプトやPDF、YouTube動画、URLを入力するだけで瞬時にマインドマップを作成してくれます。内容が構造化されていて理解するのに、とても便利です。特に、論文や海外のサイトの内容を理解する際に、Mapifyをよく利用しています。
https://mapify.so/?ref=yousukemasuda-wczxr2
無料で使えるのですが、一つだけ問題があります。それは、Mapifyで作成したマインドマップは数日間しか保存することができないのです（課金すればいいのですが...）。
Xmindファイルは保存することができるのですが、普段からXmindはあまり使っていないので、別のファイル形式に変換する方法を探していました。
そこで、Pythonを使って、**XMindファイルをMarkdown形式**（Markmap用）**とMermaid記法形式**（Mermaid.js用）に変換するスクリプトを作成しました！この記事では、そのスクリプトの実装方法や活用例について解説します。

---

## GitHub
https://github.com/Masuda-1246/xmind_to_markdown

## プログラムの概要

このプログラムでは、以下の3種類のスクリプトを用意しました：

1. **xmind2both.py**  
   - Markdown形式とMermaid記法形式の両方を生成。
   - `output/markdown`と`output/mermaid`ディレクトリに保存。

2. **xmind2markdown.py**  
   - Markdown形式（Markmap用）のみを生成。
   - `output/markdown`ディレクトリに保存。
   - VSCodeの拡張機能「Markmap」で表示可能。
  https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode

3. **xmind2mermaid.py**  
   - Mermaid記法形式のみを生成。
   - `output/mermaid`ディレクトリに保存。
   - Notionで表示可能。

また、これらのスクリプトは、**`input`ディレクトリ内のXMindファイルを処理し、変換後に削除する仕様**になっています。

---

## 使用した技術とライブラリ

### 使用言語
- **Python 3.6以上**

### 必要ライブラリ
- **xmindparser**  
  XMindファイルをPythonで読み取るためのライブラリ。

インストール方法：
```bash
pip install xmindparser
```

---

## 実装の解説

### ディレクトリ構成

スクリプトの実行前後で、以下のようなディレクトリ構成を採用しています：

#### 実行前
```
project/
├── xmind2both.py
├── xmind2markdown.py
├── xmind2mermaid.py
├── input/
│   └── example.xmind
└── output/  (空)
```

#### 実行後
```
project/
├── xmind2both.py
├── xmind2markdown.py
├── xmind2mermaid.py
├── input/  (空)
└── output/
    ├── markdown/
    │   └── example.md
    └── mermaid/
        └── example.md
```

---

### スクリプトの詳細

#### 1. XMindファイルのMarkdown変換

`xmind2markdown.py`では、XMindファイルをMarkdown形式に変換します。

##### Markdown変換用の関数
```python
def convert_to_markdown(data, level=1):
    """
    再帰的にXMindデータをMarkdown形式に変換
    """
    md_content = ""
    for topic in data:
        # Markdownの見出しレベル
        md_content += f"{'#' * level} {topic.get('title', 'Untitled')}\n\n"

        # メモ (notes) の追加
        if 'note' in topic:
            md_content += f"{topic['note']}\n\n"

        # 子トピックが存在する場合
        if 'topics' in topic:
            md_content += convert_to_markdown(topic['topics'], level + 1)

    return md_content
```

この関数では、再帰的にXMindのトピック構造をたどり、Markdownの階層構造（`#`）に変換しています。

---

#### 2. XMindファイルのMermaid変換

`xmind2mermaid.py`では、XMindファイルをMermaid記法形式に変換します。

##### Mermaid変換用の関数
```python
def convert_to_mermaid(data, level=1):
    """
    再帰的にXMindデータをMermaid mindmap形式に変換
    """
    mermaid_content = ""
    indent = "  " * level  # インデント管理
    for topic in data:
        # ノードのタイトルを取得
        title = topic.get("title", "Untitled")
        mermaid_content += f"{indent}{title}\n"

        # 子トピックが存在する場合
        if "topics" in topic:
            mermaid_content += convert_to_mermaid(topic["topics"], level + 1)

    return mermaid_content
```

---

#### 3. 両方を同時に変換

`xmind2both.py`では、Markdown形式とMermaid記法形式の両方を生成します。以下は、両方を生成するディレクトリ処理のコードです：

```python
def process_directory(input_dir, markdown_output_dir, mermaid_output_dir):
    """
    inputディレクトリ内のすべてのXMindファイルを処理してoutputディレクトリに保存。
    処理後、inputディレクトリ内のファイルを削除。
    """
    if not os.path.exists(markdown_output_dir):
        os.makedirs(markdown_output_dir)
    
    if not os.path.exists(mermaid_output_dir):
        os.makedirs(mermaid_output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".xmind"):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            markdown_output_file_path = os.path.join(markdown_output_dir, output_file_name)
            mermaid_output_file_path = os.path.join(mermaid_output_dir, output_file_name)

            # XMindファイルをMarkdownに変換
            xmind_to_md(input_file_path, markdown_output_file_path)

            # XMindファイルをMermaid形式に変換
            xmind_to_mermaid(input_file_path, mermaid_output_file_path)

            # 処理済みファイルを削除
            os.remove(input_file_path)
            print(f"処理完了: {file_name} -> {output_file_name} (削除済み)")
```

---

### 出力例

#### Markdown
```markdown
# プロジェクトA

## サブタスク1

## サブタスク2
```

#### Mermaid
```mermaid
%%{init:{'theme':'default'}}%%
mindmap
  top((プロジェクトA))
    サブタスク1
    サブタスク2
```


---

## 活用例

- **Markmap**: Markdown形式をリアルタイムにマインドマップ表示。
- **Mermaid.js**: Mermaid記法を使ったWebアプリでの可視化。

---

## おわりに

今回紹介したスクリプトは、XMindデータをMarkdownやMermaid記法で再利用する際に非常に便利です。
手軽にマインドマップをドキュメント化したり、Web上での可視化に役立ちます。ぜひ試してみてください！

何か質問やフィードバックがあれば、コメントで教えてください！