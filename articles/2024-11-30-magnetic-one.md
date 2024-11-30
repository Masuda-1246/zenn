---
title: "Magentic-Oneとは？: 複雑なタスクを解決する汎用マルチエージェントシステム"
emoji: "📝"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["ai", "エージェント", "マルチエージェントシステム", "microsoft", "llm"]
published: true
---

## TL;DR
Magentic-Oneは、Microsoft Researchによって開発された新しいマルチエージェントシステムで、複雑なタスクを自律的に解決することを目的としています。
中心となる「オーケストレーター」エージェントが、専門のエージェントを調整し、ウェブブラウジングやファイル操作、コーディングなどのタスクを実行します。
このシステムはオープンソースで提供されており、開発者や研究者が多様なアプリケーションを構築するための基盤となります。
詳しくは、以下のリンクを参照してください。
https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/

## はじめに
Magentic-Oneは、従来のAIエージェントの限界を超え、複雑なタスクを効率的に処理するために設計された汎用マルチエージェントシステムです。
このシステムは、専門的な役割を持つ複数のエージェントが協力し合い、タスクを遂行します。

## システムの構成
Magentic-Oneは、以下の5つのエージェントで構成されています：

- **オーケストレーター (Orchestrator)**: タスクの全体計画を立て、進捗を監視し、必要に応じてタスクを再配分します。
  
- **ウェブサーファー (WebSurfer)**: ウェブページをナビゲートし、情報収集やフォーム入力を行います。
  
- **ファイルサーファー (FileSurfer)**: ローカルファイルの操作を担当し、必要な情報を抽出します。
  
- **コーダー (Coder)**: プログラムのコードを作成し、他のエージェントから得た情報をもとに新しい処理を行います。
  
- **コンピュータ端末 (ComputerTerminal)**: コードの実行やシェルコマンドの処理を担当します。

このようなモジュール設計により、Magentic-Oneは柔軟性と拡張性を持ち、特定のタスクに応じてエージェントを追加または削除することが可能です。

## パフォーマンス評価
Magentic-Oneは、GAIA、AssistantBench、WebArenaの3つのベンチマークで評価され、他の最先端システムと比較して堅実な性能を示しました。
これにより、複雑なタスクに対する処理能力が証明されています。

## リスクと課題
Magentic-Oneは高い性能を発揮する一方で、以下のようなリスクも伴います：

- **誤った操作によるアカウントの停止**。
- **人間の助けを求めるための不適切な行動**。

これらのリスクを軽減するために、開発チームはエラー回復機能やタスクの再割り当て機能を実装しています。

## 今後の展望
Magentic-Oneの開発チームは、エージェントの安全性と倫理的な側面についての研究を続ける必要があると強調しています。
特に、エージェントが自らの行動の可逆性を評価する能力を向上させることが重要です。

## 最後に
Magentic-Oneは、複雑なタスクを自律的に解決するための新しいアプローチを提供します。
高い柔軟性と効率性を持つこのシステムは、今後のAIの発展において重要な役割を果たすことが期待されています。
オープンソースとして提供されることで、研究者や開発者がこの技術をさらに発展させる機会が広がります。


## 参考文献
https://www.linkedin.com/pulse/magentic-one-generalist-multi-agent-system-solving-alamelu-rvmfc
https://medium.com/@has.dhia/magentic-one-the-rise-of-generalist-multi-agent-systems-for-complex-tasks-1b9ee645efe1
https://dataconomy.com/2024/11/07/microsoft-magnetic-one-a-generalist-multi-agent-ai/
https://note.com/ainest/n/n9c9355195e44
https://arxiv.org/abs/2411.04468