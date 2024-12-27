---
title: "Terraformでのaws_default_route_tableとaws_route_tableの違いと選び方"
emoji: "🗂"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["aws", "terraform", "network", "vpc", "iac"]
published: true
---

## TL;DR
- `aws_default_route_table`: デフォルトで作成されるルートテーブルを管理するためのリソース。既存の環境を軽微に調整したい場合に有用。
- `aws_route_table`: 任意のカスタムルートテーブルを新規作成して管理するリソース。柔軟性や拡張性が必要な場合に推奨。


# 背景
AWSのVPC（Virtual Private Cloud）では、サブネット間の通信や外部へのルートを管理するためにルートテーブルを使用します。Terraformには、このルートテーブルを管理するためのリソースとして`aws_default_route_table`と`aws_route_table`の2種類があります。一見似ているように見えますが、それぞれの用途や使用方法が異なります。


# `aws_default_route_table`の特徴

## 概要
- VPC作成時にAWSが自動生成するデフォルトのルートテーブルを管理します。
- デフォルトルートテーブルの設定を変更することが可能ですが、新しいルートテーブルの作成はできません。

## 主な用途
- VPC作成時のデフォルトルートテーブルをそのまま利用しつつ、軽微な変更を加える場合。
- タグ付けや特定のルート（例: インターネットゲートウェイへのルート）を追加したい場合。

## 例
```hcl
resource "aws_default_route_table" "default" {
  default_route_table_id = aws_vpc.main.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "default-route-table"
  }
}
```
この設定では、デフォルトルートテーブルにインターネットへのルートを追加しています。


# `aws_route_table`の特徴

## 概要
- 任意の数のカスタムルートテーブルを新規作成可能。
- サブネットやリソースごとに異なるルートテーブルを作成して管理できます。

## 主な用途
- VPC内で特定のサブネットやネットワーク構成に対応するカスタムルートテーブルを作成したい場合。
- セキュリティやトラフィック管理の要件が複雑で、柔軟なルート設定が必要な場合。

## 例
```hcl
resource "aws_route_table" "custom" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "custom-route-table"
  }
}
```
この設定では、新しいカスタムルートテーブルを作成し、特定のルートを設定しています。


# 比較表

| 項目                   | `aws_default_route_table`                              | `aws_route_table`                                    |
|----------------------------|----------------------------------------------------------|-------------------------------------------------------|
| 対象                   | デフォルトで作成されるルートテーブル                    | 任意で作成するカスタムルートテーブル                  |
| 作成の可否             | 新規作成不可（デフォルトルートテーブルを変更のみ可能） | 新規作成可能                                          |
| 主な用途               | デフォルトルートテーブルの軽微な調整                     | サブネットやリソースごとに異なるルート設定             |
| 柔軟性                 | 限定的                                                  | 高い柔軟性                                             |
| 推奨シナリオ           | 小規模プロジェクト、既存環境の調整                     | 中〜大規模プロジェクト、複雑なネットワーク要件         |

---

# どちらを使うべきか？
1. 基本的には`aws_route_table`を推奨
   - 新規プロジェクトや将来的な拡張を考慮する場合。
   - VPC内で複数のサブネットに異なるルートテーブルを設定したい場合。
   - ネットワーク管理をより明示的に行いたい場合。

2. `aws_default_route_table`を使う場合
   - 既存のデフォルト設定をそのまま活用し、軽微な変更を加えたい場合。
   - プロジェクト規模が小さく、単一のルートテーブルで十分な場合。

# まとめ
- 柔軟性や拡張性を重視するなら`aws_route_table`。
- 簡易な変更や既存環境の活用を目的とするなら`aws_default_route_table`。
