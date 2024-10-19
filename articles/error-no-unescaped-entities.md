---
title: "Next.js のビルドエラー「react/no-unescaped-entities」の原因と解決方法"
emoji: "🗂"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["error", "react", "nextjs"]
published: true
---

# エラーの詳細

Next.js プロジェクトをビルドする際に、次のようなエラーが発生することがあります:

```
Failed to compile.

./components/portfolio.tsx
45:64  Error: `'` can be escaped with `&apos;`, `&lsquo;`, `&#39;`, `&rsquo;`.  react/no-unescaped-entities
```

このエラーは、JSX内で使用された文字 `'`（アポストロフィ）やその他の特定の文字が、エスケープ処理されていないことを示しています。この場合、`I'm` というテキストが問題となり、ビルドエラーを引き起こしています。

# エラーの原因

JSX内で使用される文字には、HTMLエンティティとしてエスケープするべき文字が存在します。これにより、特定の文字が正しく解釈されない問題や、XSS（クロスサイトスクリプティング）のリスクを軽減します。`'`（アポストロフィ）は、エスケープが推奨される文字の一つであり、ReactのESLintルールである `react/no-unescaped-entities` により検出されます。

# 解決方法

このエラーを解決するためには、以下の方法があります。

## 1. HTMLエンティティを使用する

問題の箇所に対して、エスケープ済みのHTMLエンティティを使用します。例えば、`I'm` の代わりに `I&apos;m` を使用するように変更します。

```jsx
<p>I&apos;m a developer.</p>
```

## 2. ESLintルールの無効化

プロジェクトの規模やポリシーに応じて、このルールを無効にすることもできます。しかし、推奨される解決策ではありません。ESLintルールを無効化する場合は、以下のように一時的にコメントを追加することで特定の行のみ無効化できます。

```jsx
{/* eslint-disable-next-line react/no-unescaped-entities */}
<p>I'm a developer.</p>
```

# まとめ

このエラーは、JSX内で直接特殊文字を使用した際に発生することが一般的です。安全で保守性の高いコードを維持するために、エスケープ済みのHTMLエンティティを使用することが推奨されます。