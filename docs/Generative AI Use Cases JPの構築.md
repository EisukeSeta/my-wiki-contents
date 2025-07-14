[[FrontPage]]

#Generative AI Use Cases JPの構築 
##環境準備 
-手元の環境で必要なもの（WSL2で準備済み）
 AWSアカウント
 AWS CLI
 AWS CDK
 npm
-リポジトリ準備
 git clone https://github.com/aws-samples/generative-ai-use-cases-jp.git
 cd generative-ai-use-cases-jp
-デプロイするリージョンを環境変数で指定（バージニア北部 us-east-1）
 export AWS_REGION=us-east-1
 --> export AWS_REGION=us-west-2
-リポジトリのルートで実行
 npm ci
-（初回のみ、CDKを使ったことがない場合）Bootstrap を行う
 npx -w packages/cdk cdk bootstrap
-最後にデプロイを実行（20～30分かかる）
 npm run cdk:deploy
-CloudFormation Stacks を確認、GenerativeAiUseCasesStackが追加されているはず
-CloudFormationでGenerativeAiUseCasesStackのOutputsタブを開き、WebUrl のリンクを開く。
-アカウントを作成し、利用する

-参考リンク
--[Github generative-ai-use-cases-jp](https://github.com/aws-samples/generative-ai-use-cases-jp)
---[ネイティブアプリのように利用する方法](https://github.com/aws-samples/generative-ai-use-cases-jp/blob/main/docs/PWA.md)
--[Generative AI Use Cases JP をデプロイしてチャットを触ってみた](https://qiita.com/wasashi/items/76642d6a864ee7dafd29)
--[AWSのGenUを試してみました。自社専用の生成AI利用システムが手軽に作れる！](https://biz.addisteria.com/aws_genu/)

##インストールがうまくいかない場合 
-nvmのインストールと更新
 $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
 $ sourece ~/.bashrc
-nvmのインストールを確認
 $ command -v nvm
-Nodeの最新バージョンをインストール
 $ nvm install node
-AWS CLI設定方法
--AWS CLIを初回利用するときのConfigure設定方法（CLIを実行するためのIAMアクセスキーを事前準備しておく）
 $ aws configure
--入力項目。準備したIAMのアクセスキーとシークレットキーを入力する
 AWS Access Key ID [****************xxxx]:
 AWS Secret Access Key [****************xxxx]:
 Default region name [None]: ap-northeast-1
 Default output format [None]: json

-参考リンク
--[Github nvm](https://github.com/nvm-sh/nvm)
--[Node.jsのバージョンをアップグレードする方法](https://qiita.com/takokke/items/df01818d65a0d4b1da90)
--[Node と NPM を最新バージョンに更新する方法](https://www.freecodecamp.org/japanese/news/how-to-update-node-and-npm-to-the-latest-version/)
--[AWS CLIを使用するためのconfigure設定方法](https://qiita.com/Kiyonchu/items/9b2f60e912a295c9261c)

##セキュリティ強化 
-セルフサインアップを無効化する
--context の selfSignUpEnabled に false を指定します。(デフォルトは true)
--packages/cdk/cdk.json を編集
 {
   "context": {
     "selfSignUpEnabled": false,
   }
 }
--設定変更後に以下を実行して変更内容を反映させる
 $ npm run cdk:deploy 

-参考リンク
--[Github generative-ai-use-cases-jp](https://github.com/aws-samples/generative-ai-use-cases-jp)

##モデル追加 
-modelIdsを変更
--packages/cdk/cdk.json を編集
    "modelRegion": "us-west-2",
    "modelIds": [
      "anthropic.claude-3-5-haiku-20241022-v1:0",
      "anthropic.claude-3-5-sonnet-20241022-v2:0",
      "anthropic.claude-3-5-sonnet-20240620-v1:0",
      "anthropic.claude-3-sonnet-20240229-v1:0"
    ],
    "imageGenerationModelIds": [
      "amazon.titan-image-generator-v2:0",
      "amazon.titan-image-generator-v1",
      "stability.stable-diffusion-xl-v1",
      "stability.sd3-large-v1:0",
      "stability.stable-image-core-v1:0",
      "stability.stable-image-ultra-v1:0"
    ],

-参考リンク
--[バージニア北部で利用可能なモデル](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/modelaccess)

##ブラウザ拡張機能 
-準備
--AWS CDKの出力をテキストファイルにメモ（コピー）しておく
 (前略)
 GenerativeAiUseCasesStack.ApiEndpoint = https://xxxx.execute-api.{region}.amazonaws.com/api/
 (中略)
 GenerativeAiUseCasesStack.IdPoolId = {region}:xxx-xxx-xxx-xxx-xxx
 (中略)
 GenerativeAiUseCasesStack.PredictStreamFunctionArn = arn:aws:lambda:{region}:{account}:function:GenerativeAiUseCasesStack-APIPredictStreamxxx-xxx
 (中略)
 GenerativeAiUseCasesStack.Region = {region}
 (中略)
 GenerativeAiUseCasesStack.UserPoolClientId =xxx
 GenerativeAiUseCasesStack.UserPoolId = {region}_xxxx
 (後略)
--generative-ai-use-cases-jp/browser-extension/src/.env を開き、メモしておいた内容を転記する
 VITE_APP_REGION=Region の値
 VITE_APP_USER_POOL_ID=IdPoolId の値
 VITE_APP_USER_POOL_CLIENT_ID=UserPoolClientId の値
 VITE_APP_IDENTITY_POOL_ID=IdPoolId の値
 VITE_APP_PREDICT_STREAM_FUNCTION_ARN=PredictStreamFunctionArn の値
 VITE_APP_API_ENDPOINT=ApiEndpoint の値
--環境情報を転記した後、generative-ai-use-cases-jp/ ディレクトリで以下のコマンドを実行
 $ npm run extension:ci
 $ npm run extension:build
--generative-ai-use-cases-jp/browser-extension/ に dist/ というディレクトリが出来上がる。これが拡張機能のパッケージ本体となる。
-ブラウザ拡張機能のインストール
--Chrome に拡張機能をインストールする方法
---メニューから「設定」をクリックし
---次に左のペインから「拡張機能」をクリック
---最後に左上に表示される「パッケージ化されていない拡張機能を読み込む」をクリック
---先程の npm run extension:build コマンドで生成した dist ディレクトリを選択（インストール完了）

-参考リンク
--[Github generative-ai-use-cases-jp ブラウザ拡張機能](https://github.com/aws-samples/generative-ai-use-cases-jp/blob/main/browser-extension/README.md)
--[無茶振りは生成 AI に断ってもらおう~ ブラウザに生成 AI を組み込んでみた ~](https://aws.amazon.com/jp/builders-flash/202405/genai-sorry-message/)

##ネイティブアプリのように利用する 
--デプロイした Web の URL にアクセスするとアドレスバー右のインストールボタンが表示されるので、クリックしてインストールする。 

-参考リンク
--[ネイティブアプリのように利用する方法](https://github.com/aws-samples/generative-ai-use-cases-jp/blob/main/docs/PWA.md)

##アップデート方法 
-main ブランチを pull する。
すでにリポジトリを clone 済みで、初回デプロイが完了していることを想定
 $ git pull
-再デプロイする。
Bootstrap は必要なし、パッケージがアップデートされている可能性があるため、npm ci コマンドは実行
 npm ci
 npm run cdk:deploy

-参考リンク
--[アップデート方法(Github)](https://github.com/aws-samples/generative-ai-use-cases-jp/blob/main/docs/UPDATE.md)

##GenU環境のクリーンアップ（削除） 
-GenU のリソースを削除、10分程かかる
 $ npm run cdk:destroy
--必要あれば、GenUに関連するS3バケットを空にし、削除する
--CDKのBootstrapで作成されたCloudFormation Stackも、不要であれば削除する
-GenUの解体は、以下でも可能。オプション設定を追加していると複数のスタックが作られるため、削除するスタックを指定する必要があるが、ここでアスタリスク"*"指定することですべてのスタックを削除することができる。
 $ npm run cdk:destroy "*"

-参考リンク
--[Generative AI Use Cases JP をデプロイしてチャットを触ってみた](https://qiita.com/wasashi/items/76642d6a864ee7dafd29)
--[GenUを構築してみた(後編)](https://zenn.dev/oka_yama/articles/5b574ef27f3718)
