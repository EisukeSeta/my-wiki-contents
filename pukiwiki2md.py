import re
import glob
import os

# 整形対象のMarkdownファイル一覧（README.md, index.mdは除外）
targets = glob.glob('docs/*.md')
targets = [f for f in targets if not os.path.basename(f) in ['README.md', 'index.md']]

def convert_pukiwiki_to_md(text):
    # 見出し変換（*** → ###, ** → ##, * → #）
    text = re.sub(r'^\*\*\*([^\n]*)', r'###\1', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*([^\n]*)', r'##\1', text, flags=re.MULTILINE)
    text = re.sub(r'^\*([^\n]*)', r'#\1', text, flags=re.MULTILINE)
    # 箇条書き（---, --, - をネストに変換）
    text = re.sub(r'^---\s+', r'    - ', text, flags=re.MULTILINE)
    text = re.sub(r'^--\s+', r'  - ', text, flags=re.MULTILINE)
    text = re.sub(r'^-\s+', r'- ', text, flags=re.MULTILINE)
    # 番号付きリスト（+ → 1.）
    text = re.sub(r'^\+\s+', r'1. ', text, flags=re.MULTILINE)
    # pukiwiki独自タグ削除（#br, [#xxxxxx] など）
    text = re.sub(r'#br', '', text)
    text = re.sub(r'\[#[a-zA-Z0-9]+\]', '', text)
    # テーブルの |h や |~ を削除
    text = re.sub(r'\|h', '|', text)
    text = re.sub(r'\|~', '|', text)
    # [[リンク:URL]] → [リンク](URL)
    text = re.sub(r'\[\[([^\]:]+):([^\]]+)\]\]', r'[\1](\2)', text)
    # 余分な空行を整理
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

for file in targets:
    with open(file, encoding='utf-8') as f:
        src = f.read()
    converted = convert_pukiwiki_to_md(src)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(converted)
print('pukiwiki形式→Markdown形式への一括変換が完了しました。')
