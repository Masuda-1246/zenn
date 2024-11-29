---
title: "HumanLayer触ってみた~Human In The Loopのプラットフォーム~"
emoji: "👏"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["humanlayer", "AI", "NLP", "hitl"]
published: false
publication_name: "nislab"
---

# TL;DR
HumanLayer(Human In The Loopの初？のプラットフォーム)の簡単なチュートリアルを紹介します。
以下のような動画のような感じで、AIエージェントが人間の承認を得るプロセスを体験できます。
![](/images/2024-11-29-humanlayer-1/demo.gif)

# HumanLayerとは？
## 概要
HumanLayerは、AIエージェントが重要な機能を実行する際に人間の監督を保証するためのプラットフォームです。
具体的には、Slackやメールなどを通じて承認ワークフローを構築し、人間のフィードバックをリアルタイムで取り入れることができます。
これにより、AIエージェントが高リスクの決定を行う際に、人間の判断を組み込むことが可能になります。

### 主な特徴

- 人間のフィードバックと承認: AIエージェントが重要な決定を行う際に、人間のフィードバックを求めることができます。
- 多様なフレームワークとの互換性: LangChain、CrewAI、ControlFlow、LlamaIndex、Haystackなど、さまざまなフレームワークと連携可能です。
- 主要なAIモデルのサポート: OpenAI、Claude、Llama3.1、Mistral、Gemini、CohereなどのAIモデルをサポートしています。

## Human In The Loopの重要性
「Human In The Loop」は、AIシステムが自律的に動作するだけでなく、人間の介入を必要とするプロセスを指します。
これにより、AIの判断が人間の倫理観や価値観に沿ったものとなり、特に高リスクの状況での信頼性が向上します。
HumanLayerは、この「Human In The Loop」アプローチを実現するための強力なツールです。

### 利用例
- 営業やマーケティング: AIエージェントが新しいリードを見つける際に、人間がSlackでフィードバックを提供することで、より効果的な営業活動が可能になります。
- カスタムエージェントの開発: 専門家のアドバイスを受けながら、営業、マーケティング、採用などのカスタムエージェントを構築できます。

## プランと価格
HumanLayerは、以下のようなプランを提供しています。

- スタータープラン: ハッカーやティンカー向けに無料で提供され、月に100リクエストまで無料。その後は200リクエストごとに20ドル。
- エージェントツールキット: 月額500ドルで、HumanLayerのブランディングを除去し、2000の操作を含む。追加の操作は200ごとに18ドル。
- カスタムプラン: プライベートVPCやオンプレミスでの展開が可能で、RBACやSSOのサポート、ボリュームディスカウントなどが含まれます。

# 使い方
### 1. HumanLayerにアクセス
以下のサイトにアクセスして、HumanLayerにサインアップします。
https://www.humanlayer.dev/

### 2. プロジェクトの作成
プロジェクトの作成は、「New Project」を押します。

![](/images/2024-11-29-humanlayer-1/humanlayer-1.png)

### 3. プロジェクトの設定
Name, Descriptionなどを入力して、「Save」を押します。

![](/images/2024-11-29-humanlayer-1/humanlayer-2.png)

### 4. ローカルでセットアップ
新しいディレクトリを作成し、そのディレクトリに移動します。
```bash
mkdir my_project
cd my_project
touch main.py
touch .envrc # direnvの設定ファイル
```
私はdirenvを使って環境変数を管理していますが、お好きな方法で環境変数を設定してください。
https://zenn.dev/masuda1112/articles/2024-11-29-direnv

### 5. 環境変数の設定
.envrcファイルに以下の行を追加します。
```bash
export HUMANLAYER_API_KEY="YOUR_HUMANLAYER_API_KEY"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```
OPENAI_API_KEYは、OpenAIを設定してください、
HUMANLAYER_API_KEYは、先ほどのプロジェクトに表示されているものを使ってください

![](/images/2024-11-29-humanlayer-1/humanlayer-4.png)

### 6. 依存関係のインストール
```bash
pip install langchain langchain-openai humanlayer
```

### 7. コードの記述
main.pyに以下のコードを記述します。
```python
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from humanlayer.core.approval import ApprovalMethod, HumanLayer

hl = HumanLayer.cloud(verbose=True)

# add can be called without approval
@tool
def add(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y


# but multiply must be approved by a human
@tool
@hl.require_approval()
def multiply(x: int, y: int) -> int:
    """multiply two numbers"""
    return x * y


tools = [add.as_tool(), multiply.as_tool()]

llm = ChatOpenAI(model="gpt-4o", temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    handle_parsing_errors=True,
)


def main():
    result = agent.run("2と5を掛け、その結果に32を足す。")
    print("\n\n----------Result----------\n\n")
    print(result)


if __name__ == "__main__":
    main()
```

このコードを実行すると、エージェントはまず`multiply`関数を呼び出そうとしますが、この関数には人間の承認が必要です。承認が得られると、`multiply`関数が実行され、その結果に対して`add`関数が適用されます。最終的な結果が出力されます。


### 8. 実行
```bash
python main.py
```
実行すると以下のようになります。
```
> Entering new AgentExecutor chain...

Invoking: `multiply` with `{'x': 2, 'y': 5}`


HumanLayer: waiting for approval for multiply via humanlayer cloud
```

`multiply`関数は人間の承認が必要なので、HumanLayerのダッシュボードに移動して承認を行います。

![](/images/2024-11-29-humanlayer-1/humanlayer-5.png)

![](/images/2024-11-29-humanlayer-1/humanlayer-6.png)

承認が完了すると、コードが正常に実行されます。

```
> Entering new AgentExecutor chain...

Invoking: `multiply` with `{'x': 2, 'y': 5}`


HumanLayer: waiting for approval for multiply via humanlayer cloud


--- ここから ---
HumanLayer: human approved multiply
10
Invoking: `add` with `{'x': 10, 'y': 32}`


422と5を掛けた結果に32を足すと、42になります。

> Finished chain.


----------Result----------


2と5を掛けた結果に32を足すと、42になります。
```

# 終わりに
HumanLayerは、AIエージェントの信頼性と安全性を高めるための「Human In The Loop」アプローチを実現する革新的なプラットフォームです。
AI技術がますます複雑化する中で、人間の判断を組み込むことで、より安全で信頼性の高いAIシステムの構築が可能になります。

何か質問やフィードバックがあれば、コメントで教えてください！