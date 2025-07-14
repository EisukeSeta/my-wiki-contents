[[FrontPage]]

*Docker運用手順 [#c66b4221]
**Dockerインストール手順（Windows11 WSL2） [#j93ec79f]
-Ubuntu 20.04 をアップデートする [#yb3e066a]
 $ sudo apt update[[FrontPage]]

*Docker運用手順 [#c66b4221]
**Dockerインストール手順（Windows11 WSL2） [#j93ec79f]
-Ubuntu 20.04 をアップデートする [#yb3e066a]
 $ sudo apt update
 $ sudo apt upgrade -y
-必要なパッケージをインストールする [#b9b9370f]
 $ sudo apt install curl -y
 $ sudo apt install apt-transport-https -y
-Docker 公式 GPG 鍵を追加 [#u7191837]
 $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
-Docker 安定版のレポジトリを追加 [#od049fd4]
 $ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
-レポジトリをアップデートし、Docker Engine をインストール [#k4888439]
 $ sudo apt update
 $ sudo apt install docker-ce docker-ce-cli containerd.io -y
-docker-compose もインストール [#w9c99bb0]
 $ sudo apt install docker-compose -y
-Docker デーモンを起動 [#l21d39ee]
 $ sudo service docker start
-Docker の容量の削減
 $ docker system df                # Docker の使用容量や割合の表示
 $ docker ps -a                    # コンテナの表示
 $ docker images                   # イメージの表示
 $ docker image prune              # 使っていないイメージの削除
 $ docker system prune             # すべてを全削除
 $ docker builder prune            # ビルドキャッシュの全削除
 $ docker rm $(docker ps -aq)      # コンテナの全削除
 $ docker rmi $(docker images -q)  # イメージの全削除
 $ docker rmi <Image ID>           # 各イメージの削除

-参考リンク [#sa868bfd]
--[[windowsにWSL2+Docker環境を構築する手順:https://qiita.com/taka777n/items/ea3a1b3a2802aabf3db2]]
--[[【2024年最新版】初心者のためのpukiwikiのインストール方法と使い方:https://wisenetwork.net/archives/2642]]
--[[Windows / WSL2 の容量を減らす方法:https://zenn.dev/anko/articles/976d904e53d87e]]

**Dockerインストール手順（AWS EC2） [#k37f966d]
-EC2内のパッケージを最新にしておく
 $ sudo yum update -y
-Docker Engineパッケージのインストール
 $ sudo yum install -y docker
-Dockerサービスの起動
 $ sudo systemctl start docker
-Dockerサービスが起動していることを確認。[active (running)]と表示されていれば正常に起動している
 $ systemctl status docker
 ● docker.service - Docker Application Container Engine
    Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
    Active: active (running) since Sat 2022-06-11 23:45:40 UTC; 5s ago
-Dockerサービスの自動起動を有効化
 $ sudo systemctl enable docker
 Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
-Dockerサービスの自動起動が有効であることを確認。[enabled]と表示されていればOK
 $ systemctl is-enabled docker
 enabled
-ec2-userにdockerグループを追加（Dockerをインストールすると、OSにdockerグループが自動作成される）、これでec2-userはsudoなしでdockerコマンドを実行できるようになる
 $ grep docker /etc/group
 docker:x:992:
 $ sudo usermod -a -G docker ec2-user
-Docker Composeのインストール

-参考リンク
--[[【AWS】EC2にDockerとDocker Composeをインストール:https://kacfg.com/aws-ec2-docker/]]
--[[パソコン起動時にWSLのdocker composeを自動起動させる:https://zenn.dev/quantum/articles/b1de629aca3cf0]]

**DOCKERコンテナ [#p53eed3a]
-実行中のコンテナ名を確認
 $ docker ps
-コンテナにログイン
 $ docker exec -it {コンテナ名} sh
-あるいは、docker-compose.ymlを作成
 services:
   pukiwiki:
     image: pengo/pukiwiki
     restart: unless-stopped
     ports:
       - 8080:80
     volumes:
      - $HOME/DOCKER/pukiwiki:/ext
--pukiwiki起動
 $ docker compose up -d
--pukiwiki停止
 $ docker compose down -v

-参考リンク
--[[pukiwiki用Dockerコンテナ:https://hub.docker.com/r/pengo/pukiwiki]]
--[[Pukiwiki 用 Dockerコンテナを触ってみたメモ:https://qiita.com/smats-rd/items/3bdd70ce2de4e65cf0f0]]
--[[PukiWikiのインストール:https://saturday-in-the-park.netlify.app/AlpineLinux/12_PikiWiki/]]
--[[【Docker Compose】今更聞けない、docker-compose.ymlの書き方や仕組み:https://qiita.com/shimada_slj/items/3580b0426fa6b73e4638]]
--[[Docker-compose基礎:https://qiita.com/ryome/items/35df47a01a7fe3ac70ee]]

**pukiwikiをDockerコンテナでインストール [#b003e734]
-インストール手順
--vオプションを省略すればマウントしない
 mkdir $HOME/pukiwiki
 docker run -p 8080:80 -v $HOME/pukiwiki:/ext -d pengo/pukiwiki
 open http://localhost:8080

-データの転送方法
サーバー側の$HOME/pukiwikiに設定ファイル等ができており、以下のフォルダ部分を移設すれば利用できる。
 wiki/ : データ本体
 attach/ : 添付ファイル
 cache/ : 最近の更新
 diff/ : 更新履歴

-pukiwikiのアンインストール方法
--展開したフォルダごと削除すればアンインストール完了

**pukiwiki設定 [#g8055808]
-pukiwiki.ini.phpを編集し、管理者パスワードを設定する（"!"の部分にmd5で暗号化し記入）
 $adminpass = '{x-php-md5}!';
-バックアップの出力（管理者パスワードが必要）
 http://localhost:8080/?cmd=dump

-参考リンク
--[[Web Collaboration by PukiWik-pukiwikiで凍結した記事の内容が消える件について:https://www.kisnet.or.jp/~kanou/?Web+Collaboration+by+PukiWik-pukiwiki%E3%81%A7%E5%87%8D%E7%B5%90%E3%81%97%E3%81%9F%E8%A8%98%E4%BA%8B%E3%81%AE%E5%86%85%E5%AE%B9%E3%81%8C%E6%B6%88%E3%81%88%E3%82%8B%E4%BB%B6%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6]]
--[[md5変換ツール:https://dev.digitra.net/tools/md5encode.php]]
--[[pukiwiki新規設置時の改修点メモ（2020年版）:https://qiita.com/saitohsan/items/84960a23b2a9c3e35a27]]
--[[PukiWiki/Install/パーミッション設定:https://pukiwiki.sourceforge.io/?PukiWiki/Install/%E3%83%91%E3%83%BC%E3%83%9F%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%AD%E5%AE%9A]]
--[[PukiWikiの管理パスワードとユーザー認証設定の更新:https://tetsuyai.hatenablog.com/entry/20080727]]
--[[データをバックアップ、リストアする:https://wiki.dobon.net/index.php?PukiWiki%2FTips%2F%A5%C7%A1%BC%A5%BF%A4%F2%A5%D0%A5%C3%A5%AF%A5%A2%A5%C3%A5%D7%A1%A2%A5%EA%A5%B9%A5%C8%A5%A2%A4%B9%A4%EB]]

**Difyインストール [#k558cee0]
-Dify導入
 $ git clone https://github.com/langgenius/dify.git
-Dify起動
 $ cp .env.example .env
 $ docker compose up -d
-http://localhost/install にアクセス。

--ollama導入（テスト、AMD ROCm導入で失敗）
---AMD GPU用
 $ docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
---コンテナーに入る
 $ docker exec -it ollama bash
---Llama3 8Bのダウンロード
 ollama run llama3
---Ollamaを終了させる -> 起動したOllamaは「/bye」と入力すると終了できる
---コンテナーを抜ける
 exit
---ollama削除
 $ docker rm ollama

--AWS Bedrock接続
---AWS CLIが設定したローカル環境のアクセスキーを取得する
 $ cat ~/.aws/credentials 
 [default]
 aws_access_key_id = XXXXXXXXXXXX
 aws_secret_access_key = XXXXXXXXXXXX
--Dify設定画面に入力（モデルIDは anthropic.claude-3-5-haiku-20241022-v1:0 など）

-参考リンク
--[[プロキシ環境下のローカルPCに "Dify" を導入して、Bedrockする:https://qiita.com/yuki_ink/items/1367e0b2bb09c95c0570#4-dify-%E5%B0%8E%E5%85%A5]]
--[[Dify（ディファイ）on WSL2でgpt-4oを実験:https://qiita.com/potofo/items/62136d2e4a5ea2f65c25]]
--[[ノーコードLLM統合アプリのdifyでollamaと連携してみた:https://qiita.com/Tadataka_Takahashi/items/ba832511bd4fd5cd46f1]]
--[[【Dify】【Ollama】【WSL2】Difyをローカル環境で実行するまでの全手順:https://touch-sp.hatenablog.com/entry/2024/05/12/110240]]
^^[[ollama用Dockerコンテナ:https://hub.docker.com/r/ollama/ollama]]
--[[ローカル環境でIAMロール権限を取得する:https://qiita.com/harumaki-web/items/f7ec46cb5f6b7b5a9cc3]]
--[[Dify導入 個人メモ:https://zenn.dev/metalmental/articles/20241003_dify]]

*関連ツール [#b8b464eb]
**AIターミナル「warp」 [#t0055c6c]
-WSLにインストール
 $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
 $ sudo apt -y install ./google-chrome-stable_current_amd64.deb
-~/.bash_profileに追加
 export WARP_ENABLE_WAYLAND=1
 export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
 export BROWSER=google-chrome
-warp起動
 $ warp-terminal

-参考リンク
--[[The intelligent terminal. Warp:https://www.warp.dev/]]
--[[WSLのワープターミナルは素晴らしいです:https://dev.to/karleeov/warp-terminal-on-wsl-is-amazing-5bj4]]
--[[知らないなんてもったいない！次世代ターミナル「Warp」:https://qiita.com/shun_sakamoto/items/a0c79083c97064a361f2]]
--[[ターミナル「Warp」の便利機能とショートカットキー:https://zenn.dev/collabostyle/articles/00706975b8a29e]]

**AMDドライバ更新（WSL対応は[[AMD Software: Adrenalin Edition™ 24.12.1 for WSL2:https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html]]） [#ke1f945f]
-[[ROCmを使用したWSL用のRadeonソフトウェアのインストール:https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html]]
 $ sudo apt update
 $ wget https://repo.radeon.com/amdgpu-install/6.1.3/ubuntu/jammy/amdgpu-install_6.1.60103-1_all.deb
 $ sudo apt install ./amdgpu-install_6.1.60103-1_all.deb
-使用可能なユースケースのリストを表示
 $ sudo amdgpu-install --list-usecase
-WSL のユース ケース # AMDでは、デフォルトでWSLユースケースをインストールすることをお勧めします。次のコマンドを実行して、オープンソースのグラフィックスとROCmをインストールします。
 $ amdgpu-install -y --usecase=wsl,rocm --no-dkms
-インストール後の確認チェック
 $ rocminfo
失敗している模様。
 hsa api call failure at: ./sources/wsl/tools/rocminfo/rocminfo.cc:1087
 Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
-ROCmのアンインストール。次のコマンドを実行して、ROCmソフトウェアスタックおよびその他のLinux用Radeonソフトウェアコンポーネントをアンインストール。
 $ sudo amdgpu-uninstall

-参考リンク
--[[Release notes amdgpu-install:https://repo.radeon.com/amdgpu-install/6.1.3/ubuntu/jammy/]]
--[[AMD Software: Adrenalin Edition 24.12.1 Release Notes:https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html]]
--[[ROCmを使用したWSL用のRadeonソフトウェアのインストール::https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html]]
--[[Windows11でAMD ROCmソフトウェアを実行する方法:https://capeta55.xsrv.jp/how-to-run-amd-rocm-on-windows11/]]

 $ sudo apt upgrade -y
-必要なパッケージをインストールする [#b9b9370f]
 $ sudo apt install curl -y
 $ sudo apt install apt-transport-https -y
-Docker 公式 GPG 鍵を追加 [#u7191837]
 $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
-Docker 安定版のレポジトリを追加 [#od049fd4]
 $ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
-レポジトリをアップデートし、Docker Engine をインストール [#k4888439]
 $ sudo apt update
 $ sudo apt install docker-ce docker-ce-cli containerd.io -y
-docker-compose もインストール [#w9c99bb0]
 $ sudo apt install docker-compose -y
-Docker デーモンを起動 [#l21d39ee]
 $ sudo service docker start
-Docker の容量の削減
 $ docker system df                # Docker の使用容量や割合の表示
 $ docker ps -a                    # コンテナの表示
 $ docker images                   # イメージの表示
 $ docker image prune              # 使っていないイメージの削除
 $ docker system prune             # すべてを全削除
 $ docker builder prune            # ビルドキャッシュの全削除
 $ docker rm $(docker ps -aq)      # コンテナの全削除
 $ docker rmi $(docker images -q)  # イメージの全削除
 $ docker rmi <Image ID>           # 各イメージの削除

-参考リンク [#sa868bfd]
--[[windowsにWSL2+Docker環境を構築する手順:https://qiita.com/taka777n/items/ea3a1b3a2802aabf3db2]]
--[[【2024年最新版】初心者のためのpukiwikiのインストール方法と使い方:https://wisenetwork.net/archives/2642]]
--[[Windows / WSL2 の容量を減らす方法:https://zenn.dev/anko/articles/976d904e53d87e]]

**Dockerインストール手順（AWS EC2） [#k37f966d]
-EC2内のパッケージを最新にしておく
 $ sudo yum update -y
-Docker Engineパッケージのインストール
 $ sudo yum install -y docker
-Dockerサービスの起動
 $ sudo systemctl start docker
-Dockerサービスが起動していることを確認。[active (running)]と表示されていれば正常に起動している
 $ systemctl status docker
 ● docker.service - Docker Application Container Engine
    Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
    Active: active (running) since Sat 2022-06-11 23:45:40 UTC; 5s ago
-Dockerサービスの自動起動を有効化
 $ sudo systemctl enable docker
 Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
-Dockerサービスの自動起動が有効であることを確認。[enabled]と表示されていればOK
 $ systemctl is-enabled docker
 enabled
-ec2-userにdockerグループを追加（Dockerをインストールすると、OSにdockerグループが自動作成される）、これでec2-userはsudoなしでdockerコマンドを実行できるようになる
 $ grep docker /etc/group
 docker:x:992:
 $ sudo usermod -a -G docker ec2-user
-Docker Composeのインストール

-参考リンク
--[[【AWS】EC2にDockerとDocker Composeをインストール:https://kacfg.com/aws-ec2-docker/]]
--[[パソコン起動時にWSLのdocker composeを自動起動させる:https://zenn.dev/quantum/articles/b1de629aca3cf0]]

**DOCKERコンテナ [#p53eed3a]
-実行中のコンテナ名を確認
 $ docker ps
-コンテナにログイン
 $ docker exec -it {コンテナ名} sh
-あるいは、docker-compose.ymlを作成
 services:
   pukiwiki:
     image: pengo/pukiwiki
     restart: unless-stopped
     ports:
       - 8080:80
     volumes:
      - $HOME/DOCKER/pukiwiki:/ext
--pukiwiki起動
 $ docker compose up -d
--pukiwiki停止
 $ docker compose down -v

-参考リンク
--[[pukiwiki用Dockerコンテナ:https://hub.docker.com/r/pengo/pukiwiki]]
--[[Pukiwiki 用 Dockerコンテナを触ってみたメモ:https://qiita.com/smats-rd/items/3bdd70ce2de4e65cf0f0]]
--[[PukiWikiのインストール:https://saturday-in-the-park.netlify.app/AlpineLinux/12_PikiWiki/]]
--[[【Docker Compose】今更聞けない、docker-compose.ymlの書き方や仕組み:https://qiita.com/shimada_slj/items/3580b0426fa6b73e4638]]
--[[Docker-compose基礎:https://qiita.com/ryome/items/35df47a01a7fe3ac70ee]]

**pukiwikiをDockerコンテナでインストール [#b003e734]
-インストール手順
--vオプションを省略すればマウントしない
 mkdir $HOME/pukiwiki
 docker run -p 8080:80 -v $HOME/pukiwiki:/ext -d pengo/pukiwiki
 open http://localhost:8080

-データの転送方法
サーバー側の$HOME/pukiwikiに設定ファイル等ができており、以下のフォルダ部分を移設すれば利用できる。
 wiki/ : データ本体
 attach/ : 添付ファイル
 cache/ : 最近の更新
 diff/ : 更新履歴

-pukiwikiのアンインストール方法
--展開したフォルダごと削除すればアンインストール完了

**pukiwiki設定 [#g8055808]
-pukiwiki.ini.phpを編集し、管理者パスワードを設定する（"!"の部分にmd5で暗号化し記入）
 $adminpass = '{x-php-md5}!';
-バックアップの出力（管理者パスワードが必要）
 http://localhost:8080/?cmd=dump

-参考リンク
--[[Web Collaboration by PukiWik-pukiwikiで凍結した記事の内容が消える件について:https://www.kisnet.or.jp/~kanou/?Web+Collaboration+by+PukiWik-pukiwiki%E3%81%A7%E5%87%8D%E7%B5%90%E3%81%97%E3%81%9F%E8%A8%98%E4%BA%8B%E3%81%AE%E5%86%85%E5%AE%B9%E3%81%8C%E6%B6%88%E3%81%88%E3%82%8B%E4%BB%B6%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6]]
--[[md5変換ツール:https://dev.digitra.net/tools/md5encode.php]]
--[[pukiwiki新規設置時の改修点メモ（2020年版）:https://qiita.com/saitohsan/items/84960a23b2a9c3e35a27]]
--[[PukiWiki/Install/パーミッション設定:https://pukiwiki.sourceforge.io/?PukiWiki/Install/%E3%83%91%E3%83%BC%E3%83%9F%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%AD%E5%AE%9A]]
--[[PukiWikiの管理パスワードとユーザー認証設定の更新:https://tetsuyai.hatenablog.com/entry/20080727]]
--[[データをバックアップ、リストアする:https://wiki.dobon.net/index.php?PukiWiki%2FTips%2F%A5%C7%A1%BC%A5%BF%A4%F2%A5%D0%A5%C3%A5%AF%A5%A2%A5%C3%A5%D7%A1%A2%A5%EA%A5%B9%A5%C8%A5%A2%A4%B9%A4%EB]]

**Difyインストール [#k558cee0]
-Dify導入
 $ git clone https://github.com/langgenius/dify.git
-Dify起動
 $ cp .env.example .env
 $ docker compose up -d
-http://localhost/install にアクセス。

--ollama導入（テスト、AMD ROCm導入で失敗）
---AMD GPU用
 $ docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
---コンテナーに入る
 $ docker exec -it ollama bash
---Llama3 8Bのダウンロード
 ollama run llama3
---Ollamaを終了させる -> 起動したOllamaは「/bye」と入力すると終了できる
---コンテナーを抜ける
 exit
---ollama削除
 $ docker rm ollama

--AWS Bedrock接続
---AWS CLIが設定したローカル環境のアクセスキーを取得する
 $ cat ~/.aws/credentials 
 [default]
 aws_access_key_id = XXXXXXXXXXXX
 aws_secret_access_key = XXXXXXXXXXXX
--Dify設定画面に入力（モデルIDは anthropic.claude-3-5-haiku-20241022-v1:0 など）

-参考リンク
--[[プロキシ環境下のローカルPCに "Dify" を導入して、Bedrockする:https://qiita.com/yuki_ink/items/1367e0b2bb09c95c0570#4-dify-%E5%B0%8E%E5%85%A5]]
--[[Dify（ディファイ）on WSL2でgpt-4oを実験:https://qiita.com/potofo/items/62136d2e4a5ea2f65c25]]
--[[ノーコードLLM統合アプリのdifyでollamaと連携してみた:https://qiita.com/Tadataka_Takahashi/items/ba832511bd4fd5cd46f1]]
--[[【Dify】【Ollama】【WSL2】Difyをローカル環境で実行するまでの全手順:https://touch-sp.hatenablog.com/entry/2024/05/12/110240]]
^^[[ollama用Dockerコンテナ:https://hub.docker.com/r/ollama/ollama]]
--[[ローカル環境でIAMロール権限を取得する:https://qiita.com/harumaki-web/items/f7ec46cb5f6b7b5a9cc3]]
--[[Dify導入 個人メモ:https://zenn.dev/metalmental/articles/20241003_dify]]

*関連ツール [#b8b464eb]
**AIターミナル「warp」 [#t0055c6c]
-WSLにインストール
 $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
 $ sudo apt -y install ./google-chrome-stable_current_amd64.deb
-~/.bash_profileに追加
 export WARP_ENABLE_WAYLAND=1
 export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
 export BROWSER=google-chrome
-warp起動
 $ warp-terminal

-参考リンク
--[[The intelligent terminal. Warp:https://www.warp.dev/]]
--[[WSLのワープターミナルは素晴らしいです:https://dev.to/karleeov/warp-terminal-on-wsl-is-amazing-5bj4]]

**AMDドライバ更新（WSL対応は[[AMD Software: Adrenalin Edition™ 24.12.1 for WSL2:https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html]]） [#ke1f945f]
-[[ROCmを使用したWSL用のRadeonソフトウェアのインストール:https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html]]
 $ sudo apt update
 $ wget https://repo.radeon.com/amdgpu-install/6.1.3/ubuntu/jammy/amdgpu-install_6.1.60103-1_all.deb
 $ sudo apt install ./amdgpu-install_6.1.60103-1_all.deb
-使用可能なユースケースのリストを表示
 $ sudo amdgpu-install --list-usecase
-WSL のユース ケース # AMDでは、デフォルトでWSLユースケースをインストールすることをお勧めします。次のコマンドを実行して、オープンソースのグラフィックスとROCmをインストールします。
 $ amdgpu-install -y --usecase=wsl,rocm --no-dkms
-インストール後の確認チェック
 $ rocminfo
失敗している模様。
 hsa api call failure at: ./sources/wsl/tools/rocminfo/rocminfo.cc:1087
 Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
-ROCmのアンインストール。次のコマンドを実行して、ROCmソフトウェアスタックおよびその他のLinux用Radeonソフトウェアコンポーネントをアンインストール。
 $ sudo amdgpu-uninstall

-参考リンク
--[[Release notes amdgpu-install:https://repo.radeon.com/amdgpu-install/6.1.3/ubuntu/jammy/]]
--[[AMD Software: Adrenalin Edition 24.12.1 Release Notes:https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html]]
--[[ROCmを使用したWSL用のRadeonソフトウェアのインストール::https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html]]
--[[Windows11でAMD ROCmソフトウェアを実行する方法:https://capeta55.xsrv.jp/how-to-run-amd-rocm-on-windows11/]]
