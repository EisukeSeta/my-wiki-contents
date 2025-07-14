# my-wiki-contents
markdown files from pukiwiki

---

## mkdocsによるHTML変換・GitHub Pages公開手順

### 必要なもの
- Python（3.6以上推奨）
- pip

### セットアップ手順

1. mkdocsのインストール
   ```sh
   pip install mkdocs
   ```
2. プロジェクト初期化（初回のみ）
   ```sh
   mkdocs new .
   ```
3. マークダウンファイルをdocsフォルダに移動
   ```sh
   move *.md docs/
   ```
4. サイトのビルド（HTML生成）
   ```sh
   mkdocs build
   ```
   - 生成されたHTMLは`site/`フォルダに出力されます。

### GitHub Pagesで公開する場合

1. GitHubリポジトリのSettings → Pagesで、
   - Branch: `main`
   - Folder: `/ (root)`または`/docs`（`site/`は選択不可なので注意）
   - もしくは、`gh-deploy`コマンドで自動デプロイも可能

2. `mkdocs gh-deploy`コマンドでGitHub Pagesにデプロイ
   ```sh
   mkdocs gh-deploy
   ```
   - 初回はGitHubの認証が必要な場合があります。

---

### 参考
- [MkDocs公式ドキュメント（日本語訳）](https://mkdocs-ja.readthedocs.io/ja/latest/)
- [GitHub Pages公式](https://pages.github.com/)
