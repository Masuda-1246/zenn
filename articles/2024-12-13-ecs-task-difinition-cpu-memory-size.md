---
title: "TerraformでECSタスク定義のCPUとメモリを最適化する方法：開発環境から本番環境まで"
emoji: "👌"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["aws", "ecs", "terraform", "container"]
published: true
---
### はじめに
AWS ECS（Elastic Container Service）でコンテナアプリケーションを運用する際、タスク定義で設定するCPUとメモリの値を適切に設定することは、パフォーマンスとコストのバランスを取る上で非常に重要です。特に、開発 (dev)、ステージング (stg)、本番 (prd) といった異なる環境で、それぞれ適切なリソース量を設定する必要があります。

この記事では、Terraformを使用してECSタスク定義のCPUとメモリを最適化するためのステップと、具体的な設定例を解説します。

### TL;DR

- **アプリケーションの要件を理解する**：バックエンドとフロントエンドで、必要なCPUとメモリ量は大きく異なります。
- **環境ごとにリソース量を調整する**：開発環境は最小限、ステージング環境は本番環境に近い設定、本番環境は余裕を持った設定が推奨されます。
- **単位を正しく理解する**：CPUはvCPU、メモリはMiB（メビバイト）で指定します。
- **過剰なリソースはコスト増、不足はパフォーマンス低下につながる**：適切なリソース量を設定することが重要です。
- **CloudWatchメトリクスを監視して継続的に最適化する**：実際の使用状況を把握し、必要に応じてリソース量を調整します。

### 1. アプリケーションの要件を把握する

まず、バックエンドAPIとフロントエンドで、それぞれどれくらいのCPUとメモリが必要なのかを把握する必要があります。

- **バックエンドAPI**：
    - リクエスト処理量（1秒あたりのリクエスト数）
    - データベース接続数
    - 計算処理の複雑さ
    - 使用するプログラミング言語やフレームワークの特性
- **フロントエンド**：
    - 表示するコンテンツの量
    - JavaScriptの実行量
    - APIリクエストの頻度
    - ユーザー数

これらの要素を考慮し、アプリケーションがどれくらいのリソースを消費するかを把握しましょう。

### 2. 環境ごとのリソース量の変化を考慮する

- **開発 (dev) 環境**：
    - 最小限の構成で十分な場合が多いです。
    - 開発中のテストやデバッグが主な目的です。
    - コストを抑えることが重要です。
- **ステージング (stg) 環境**：
    - 本番環境に近い構成にする必要があります。
    - パフォーマンスや安定性を検証するために、本番と同程度の負荷をかけます。
- **本番 (prd) 環境**：
    - 実際のユーザーからのリクエストに対応できる十分なリソースが必要です。
    - スケーラビリティや可用性を考慮して、余裕を持った構成にする必要があります。

### 3. CPUとメモリの単位について

- **CPU**：1 vCPUは、Amazon EC2インスタンスの1つの仮想CPUコアを表します。Fargateでは、CPUはvCPUの単位で指定します。
- **メモリ**：メモリはMiB（メビバイト）単位で指定します。1024MiBは1GiB（ギビバイト）に相当します。

### 4. 推奨される設定例

以下は、一般的な設定例です。実際のアプリケーションに合わせて調整が必要です。

| 環境 | アプリケーション | CPU  | メモリ (MiB) |
| --- | ----------- | -------- | -------- |
| dev | バックエンドAPI  | 256    | 512    |
| dev | フロントエンド  | 256    | 512    |
| stg | バックエンドAPI  | 512    | 1024   |
| stg | フロントエンド  | 512    | 1024   |
| prd | バックエンドAPI  | 1024  | 2048   |
| prd | フロントエンド  | 1024  | 2048   |

### 5. Terraformコードの設定例

```terraform
resource "aws_ecs_task_definition" "backend_api_dev" {
  family                   = "your-app-dev-backend-api"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  # ... その他の設定 ...
}

resource "aws_ecs_task_definition" "backend_api_stg" {
  family                   = "your-app-stg-backend-api"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"
  # ... その他の設定 ...
}

resource "aws_ecs_task_definition" "backend_api_prd" {
  family                   = "your-app-prd-backend-api"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024"
  memory                   = "2048"
  # ... その他の設定 ...
}

resource "aws_ecs_task_definition" "frontend_dev" {
  family                   = "your-app-dev-frontend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  # ... その他の設定 ...
}

resource "aws_ecs_task_definition" "frontend_stg" {
  family                   = "your-app-stg-frontend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"
  # ... その他の設定 ...
}

resource "aws_ecs_task_definition" "frontend_prd" {
  family                   = "your-app-prd-frontend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024"
  memory                   = "2048"
  # ... その他の設定 ...
}
```

### 6. 設定のポイント

- **過剰なリソースはコスト増につながる**：必要なリソースよりも大幅に多い値を設定すると、無駄なコストが発生します。
- **不足したリソースはパフォーマンス低下につながる**：リソースが不足すると、アプリケーションの応答が遅くなったり、エラーが発生したりする可能性があります。
- **スケーリング設定を検討する**：ECSのオートスケーリングを活用することで、負荷に応じてリソースを自動的に調整できます。
- **CloudWatchメトリクスを監視する**：CPU使用率やメモリ使用率を監視し、必要に応じて設定を調整します。

### 7. 継続的な監視と最適化

設定は一度決めたら終わりではありません。

- CloudWatchのメトリクスを監視し、CPU使用率やメモリ使用率が常に高い場合は、リソースを増やすことを検討します。
- 逆に、リソースが常に余っている場合は、リソースを減らすことでコストを削減できます。

### まとめ

TerraformでECSタスク定義のCPUとメモリを設定する際には、アプリケーションの要件と環境ごとの特性を考慮し、適切な値を設定することが重要です。設定後も、CloudWatchメトリクスを監視し、継続的に最適化を行うことで、パフォーマンスとコストのバランスを保つことができます。

ご不明な点がありましたら、お気軽にご質問ください。
