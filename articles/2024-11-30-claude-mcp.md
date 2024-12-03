---
title: "ClaudeのMCP(Model Context Protocol)をMacで触ってみた"
emoji: "📌"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["claude", "mcp", "ai", "mac", "llm"]
published: true
publication_name: "nislab"
---

## TL;DR
Model Context Protocol (MCP)を使用してMac上でBrave SearchとFilesystemに接続する方法を紹介します。
MCPはAIアシスタントとデータソースを簡単に接続できる新しいプロトコルで、Brave SearchやMacのファイルシステムとの連携が可能になります。

## 私たちの研究室(NISLab)
https://nisk.doshisha.ac.jp/

## アドベントカレンダー  1日目~
https://nislab-advent-calendar-2024-12.vercel.app/

## Model Context Protocolとは
Model Context Protocol (MCP)は、Anthropicが2024年11月25日に発表した新しいオープンスタンダードです。このプロトコルは、AIアシスタントと様々なデータソースを簡単に接続することを可能にします。MCPを使用することで、AIシステムは必要なデータにアクセスしやすくなり、より関連性の高い応答を生成できるようになります。

## MacでMCPを使用するための準備

MCPを使用するには、以下の手順を実行します:

1. Claude Desktop アプリケーションをMacにインストールします。

https://claude.ai/download
2. Brave APIにログインします

https://brave.com/search/api/

3. 「API Keys」タグを押します
![](/images/2024-11-30-claude-mcp/brave-1.png)

4. 「Subscriptions」を押します
![](/images/2024-11-30-claude-mcp/brave-2.png)

5. Freeを選択します
![](/images/2024-11-30-claude-mcp/brave-3.png)

6. 登録が完了すると次のようになります
![](/images/2024-11-30-claude-mcp/brave-4.png)

7. もう一度「API Keys」タグを押します
![](/images/2024-11-30-claude-mcp/brave-5.png)

8. 「Add API key」を押します 
![](/images/2024-11-30-claude-mcp/brave-6.png)

9. Nameを入力し、「Add」を押します
![](/images/2024-11-30-claude-mcp/brave-7.png)

10. 作成されたAPIキーをコピーしておきます

11. Claude Desktopアプリケーションを開きメニューバーの「Claude」>「Settings」にアクセスします
![](/images/2024-11-30-claude-mcp/claude-1.png)

12. Developer > Edit Configを押します
![](/images/2024-11-30-claude-mcp/claude-2.png)

13. Finderが開くのでclaude_desktop_config.jsonを開きます
![](/images/2024-11-30-claude-mcp/claude-3.png)

14. ファイルの中身を一旦削除し、以下のように書き換えます
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/<username>/Desktop"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"　//ここに先ほどコピーしたAPIキーを貼り付けます
      }
    }
  }
}
```

::: message
usernameの確認方法は、ターミナルを開き、`whoami`と入力すると表示されます。
:::

15. 保存して、Claude Desktopアプリケーションを再起動します

16. 再起動するとチャット欄の右下に金槌と11の数字が表示されます（これでMCPが有効になりました）
![](/images/2024-11-30-claude-mcp/claude-4.png)

17. チャット欄に「brave search」や「filesystem」などのキーワードを入力して、MCPを使用してBrave SearchやMacのファイルシステムにアクセスできることを確認します


## Demo
実際に試してみました。
![](/images/2024-11-30-claude-mcp/demo-1.png)
![](/images/2024-11-30-claude-mcp/demo-2.png)
Desktopにファイルが作成され、開くと以下のようなCSVファイルが作成されていました。
![](/images/2024-11-30-claude-mcp/demo-3.png)

## 最後に
Claudeのmcpにはまだまだ、機能が沢山あるので、興味があれば以下のリンクを参照してください。
https://github.com/modelcontextprotocol/servers?tab=readme-ov-file


## 参考文献
https://www.anthropic.com/news/model-context-protocol
https://zenn.dev/acntechjp/articles/483747f8e89ad8
https://github.com/modelcontextprotocol/servers?tab=readme-ov-file
https://www.youtube.com/watch?v=eHrp9hKZed8