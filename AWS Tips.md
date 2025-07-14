[[FrontPage]]

*AWS費用 [#u7464e4e]
-参考リンク
--[[ざっくりAWS (EC2):https://aws-rough.cc/ec2/]]
---[[ざっくりAWS Fargateの料金を日本円で計算:https://aws-rough.cc/fargate/]]

*EC2の設定 [#d82e481c]

-参考リンク
--[[【AWS】VPCを設定して自分だけのネットワーク環境を構築してみよう:https://kacfg.com/vpc/]]
--[[【AWS】EC2でAmazon Linux 2を構築しSSH接続してみよう:https://kacfg.com/ec2-amazon-linux/]]

**Node.js のセットアップ [#a540fdf9]
-Linux インスタンスで Node.js を設定するには
+SSH を使用して、Linux インスタンスに ec2-user として接続します。
+コマンドラインで次のように入力して、ノードバージョンマネージャー (nvm) をインストールします。
 curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm では Node.js の複数のバージョンをインストールすることができ、またそれらの切り替えもできるため、nvm を使用して Node.js をインストールします。
+コマンドラインで次のように入力し、nvm をロードします。
 source ~/.bashrc
+コマンドラインで次のように入力し、nvm を使用して Node.js の最新の LTS バージョンをインストールします。
 nvm install --lts
+コマンドラインで次のように入力して、Node.js が正しくインストールされ、実行されていることをテストします。
 node -e "console.log('Running Node.js ' + process.version)"
 Running Node.js VERSION

-参考リンク
--[[Github nvm:https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating]]
--[[チュートリアル: Amazon EC2 インスタンスでの Node.js のセットアップ:https://docs.aws.amazon.com/ja_jp/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html]]

**AWS CDK CLI のインストール [#cc1b8a9a]
-Node Package Managerを使用してCKD CLIをインストール （-g オプションでグローバルにインストール）
 $ npm install -g aws-cdk
-CDK CLI の正常なインストールの確認
 $ cdk --version
-AWS CLIが設定したローカル環境のアクセスキーを取得する
 $ cat ~/.aws/credentials 
 [default]
 aws_access_key_id = XXXXXXXXXXXX
 aws_secret_access_key = XXXXXXXXXXXX

-参考リンク
--[[AWS CDK の開始方法:https://docs.aws.amazon.com/ja_jp/cdk/v2/guide/getting_started.html]]
--[[ローカル環境でIAMロール権限を取得する:https://qiita.com/harumaki-web/items/f7ec46cb5f6b7b5a9cc3]]

* Fargateの設定 [#wd7db513]

-参考リンク
--[[[初心者向け]言われるままにFargate初めて触ったので、忘れないための記録:https://dev.classmethod.jp/articles/fargate-my-first-step/]]

**AWS Copilot CLI [#zaaf5db4]
-[[Homebrew:https://brew.sh/ja/]]のインストール
 $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
--/home/linuxbrew/　以下にインストールされる。インストール途中の指示に従う。
 ==> Next steps:
 - Run these commands in your terminal to add Homebrew to your PATH:
     echo >> /home/seta/.bashrc
     echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/seta/.bashrc
     eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
 - Install Homebrew's dependencies if you have sudo access:
     sudo apt-get install build-essential
   For more information, see:
     https://docs.brew.sh/Homebrew-on-Linux
 - We recommend that you install GCC:
     brew install gcc
 - Run brew help to get started
 - Further documentation:
     https://docs.brew.sh
-AWS CopilotをHomebrewでインストール
 $ brew install aws/tap/copilot-cli
--インストールされたバージョンの確認
 $ copilot --version
 copilot version: v1.34.0
--ヘルプの表示
 $ copilot --help
-アプリケーションの作成、コマンドを実行したディレクトリに存在する Dockerfile を自動的に検出してくれる
 $ copilot app init copilot-demo-app --resource-tags
もしくは簡単に copilot initで、インタラクティブに情報を指定する
 $ copilot init
今回指定した情報は以下
 Application name: copilot-pukiwiki
 Which workload type best represents your architecture?: Load Balanced Web Service   (Public. ALB by default. Internet to ECS on Fargate)
 What do you want to name this service?: cop-pukiwiki
 Which Dockerfile would you like to use for cop-pukiwiki?: Use an existing image instead
 What's the location ([registry/]repository[:tag|@digest]) of the image to use?: pengo/pukiwiki
 Which port do you want customer traffic sent to?: 80 （デフォルト）
 Would you like to deploy an environment? [? for help] (y/N) : y
 What is your environment's name?: copilot-pukiwiki-env
-アプリケーションの一覧
 $ copilot app ls
-アプリケーションに含まれるサービスや環境の一覧を表示
 $ copilot app show
-アプリケーションの削除（deleteコマンドで環境一式まるまる削除が可能）
 $ copilot app ls
 copilot-pukiwiki
 $ copilot app delete copilot-pukiwiki

-参考リンク
--[[ECSのオペレーションを劇的に簡略化するAWS Copilotが発表されました！:https://dev.classmethod.jp/articles/aws-copilot/]]
--[[AWS Copilot CLI のインストール:https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-install.html]]
--[[AWS Copilot 入門:https://qiita.com/yoshii0110/items/8a74cc0fc540ae3f2389]]
--[[AWS Copilotで検証環境を構築した話:https://qiita.com/ttanaka-gxp/items/238017f2ea61492ac154]]
--[[AWS Copilot CLIを試してみた:https://qiita.com/zumax/items/bc89fb76db531742499b]]
--[[AWS Copilot CLIのススメ:https://zenn.dev/praha/articles/f42467cd6a9e79]]
