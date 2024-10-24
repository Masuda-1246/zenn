---
title: "zennの記事を作成するツール作ってみた"
emoji: "📘"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["zenn", "gpt", "llm", "nextjs", "v0"]
published: true
---
## TL;DR
この動画をご覧ください
https://youtu.be/USWBTOucO80

## 動機
皆さんは調べ物やエラー解決をする際、どのような順序で進めていますか？  
僕はまずGoogleで検索し、QiitaやZenn、Stack Overflowなどのコミュニティサイトを参照し、それでも解決しない場合は公式ドキュメントを読んでいます。  
最近では、ChatGPTやClaude.aiといったAIモデルを利用して調べることもあります。

以前は、調べた内容をNotionにメモしていましたが、あることに気づきました。  
**Notionにメモしても、調べる時には全然参照していない**ことに。

同じエラーで何度もつまずいているのに、Notionは一切確認していないという現実に気付き、最近は調べ物をした際には**Zennに記事を書く**ようにしています。  
Zennに記事を書くことで、次に同じ問題に直面した時に助けになるし（ZennはSEOが強い）、他の人の役にも立つかもしれません。

そんなわけで、最近はZennの記事を書く機会が増えたのですが、やはり記事を書くのには時間がかかります。  
そこで、**記事を書いてくれるツールを作ってみました**。

## GitHubリポジトリ
ツールはこちらのリポジトリで公開しています：
https://github.com/Masuda-1246/zenn-maker

## 用意するもの
- Zennのアカウント
- GitHubのアカウント
- OpenAIのアカウント（APIキーが必要です）

## 事前準備

### 1. ZennをGitHubと連携させる
[この記事](https://zenn.dev/zenn/articles/connect-to-github)を参考に、ZennとGitHubを連携させます。  
レポジトリ名は、できれば`zenn`にしておいてください。

### 2. GitHubアプリを作成
次に、GitHubのAppsを作成します。作成したアプリをフォークしたレポジトリや、Zennに記事を保存するレポジトリにインストールしてください。  
詳細は[こちらの記事](https://zenn.dev/suzutan/articles/how-to-use-github-apps-token-in-github-actions)を参考に設定します。

### 3. GitHub Secretsと環境変数の設定
GitHubに以下の環境変数とSecretsを設定します。

#### Secrets
- `APP_ID`: GitHub AppのID
- `PRIVATE_KEY`: GitHub Appのプライベートキー
![](/images/zenn-maker/github-0.png)
#### 環境変数
- `DESTINATION_REPO`: Zennの記事を保存しているレポジトリ（例: `Masuda-1246/zenn`）
- `DESTINATION_REPO_BASE_BRANCH`: ベースブランチ（例: `main`）
- `DESTINATION_REPO_HEAD_BRANCH`: ヘッドブランチ（例: `zenn-maker`）
![](/images/zenn-maker/github-1.png)

## セットアップ方法

1. このリポジトリをフォーク
2. フォークしたリポジトリをローカルにクローン
3. `npm install`を実行
4. `.envrc.example`を参考に環境変数を設定
   - `OPENAI_API_KEY`: OpenAIのAPIキー
   - `OPENAI_MODEL`: 使用するOpenAIモデル（例: `gpt-3.5-turbo-0125`）
5. `npm run dev`を実行

## 使い方

1. [localhost:3000](http://localhost:3000) にアクセスします。
   ![](/images/zenn-maker/zenn-maker-0.png)

2. 調べたいことやエラー内容をテキストエリアに入力し、`Send`ボタン（またはCtrl + Enter）をクリックします。
   ![](/images/zenn-maker/zenn-maker-1.png)

3. AIが回答を生成しますので、少し待ちます。
   ![](/images/zenn-maker/zenn-maker-2.png)

4. 問題が解決したら、`Generate Blog Post`ボタンをクリック。
5. ファイル名を入力し、`Generate`ボタンをクリック。
   ![](/images/zenn-maker/zenn-maker-3.png)

6. しばらく待つと、記事が生成されます。
   ![](/images/zenn-maker/zenn-maker-4.png)

7. 記事が気に入ったら、`Save Blog Post`ボタンをクリック。
8. 記事が`data/articles`に保存されます。
   ![](/images/zenn-maker/zenn-maker-5.png)

9. `git push`を実行。
10. Zennの保存先レポジトリにPRが自動で作成されます。
    ![](/images/zenn-maker/zenn-maker-6.png)

11. PRをマージすると、記事が公開されます。
    ![](/images/zenn-maker/zenn-maker-7.png)

## 構成技術
- Next.js
- OpenAI
- GitHub Actions
- V0

## まとめ
このツールを使うことで、記事を書く作業が劇的に楽になりました。もはや楽を通り越して怠けているかもしれませんが…。  
今回はローカルで動かす簡単なアプリですが、興味がある方はPRを送っていただけると嬉しいです！  
フォークして使って問題ありませんが、バグや改善点があれば、ぜひIssueを立ててください。
自分なりにカスタマイズして、使いやすいように改善してみてください！
