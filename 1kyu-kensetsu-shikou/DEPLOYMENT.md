# デプロイメントガイド

## 1級建築施工管理技士 完全オリジナル問題集 - 公開方法

---

## 🌐 公開方法（3つの選択肢）

### 方法1: GitHub Pages（推奨・無料）

#### ステップ1: GitHubリポジトリを作成
```bash
# GitHubで新しいリポジトリを作成
# 例: https://github.com/YOUR_USERNAME/1kyu-kensetsu-shikou
```

#### ステップ2: コードをプッシュ
```bash
cd /home/user/webapp/1kyu-kensetsu-shikou

# Gitリポジトリ初期化（既存の場合は不要）
git init

# ファイルを追加
git add .

# コミット
git commit -m "Initial commit: 1級建築施工管理技士問題集"

# リモート追加
git remote add origin https://github.com/YOUR_USERNAME/1kyu-kensetsu-shikou.git

# プッシュ
git branch -M main
git push -u origin main
```

#### ステップ3: GitHub Pagesを有効化
1. GitHubリポジトリページへアクセス
2. 「Settings」→「Pages」をクリック
3. Source: `main` ブランチを選択
4. ディレクトリ: `/ (root)` を選択
5. 「Save」をクリック

#### ステップ4: 公開URLを確認
数分後、以下のようなURLで公開されます：
```
https://YOUR_USERNAME.github.io/1kyu-kensetsu-shikou/
```

---

### 方法2: Cloudflare Pages（高速・無料）

#### 必要なもの
- Cloudflare アカウント（無料）
- Cloudflare API トークン

#### ステップ1: Cloudflare ダッシュボード
1. [Cloudflare](https://dash.cloudflare.com/)にログイン
2. 「Pages」→「Create a project」

#### ステップ2: GitHubと連携
1. 「Connect to Git」を選択
2. GitHubリポジトリを選択
3. ビルド設定:
   - **Framework preset**: None
   - **Build command**: (空欄)
   - **Build output directory**: `/`

#### ステップ3: デプロイ
「Save and Deploy」をクリック

#### 公開URL
```
https://1kyu-kensetsu-shikou.pages.dev
```

または、カスタムドメインも設定可能

---

### 方法3: Netlify（簡単・無料）

#### ドラッグ&ドロップでデプロイ

1. [Netlify](https://www.netlify.com/)にアクセス
2. 「Sites」→「Add new site」→「Deploy manually」
3. 以下のフォルダをドラッグ&ドロップ:
   ```
   /home/user/webapp/1kyu-kensetsu-shikou/
   ```

#### 公開URL（自動生成）
```
https://random-name-12345.netlify.app
```

カスタムドメイン名に変更可能

---

## 📁 デプロイに必要なファイル

以下のファイルが公開されます：

### 必須ファイル
- ✅ `index.html` - メインページ
- ✅ `all_250_questions.json` - 問題データ
- ✅ `README.md` - 使用方法
- ✅ `LICENSE_AND_DISCLAIMER.md` - 免責事項

### オプションファイル
- `textbook_all_250.txt` - テキスト版
- `PDF_DESIGN.md` - PDF設計書
- `SUMMARY.md` - サマリー
- その他のJSONファイル

---

## 🚀 クイックデプロイ（コマンドライン）

### GitHub Pagesへ自動デプロイ
```bash
#!/bin/bash
# deploy_github.sh

cd /home/user/webapp/1kyu-kensetsu-shikou

# 初期化
git init
git add .
git commit -m "Deploy: 1級建築施工管理技士問題集"

# リモート設定（YOUR_USERNAMEを実際のユーザー名に変更）
git remote add origin https://github.com/YOUR_USERNAME/1kyu-kensetsu-shikou.git

# プッシュ
git branch -M main
git push -u origin main

echo "✅ GitHubにプッシュ完了"
echo "次のステップ: GitHub Settingsでpagesを有効化してください"
```

### Netlify CLI
```bash
# Netlify CLIをインストール
npm install -g netlify-cli

# ログイン
netlify login

# デプロイ
cd /home/user/webapp/1kyu-kensetsu-shikou
netlify deploy --prod

# 公開URLが表示されます
```

---

## 🔧 GitHub Actions（自動デプロイ）

### .github/workflows/deploy.yml
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./1kyu-kensetsu-shikou
```

このファイルを作成すると、`main`ブランチへのプッシュで自動的にデプロイされます。

---

## 📊 各サービスの比較

| サービス | 料金 | 速度 | 簡単さ | カスタムドメイン |
|---------|------|------|--------|----------------|
| GitHub Pages | 無料 | 普通 | ★★★☆☆ | ✅ |
| Cloudflare Pages | 無料 | 高速 | ★★★★☆ | ✅ |
| Netlify | 無料 | 高速 | ★★★★★ | ✅ |
| Vercel | 無料 | 高速 | ★★★★☆ | ✅ |

**推奨**: 初心者は **Netlify**、技術者は **Cloudflare Pages**

---

## ⚠️ デプロイ前のチェックリスト

- [ ] `index.html`が正しく動作する
- [ ] `all_250_questions.json`が存在する
- [ ] 免責事項ファイルが含まれている
- [ ] README.mdが最新
- [ ] プライベート情報が含まれていない
- [ ] ライセンス情報が明記されている

---

## 🔒 セキュリティ注意事項

### 公開して良いファイル
✅ index.html  
✅ all_250_questions.json  
✅ README.md  
✅ LICENSE_AND_DISCLAIMER.md  
✅ textbook_all_250.txt  

### 公開しない方が良いファイル（任意）
⚠️ generate_*.py（生成スクリプト）  
⚠️ node_modules/（依存関係）  
⚠️ .git/（Gitディレクトリ）  

### .gitignoreの例
```
node_modules/
.DS_Store
*.pyc
__pycache__/
.env
```

---

## 📱 モバイル対応確認

デプロイ後、以下をテストしてください：
- [ ] スマートフォンで表示できる
- [ ] タブレットで表示できる
- [ ] 印刷プレビューが正しい
- [ ] JSONが正しく読み込まれる

---

## 🌍 カスタムドメインの設定（オプション）

### GitHub Pagesの場合
1. ドメインを購入（例: `1kyu-kentiku.com`）
2. DNS設定で以下のCNAMEレコードを追加:
   ```
   www.1kyu-kentiku.com → YOUR_USERNAME.github.io
   ```
3. GitHubリポジトリの「Settings」→「Pages」でカスタムドメインを設定

### Cloudflare Pagesの場合
1. Cloudflare Pagesダッシュボードを開く
2. 「Custom domains」→「Set up a custom domain」
3. ドメイン名を入力して指示に従う

---

## 📈 アクセス解析（オプション）

### Google Analyticsの追加
`index.html`の`<head>`内に追加：
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🆘 トラブルシューティング

### 問題: ページが表示されない
✓ `index.html`がルートディレクトリにあるか確認  
✓ GitHubの場合、Pagesが有効化されているか確認  
✓ 数分待ってから再度アクセス

### 問題: JSONが読み込めない
✓ ブラウザのコンソールでエラーを確認  
✓ `all_250_questions.json`が同じディレクトリにあるか確認  
✓ ファイル名が正確か確認（大文字小文字区別）

### 問題: 404エラー
✓ URLが正しいか確認  
✓ デプロイが完了しているか確認  
✓ ブラウザのキャッシュをクリア

---

## 📞 サポート

- GitHub Pages: https://docs.github.com/pages
- Cloudflare Pages: https://developers.cloudflare.com/pages
- Netlify: https://docs.netlify.com

---

**これで全世界に公開できます！** 🌏

作成日: 2025年12月31日
