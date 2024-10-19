---
title: "v0とGPTでポートフォリオサイトを爆速で作成し、Vercelにデプロイする"
emoji: "🙆"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["v0", "GPT", "Vercel", "生成AI"]
published: true
---

ポートフォリオサイトを作るのって、一見時間がかかりそうだと思いませんか？しかし、今回はGPTの助けを借りて、わずか数十分でポートフォリオサイトを作成し、Vercelにデプロイする方法をご紹介します。この方法は、エンジニアとしての自分を魅力的にアピールするためのサイトを効率的に作りたい人にぴったりです。

# 使用するツール

- **v0**: テキストだけで、UIやゲーム・アプリを作成できるツールです。
- **ChatGPT**: コーディングやコンテンツ作成のアシスタントとして活用します。
- **Vercel**: 作成したポートフォリオを簡単にホスティングし、世界に公開するプラットフォームです。

# ステップ1: ポートフォリオの要素を決定する

まず、ChatGPTを使ってポートフォリオにどのような要素を含めるべきかを確認します。例えば、自己紹介、スキルセット、プロジェクトリスト、連絡先などです。ChatGPTに質問し、必要な要素をリストアップしてもらうことで、全体の構成を考えやすくなります。

```txt:chatgpt
質問：私はエンジニアです。ポートフォリオサイトを作成したいです。どのような内容を入れるべきかを教えてください
ChatGPT：エンジニアのポートフォリオサイトには、以下の内容を含めると効果的です。
### 1. **自己紹介 (About Me)**
 - **プロフィール写真**：信頼感を与えるために、自分らしさを表現した写真を載せましょう。
 - **簡潔な自己紹介**：名前、専門分野、現在の職業や学んでいること、趣味や興味を含めても良いです。
 - **スキルセット**：プログラミング言語、フレームワーク、ツールなど、得意な技術やツールをリスト化します。
### 2. **プロジェクト (Projects)**
 - **実績のあるプロジェクト**：開発したアプリケーション、参加したプロジェクト、オープンソース貢献などを紹介します。
   - **プロジェクト名と概要**：何を作ったか、どんな目的で作ったのか。
   - **使用した技術**：技術スタック（例: React, Node.js, Dockerなど）。
   - **役割と貢献**：自分がどの部分を担当したか、具体的な成果。
   - **リンク**：GitHubやライブデモへのリンクがあると良いで### 3. **スキルセット (Skills)**
 - **プログラミング言語**：得意な言語を並べ、各スキルのレベル（初級、中級、上級）も表示できます。
 - **フレームワーク・ライブラリ**：React、Vue、Django、Railsなど。
 - **ツール・プラットフォーム**：AWS、Docker、CI/CDツール、データベース管理ツールなど。
### 4. **実績 (Achievements)**
 - **認定資格**：AWS認定や各種プログラミング資格。
 - **受賞歴**：ハッカソンやコンテストでの受賞歴があれば。
 - **メディア掲載・寄稿記事**：自分の技術や知識がメディアで紹介された場合や寄稿記事など。
### 5. **ブログ (Blog)**
 - **技術的な知見をシェア**：自分の経験や学びを記事にして公開することで、専門性をアピールできます。
 - **学んだことや課題の解決方法**：問題解決の経験やチュートリアル。
### 6. **お問い合わせ (Contact)**
 - **メールアドレス**や**SNSのリンク**を載せて、仕事の依頼や問い合わせを受け付けられるように。
 - **フォーム**を設置するのも便利です。
### 7. **SNSリンク**
 - GitHub, LinkedIn, Twitterなど、プロフェッショナルな活動をしているSNSへのリンクを追加します。
### 8. **ダウンロード可能な履歴書 (Resume)**
 - 最新の履歴書をPDFでダウンロードできるようにしておくと、雇用者やクライアントにアピールしやすいです。
これらの要素を取り入れることで、あなたのスキルや実績を効果的に伝えられるポートフォリオサイトが作れます。デザインはシンプルで見やすく、ナビゲーションも直感的にすると良いでしょう。
```

# ステップ2: 画面構成を設計する

次に、GPTから得た情報を基にポートフォリオサイトの画面構成を設計します。各要素の配置やページの流れを決め、どのセクションがどこにあると最も効果的かを考えます。これもGPTにお願いします。

```txt:chatgpt
質問：1,2,3,4,7,8で一枚のポートフォリオサイトを作成したいです。この時のサイトのデザイン、画面構成を提案してください
ChatGPT：1ページに情報を集約したポートフォリオサイト（シングルページ）のデザインと画面構成について提案します。全体的にシンプルで見やすく、視覚的に魅力的であることを重視し、スクロールすることで各セクションを順に確認できるようにします。
### **全体的なデザインの方向性**
- **色合い**：メインカラーとアクセントカラーの2〜3色を基調にし、シンプルで清潔感のある配色（例：白、ブルー、グレー）。
- **タイポグラフィ**：見出しは太字で目立たせ、本文はシンプルで読みやすいフォント。
- **レスポンシブ対応**：PCとモバイルの両方で見やすいレイアウト。
### **セクション構成と内容**
1. **ヘッダー (Header)**
 - **ナビゲーションバー**：ページ上部に固定。各セクションへのリンク（「About Me」「Projects」「Skills」「Achievements」「Contact」「Resume」）を設置。右端にSNSアイコンを配置して、外部リンクへ誘導。
 - **ロゴ**：左上に自分の名前やロゴを表示。
2. **ヒーローセクション (Hero Section)**
 - **自己紹介の一部**：シンプルでキャッチーなキャッチコピー（例：「I'm [Your Name], a Software Engineer Specializing in [Your Specialty]」）。
 - **背景画像または動画**：目を引くデザインで、あなたの個性を反映したものを選ぶと良いでしょう。エフェクトの少ない背景で、目立ちすぎないように。
 - **アクションボタン**： "Contact Me" と "View Resume" ボタンを配置して、すぐにアクセスできるように。
3. **自己紹介セクション (About Me)**
 - **プロフィール写真**：丸いアイコンで表示し、自己紹介文の横に配置。
 - **簡潔な自己紹介**：数行の自己紹介文を載せる。自分の強みやスキルセットを簡単に伝える。
 - **SNSアイコン**：GitHub, LinkedIn, Twitterなどのアイコンを並べ、すぐにアクセスできるように。
4. **プロジェクトセクション (Projects)**
 - **カード型レイアウト**：各プロジェクトをカード形式で表示し、プロジェクト名、簡単な説明、使用した技術、リンクボタン（「GitHubを見る」「デモを見る」など）を配置。
 - **マウスオーバー時のエフェクト**：カーソルを合わせた時にカードが少し浮き上がるようなエフェクトを付けると、視覚的にインタラクティブになります。
5. **スキルセットセクション (Skills)**
 - **アイコンとリスト形式**：各スキルをアイコン付きのリストで表示し、プログラミング言語やツールごとにカテゴリ分けします。
 - **スキルバー**：スキルのレベルを視覚的に表現するためのバーや円グラフを追加しても良いでしょう。
6. **実績セクション (Achievements)**
 - **タイムラインまたはバッジ表示**：認定資格や受賞歴をタイムライン形式で表示し、時系列に沿った実績がわかるようにします。または、資格や受賞歴をアイコンやバッジ形式で並べるデザインも考えられます。
 - **簡単な説明**：各実績の簡単な説明を添えると良いです。
7. **お問い合わせセクション (Contact)**
 - **シンプルなフォーム**：名前、メールアドレス、メッセージを入力できるフォームを配置。送信ボタンも目立つように。
 - **メールアドレスとSNSリンク**：フォームの下に直接メールアドレスとSNSアイコンを表示し、複数の方法で連絡できるようにします。
8. **フッター (Footer)**
 - **ダウンロード可能な履歴書 (Resume Download)**：フッターの一部に「Download Resume」ボタンを配置。
 - **ナビゲーションリンクの再掲**：スクロールしなくても簡単に他のセクションにアクセスできるよう、フッターにもナビゲーションリンクを追加。
この構成で、スクロールすることで各セクションが次々と表示されるシンプルなポートフォリオサイトが完成します。特に「自己紹介」と「プロジェクト」セクションは見せ方が重要なので、デザインに力を入れると良いでしょう。
```

# ステップ3: コンテンツを英語に翻訳する
v0では英語の方が精度が高いため、ステップ2で得た提案を修正した後に英語に翻訳します。これはGPTを使っても良いですし、DeepLなどの翻訳サイトを利用しても良いでしょう。サイトの色の構成も指定したいため、[Color Hunt](https://colorhunt.co/)などで使いたい色を選び、その色を反映させるように修正します。私は以下のカラーコードを使用しました。
[#F5F5F5 #48CFCB #229799 #424242](https://colorhunt.co/palette/f5f5f548cfcb229799424242)
![](/images/v0-gpt-portfolio-20241017/colorhunt.png)
最終的に以下のような文章になります。
```
Overall design direction Color scheme: Simple, clean color scheme based on two or three main colors and accent colors(#F5F5F5 #48CFCB #229799 #424242)
Typography: Headlines should be bold and stand out, while body text should be in a simple, easy-to-read font. Responsive: Layout that is easy to view on both PCs and mobile devices. Section Structure and Content Header
Navigation bar: Fixed at the top of the page. Links to each section (“About Me,” “Projects,” “Skills,” “Achievements,” “Contact,” and “Resume”). SNS icons are placed on the far right to direct visitors to external links. Logo: Display your name or logo in the upper left corner. Hero Section
Part of your introduction: A simple, catchy tagline (e.g., “I'm [Your Name], a Software Engineer Specializing in [Your Specialty]”). Background image or video: an eye-catching design that reflects your personality. Use a background with few effects and not too obvious. Action Buttons: Place “Contact Me” and “View Resume” buttons for quick access. Self-introduction section (About Me)
Profile photo: Displayed as a round icon and placed next to the introductory text. Brief self-introduction: A few lines of self-introductory text. Provide a brief description of your strengths and skill set. Social networking icons: Icons for GitHub, LinkedIn, Twitter, etc. for quick access. Projects section
Card-style layout: Display each project as a card, with the project name, a brief description, the technology used, and link buttons (“View GitHub,” “View Demo,” etc.). Mouse-over effects: Visually interactive by adding an effect that makes the card slightly float when hovering the cursor over it. Skill Set section (Skills)
Icon and list format: Display each skill as a list with icons, categorized by programming language and tools. Skills bar: You may want to add a bar or pie chart to visually represent skill levels. Achievements section (Achievements)
Timeline or Badge Display: Display certifications and awards in a timeline format to show achievements in chronological order. Alternatively, the design could be arranged with certifications and awards in icon or badge format. Brief description: A brief description of each accomplishment should accompany the description. Contact section (Contact)
Simple form: Place a form where you can enter your name, email address, and a message. A submit button should also be prominently displayed. Email address and SNS links: Display the email address and SNS icons directly below the form so that people can contact you in multiple ways. Footer
Downloadable Resume (Resume Download): Place a “Download Resume” button as part of the footer. Re-added navigation links: To allow easy access to other sections without scrolling, navigation links are also added to the footer
```

# ステップ4: v0でデザインを作成する
次に、v0（[https://v0.dev](https://v0.dev)）にアクセスして、画面を作成します。
![](/images/v0-gpt-portfolio-20241017/v0-top.png)
ask v0 questionにステップ３で翻訳した文章を入力し、送信します。すると、v0が自動でポートフォリオサイトのデザインを作成してくれます。
![](/images/v0-gpt-portfolio-20241017/v0-second.png)
画面を作成すると以下のようなコードを作成してくれます。
:::details portfolio.tsx
```tsx: portfolio.tsx
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Github, Linkedin, Twitter, Download, ExternalLink } from "lucide-react"
import Image from "next/image"
import Link from "next/link"

export default function Portfolio() {
  return (
    <div className="bg-[#F5F5F5] text-[#424242] min-h-screen">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-white shadow-md z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-[#229799]">
            Your Name
          </Link>
          <nav className="hidden md:flex space-x-4">
            <Link href="#about" className="hover:text-[#48CFCB]">About Me</Link>
            <Link href="#projects" className="hover:text-[#48CFCB]">Projects</Link>
            <Link href="#skills" className="hover:text-[#48CFCB]">Skills</Link>
            <Link href="#achievements" className="hover:text-[#48CFCB]">Achievements</Link>
            <Link href="#contact" className="hover:text-[#48CFCB]">Contact</Link>
            <Link href="#resume" className="hover:text-[#48CFCB]">Resume</Link>
          </nav>
          <div className="flex space-x-2">
            <Link href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">
              <Github className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
            </Link>
            <Link href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">
              <Linkedin className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
            </Link>
            <Link href="https://twitter.com/yourusername" target="_blank" rel="noopener noreferrer">
              <Twitter className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-20 pb-12 md:pt-32 md:pb-24 bg-gradient-to-r from-[#48CFCB] to-[#229799] text-white">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">I'm Your Name</h1>
          <p className="text-xl md:text-2xl mb-8">A Software Engineer Specializing in Your Specialty</p>
          <div className="flex justify-center space-x-4">
            <Button variant="secondary" asChild>
              <Link href="#contact">Contact Me</Link>
            </Button>
            <Button variant="outline" asChild>
              <Link href="#resume">View Resume</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* About Me Section */}
      <section id="about" className="py-12 md:py-24">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center">
            <Image
              src="/placeholder.svg?height=200&width=200"
              alt="Your Name"
              width={200}
              height={200}
              className="rounded-full mb-8 md:mb-0 md:mr-8"
            />
            <div>
              <h2 className="text-3xl font-bold mb-4">About Me</h2>
              <p className="text-lg mb-4">
                Here's a brief introduction about yourself. Highlight your strengths, passion, and what makes you unique as a software engineer.
              </p>
              <div className="flex space-x-4">
                <Link href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">
                  <Github className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
                <Link href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">
                  <Linkedin className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
                <Link href="https://twitter.com/yourusername" target="_blank" rel="noopener noreferrer">
                  <Twitter className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section id="projects" className="py-12 md:py-24 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-8 text-center">Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[1, 2, 3].map((project) => (
              <Card key={project} className="transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
                <CardHeader>
                  <CardTitle>Project {project}</CardTitle>
                  <CardDescription>Brief description of the project</CardDescription>
                </CardHeader>
                <CardContent>
                  <p className="mb-4">Technologies used: React, Node.js, MongoDB</p>
                  <div className="flex space-x-2">
                    <Button variant="outline" size="sm" asChild>
                      <Link href="#" target="_blank" rel="noopener noreferrer">
                        <Github className="mr-2 h-4 w-4" />
                        View GitHub
                      </Link>
                    </Button>
                    <Button variant="outline" size="sm" asChild>
                      <Link href="#" target="_blank" rel="noopener noreferrer">
                        <ExternalLink className="mr-2 h-4 w-4" />
                        View Demo
                      </Link>
                    </Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="py-12 md:py-24">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-8 text-center">Skills</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {['JavaScript', 'React', 'Node.js', 'Python', 'SQL', 'Git', 'AWS', 'Docker'].map((skill) => (
              <div key={skill} className="flex items-center p-4 bg-white rounded-lg shadow">
                <div className="mr-4 text-[#229799]">
                  {/* You can replace this with actual skill icons */}
                  <div className="w-8 h-8 bg-[#48CFCB] rounded-full"></div>
                </div>
                <span>{skill}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Achievements Section */}
      <section id="achievements" className="py-12 md:py-24 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-8 text-center">Achievements</h2>
          <div className="space-y-8">
            {[1, 2, 3].map((achievement) => (
              <Card key={achievement}>
                <CardHeader>
                  <CardTitle>Achievement {achievement}</CardTitle>
                  <CardDescription>Year Achieved</CardDescription>
                </CardHeader>
                <CardContent>
                  <p>Brief description of the achievement or certification.</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-12 md:py-24">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-8 text-center">Contact Me</h2>
          <div className="max-w-md mx-auto">
            <form className="space-y-4">
              <Input type="text" placeholder="Your Name" />
              <Input type="email" placeholder="Your Email" />
              <Textarea placeholder="Your Message" />
              <Button type="submit" className="w-full">Send Message</Button>
            </form>
            <div className="mt-8 text-center">
              <p className="mb-2">Email: your.email@example.com</p>
              <div className="flex justify-center space-x-4">
                <Link href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">
                  <Github className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
                <Link href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">
                  <Linkedin className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
                <Link href="https://twitter.com/yourusername" target="_blank" rel="noopener noreferrer">
                  <Twitter className="h-6 w-6 text-[#229799] hover:text-[#48CFCB]" />
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#229799] text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <nav className="flex flex-wrap justify-center md:justify-start space-x-4 mb-4 md:mb-0">
              <Link href="#about" className="hover:text-[#48CFCB]">About Me</Link>
              <Link href="#projects" className="hover:text-[#48CFCB]">Projects</Link>
              <Link href="#skills" className="hover:text-[#48CFCB]">Skills</Link>
              <Link href="#achievements" className="hover:text-[#48CFCB]">Achievements</Link>
              <Link href="#contact" className="hover:text-[#48CFCB]">Contact</Link>
            </nav>
            <Button variant="secondary" asChild>
              <Link href="/your-resume.pdf" download>
                <Download className="mr-2 h-4 w-4" />
                Download Resume
              </Link>
            </Button>
          </div>
          <div className="mt-8 text-center">
            <p>&copy; {new Date().getFullYear()} Your Name. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
```
:::


# ステップ5: コードをローカルで構築する

v0でデザインが完成したら、そのコードをエクスポートします。v0を使うことで、Tailwind CSSベースのコンポーネントライブラリ（shadcn/ui）を使用して、UIが自動で生成されます。以下の手順でプロジェクトをローカルにセットアップします。

```bash: terminal
❯ npx shadcn@latest add "[https://v0.dev/chat/b/xxxxxx](https://v0.dev/chat/b/xxxxxx)"
✔ The path /Users/masudaharukasuke/github does not contain a package.json file. Would you like to start a new Next.js project? … yes
✔ What is your project named? … my-portfolio
✔ Creating a new Next.js project.
✔ Which style would you like to use? › New York
✔ Which color would you like to use as the base color? › Neutral
✔ Would you like to use CSS variables for theming? … no / yes
✔ Writing components.json.
✔ Checking registry.
✔ Installing dependencies.
✔ Created 5 files:
- components/portfolio.tsx
- components/ui/button.tsx
- components/ui/card.tsx
- components/ui/input.tsx
- components/ui/textarea.tsx
npm notice
npm notice New minor version of npm available! 10.8.2 -> 10.9.0
npm notice Changelog: [https://github.com/npm/cli/releases/tag/v10.9.0](https://github.com/npm/cli/releases/tag/v10.9.0)
npm notice To update run: npm install -g npm@10.9.0
npm notice

```

作成したレポジトリに移動し正しく動くかを確認してください。

```bash: terminal
cd my-portfolio
npm run dev
```
[http://localhost:3000](http://localhost:3000)にアクセスするとv0で作成したデザイン通りのページが出力してくれます
![](/images/v0-gpt-portfolio-20241017/localhost.png)

また、Vercelにデプロイする際にはnpm run buildを実行します。ビルドが正しく完了するかを確認してください。

```bash: terminal
npm run build
```

:::details 私は以下のようなエラーが発生しました。
エラー内容
```bash: terminal
Failed to compile.

./components/portfolio.tsx
45:64  Error: `'` can be escaped with `&apos;`, `&lsquo;`, `&#39;`, `&rsquo;`.  react/no-unescaped-entities
72:21  Error: `'` can be escaped with `&apos;`, `&lsquo;`, `&#39;`, `&rsquo;`.  react/no-unescaped-entities

./components/ui/input.tsx
5:18  Error: An interface declaring no members is equivalent to its supertype.  @typescript-eslint/no-empty-object-type

./components/ui/textarea.tsx
5:18  Error: An interface declaring no members is equivalent to its supertype.  @typescript-eslint/no-empty-object-type
```
ダッシュがエスケープされていないためエラーが発生しているようです。以下のように修正します。
```diff tsx: portfolio.tsx
- I'm
+ I&apos;m

- Here's
+ Here&apos;s
```
また`interface`のエラーは以下のように修正します。
```diff tsx: input.tsx
- export interface InputProps
-   extends React.InputHTMLAttributes<HTMLInputElement> {}
+ export type InputProps = React.InputHTMLAttributes<HTMLInputElement>
```
```diff tsx: textarea.tsx
- export interface TextareaProps
-   extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}
+ export type TextareaProps = React.TextareaHTMLAttributes<HTMLTextAreaElement>
```
:::

# ステップ6: GitHubにプッシュする
プロジェクトがローカルで問題なく動作することを確認したら、GitHubリポジトリを作成してコードをアップロードします。これにより、バージョン管理ができ、Vercelへのデプロイがスムーズになります。
![](/images/v0-gpt-portfolio-20241017/github.png)
# ステップ7: Vercelにデプロイする
最後に、Vercelを使ってポートフォリオサイトをデプロイします。Vercelにサインインし、GitHubリポジトリを選択するだけで簡単にデプロイできます。
![](/images/v0-gpt-portfolio-20241017/vercel-0.png)
![](/images/v0-gpt-portfolio-20241017/vercel-1.png)
デプロイが完了すると以下のような画面になります。
![](/images/v0-gpt-portfolio-20241017/vercel-2.png)
デプロイが完了したら、提供されたURLにアクセスして、ポートフォリオサイトが正常に表示されるか確認してください。
[https://portfolio-mock-masuda1246s-projects.vercel.app/](https://portfolio-mock-masuda1246s-projects.vercel.app/)


# おわりに
この方法を使用すると、短時間でポートフォリオサイトを作成し、デプロイできます。v0のUI作成ととChatGPTのコンテンツ生成機能を活用することで、効率的に高品質なサイトが構築可能です。Vercelを使用すれば、ホスティングも簡単です。
コンテンツの修正やデザインの変更が必要な場合も、Next.jsとshadcn/uiを利用することで、開発者にとって使いやすい構造になっています。これらの技術を活用して、自分のポートフォリオを素早く公開してみましょう。