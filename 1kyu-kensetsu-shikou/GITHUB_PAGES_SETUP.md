# GitHub Pages セットアップガイド

## 📋 現在の状況

✅ **GitHubリポジトリへのプッシュ完了**
- リポジトリURL: https://github.com/bmwz376-cmd/1-1-
- ブランチ: `main`
- 問題集ディレクトリ: `/1kyu-kensetsu-shikou`

---

## 🚀 GitHub Pagesを有効化する手順

### ステップ1: GitHubリポジトリページへアクセス

https://github.com/bmwz376-cmd/1-1-

### ステップ2: Settings を開く

1. リポジトリページ上部の `⚙️ Settings` タブをクリック

### ステップ3: Pages 設定を開く

1. 左サイドバーの `Pages` をクリック（Code and automation セクション内）

### ステップ4: Source を設定

**Build and deployment** セクションで以下を設定:

1. **Source**: `Deploy from a branch` を選択
2. **Branch**: 
   - ブランチ: `main` を選択
   - フォルダ: `/ (root)` を選択
3. `Save` ボタンをクリック

### ステップ5: デプロイ完了を待つ

- 数分待つと、自動的にデプロイが開始されます
- ページ上部に緑色のメッセージが表示されます:
  ```
  Your site is live at https://bmwz376-cmd.github.io/1-1-/
  ```

---

## 🌐 公開URL

### メインページ:
```
https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/
```

または

```
https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/index.html
```

### 個別ファイルアクセス:

- **JSON データ**: https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/all_250_questions.json
- **テキスト教材**: https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/textbook_all_250.txt
- **README**: https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/README.md

---

## ✅ 確認方法

1. GitHubリポジトリページの `Actions` タブをチェック
   - 緑色のチェックマーク ✅ が表示されればデプロイ成功
2. 公開URLにアクセスして問題集が表示されるか確認

---

## 🔧 トラブルシューティング

### 404 エラーが表示される場合

**原因**: フォルダパスが正しく設定されていない

**解決方法**:
1. Settings → Pages で **フォルダ** を `/ (root)` に設定
2. または、以下のURLでアクセス:
   ```
   https://bmwz376-cmd.github.io/1-1-/1kyu-kensetsu-shikou/
   ```

### デプロイが完了しない場合

**確認事項**:
1. `Actions` タブでワークフロー実行状況を確認
2. エラーメッセージがあれば内容を確認
3. `main` ブランチに最新コードがプッシュされているか確認

---

## 📱 アクセス方法

デプロイ完了後、以下の方法でアクセスできます:

### パソコン・スマホ・タブレット
- ブラウザで上記URLを開く
- スマホ対応済み（レスポンシブデザイン）

### PDF として保存
1. ブラウザで問題集ページを開く
2. `Ctrl + P` (Windows) または `Cmd + P` (Mac) で印刷画面を開く
3. 「送信先」を「PDFに保存」に変更
4. 保存実行

---

## 🎓 完成した成果物

✅ **全250問の完全オリジナル問題集**
- 第1年次〜第5年次（各50問）
- 法規・施工・施工管理・共通の4分野
- 詳細な解説・図解付き
- ルビ（ふりがな）付き
- Web表示対応（HTML）
- テキスト形式対応
- JSON データ対応
- PDF印刷対応

✅ **ドキュメント完備**
- README.md（使い方ガイド）
- LICENSE_AND_DISCLAIMER.md（免責事項）
- PDF_DESIGN.md（PDF設計書）
- DEPLOYMENT.md（デプロイガイド）
- SUMMARY.md（成果物サマリー）

---

## 🎉 次のステップ

1. **GitHub Pagesを有効化**（上記手順に従う）
2. **公開URLにアクセス**して動作確認
3. **URLを共有**して利用開始

**お疲れさまでした！** 🎊
