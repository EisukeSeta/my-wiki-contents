[[FrontPage]]

#contents

#システム関係 
##キーボードレイアウト 
-[Windows 108日本語キーボード を Mac で使えるようにキーを設定する方法](https://sundaygamer.net/windows-keyboard-on-mac/)
##ファイルサイズ圧縮 
-[Windows10 フォルダ圧縮 GUIツール CompactGUI](https://github.com/ImminentFate/CompactGUI/)
+普通にCompactGUI.exeをダウンロードする
+起動したらSelectとかなんとか書かれてるのをクリック
+ダイアログが出るので、圧縮したいフォルダを選択
+ここでちょっと待たされて反応無くなるけど待つ
+しばらくしたら圧縮形式を選択するダイアログが出るので
+XPRESS16Kを選択してCompress Folderボタンをクリック
--[指定したフォルダを、普通に使える状態のまま圧縮できるようにする！「CompactGUI」](https://www.gigafree.net/utility/CompactGUI.html)
--圧縮したフォルダを元に戻す
 圧縮完了後、通常では「Uncompress」というボタンが表示されるようですが、私の環境では表示されなかったので、一応コマンドラインで圧縮の解除を行う方法を紹介しておきます。コマンドプロンプトに慣れている人は、コマンドプロンプトを開いて
    compact /U /EXE /S:圧縮解除を行うフォルダのパス 
 と入力 → 「Enter」キーを押せば OK です。
    compact /U /EXE /S:D:\download\GIMPPortable 
 のような感じです。

-[Optimizer Textures (Ordenador)](http://skyrim.2game.info/detail.php?id=12801):テクスチャを最適化して僅かな画質劣化と引き換えにパフォーマンスを向上させます。指定フォルダ以下にある最適化可能なテクスチャを自動判定して圧縮します。

##操作方法 
-[スカイリム（Skyrim）PC版の操作方法一覧](http://best-skyrim-navi.blogspot.jp/2012/01/skyrimpc.html)
-[スカイリムのCTD対策](http://skyrimshot.blog.fc2.com/blog-entry-27.html)

##インストーラ 
-[NMM (Nexusmods skyrim)](http://www.nexusmods.com/skyrim/mods/modmanager/?)
--[SkyrimのMODの導入方法 はじめてMODを入れる人向けに書きました｜NMMの使い方](http://nerdhayayo.blog.fc2.com/blog-entry-7.html)
---[Nexus mods](http://www.nexusmods.com/skyrim/mods/modmanager/?)

##バグフィックス 
-[Unofficial Skyrim Legendary Edition Patch](http://www.nexusmods.com/skyrim/mods/71214/?)
--[USLEEP - Japanese Voice Edit](http://skyrim.2game.info/detail.php?id=85456):USLEEP - Japanese Voice EditはUnofficial Skyrim Legendary Edition Patch用の日本語音声ファイルです。

-[Crash fixes](http://skyrim.2game.info/detail.php?id=72725):各種クラッシュ事項に対処することを試み、対処する助けとなるplugin。
--[SKSE Plugin Preloader](http://skyrim.2game.info/detail.php?id=75795):Skyrimのプログラム処理が始まる前に、SKSE pluginをロードすることができるようにするもの現在のところ Crash fixes v10のINIファイルでUseOSAllocators=1を指定する場合にのみ必要。
 メモリ・アロケーション・パッチ機能を使用する方法
 1. CrashFixPlugin.ini を開き、"UseOSAllocators=0"と記述されている箇所を見つける
 2. "UseOSAllocators=1"と変更する
 3. SKSE Plugin Preloaderをダウンロードし、インストールする
 4. ゲームを開始する。メモリ・パッチが適用できなかった旨のエラーが表示されたら、内容を読んで下さい。状況把握に役立ちます。
 (5.)ENBを使用していてゲームがクラッシュしたなら、enblocal.iniでExpandSystemMemoryX64=falseに設定して下さい。
 (6.) ゲームのクラッシュが増えるようだったら(特にUNP RaceMenu sliderに関連している？)、CrashFixPlugin.iniでAlignHeapAllocate=1に設定してみる。

-[Safety Load](http://skyrim.2game.info/detail.php?id=46465):無限ロード防止SKSEプラグイン。ロード画面で止まってしまうバグを修正します。
DATA/SKSE/Plugins/SafetyLoad.iniを作成。
 EnableOnlyLoading = true

-[Continue Game No Crash](http://skyrim.2game.info/detail.php?id=78557):初回ロードCTD防止のための有名な方法である、セーフゾーンでのセーブデータをまずロード、目的のセーブデータをロードというプロセスを自動で行って、初回ロードCTDを防止してくれま
す。
--[Load Game CTD Fix](http://skyrim.2game.info/detail.php?id=85443):ロード時に一時的にシングルコア状態にCPUの機能を制限することで同時読み込みに起因するCTDを回避する。Continue Game No Crashの後継。

-[Hdt Invisibility Fix beta](http://skyrim.2game.info/detail.php?id=77815):透明人間になってしまうバグが発生したNPCを自動で元に戻すMOD。

-[Prisoner cart fix](http://skyrim.2game.info/detail.php?id=65538):MODを入れた環境でニューゲーム開始直後に馬車が荒ぶるバグのFIXです。多少荒ぶることはありますが、とりあえず進行します。

-[Universal Race Scale Remover](http://skyrim.2game.info/detail.php?id=80763):NPCが家具を使う際に縮尺を1.0に戻すキーワー「RaceToScale」を削除します。子供が家具を使うと巨大化してた人にお勧め。

-[Modern Brawl Bug Fix](http://skyrim.2game.info/detail.php?id=77465):殴り合いは、参加者に魔法の効果がかかると中断される。当MODは、該当する戦闘状況中断のトリガーを、殴り合いのあいだに武器(素手は除く)で攻撃する、攻撃的な呪文およびシャウトおよび巻物を使った時、あるいはプレイヤーが呪文をとなえた時、錬金素材を使ったりポーションを使ったりした時のみに変更する。

###[SKSEによる修正](http://skyrim-mod.blog.jp/archives/1005619907.html) 
SKSE.iniに追加します。メモリーパッチ機能を有効にします(計768MB、2ブロック目が256MB)。またゴミスクリプトがセーブデータを破損させたり、ファイルサイズが延々と肥大化することを防ぐ機能をオンにします。
 [Memory]
 DefaultHeapInitialAllocMB=768
 ScrapHeapSizeMB=256
 
 [General] 
 ClearInvalidRegistrations=1 

##関連ツール 
-[MOD Organizer](http://skyrim.2game.info/detail.php?id=1334):MOD総合管理ツール。略称「MO」。最大の特徴は「仮想」Dataフォルダ機能。
-[TES5Edit](http://skyrim.2game.info/detail.php?id=25859):MOD編集・クリーニングツール。
-[BodySlide and Outfit Studio](http://skyrim.2game.info/detail.php?id=49015):従来のBodySlideの機能に加え、服や鎧などのメッシュの編集を手軽に行えるツールOutfitStudioの２種類が同梱されています。
-[Nifscope](http://niftools.sourceforge.net/wiki/NifSkope)
--[MOD制作ツール NifSkopeの導入](http://barom777.blog.fc2.com/blog-entry-22.html)
--[NifskopeのNiAlphaPropertyによる透過設定の使い方](http://skmod.hatenablog.com/entry/mesh/Nifskope5)
-[Save game script cleaner](http://www.nexusmods.com/skyrim/mods/52363/?):セーブデータのクリーニングツールです。
 使い方
 右上Openを押してセーブファイルを読み込みます。
 ゲーム内で一回セーブデータを読み込んでから、もう一度セーブすることで正しく適用されます。
 
 "FixScriptInstances" 孤立したスクリプトインスタンスの消去
 使われないで孤立しているインスタンスを消去します。
 使うには「FixScriptInstances」ボタンを押します。
 そのあと一度セーブデータをゲームで読み込んでからセーブが必要です。
 
 "Delete All #" 外したmodのスクリプト情報をセーブデータ内から消去
 セーブデータにodを外しても残っているクラスがある場合は#マークがつくので、それを一括で除去する機能です。
 「Delete All #」ボタンを押すだけです。
-[LOOT](https://www.nexusmods.com/skyrimspecialedition/mods/1918/?tab=description)
--[捻じ曲げるSkyrim Skyrim再構築第三回目（Mod Organizer解説編）](http://twistskyrim.blog.jp/)
--[Rolling Sweet Roll 【Skyrim&SE】MODのロードオーダーを最適化”LOOT”の使い方（ロードオーダーはMOD管理に非常に大事）](https://jazbay.com/skyrim/archives/15227)

##User Interface 
-[SKY UI](http://skyrim.2game.info/detail.php?id=3863): Skyrimのインターフェース周りを劇的に改良
--[SkyUIの使用方法について その1](http://semakimomo.net/post-053/)
-[UIExtensions](http://skyrim.2game.info/detail.php?id=57046&no=1):別種のメニュー形態を追加する
--[AddItemMenu - Ultimate Mod Explorer](http://skyrim.2game.info/detail.php?id=64905):導入後、自動でAddItemMenu v2 Packがアイテム欄に入っているので使用してAddItemMenuの呪文書とアイテムを手に入れてください
アイテムが使えない時は捨ててから拾えば使えるようです
AddItemMeuを使うと表示されるMOD一覧の中から任意のMODを選択すると
そのMODに含まれるアイテムが四次元ポケットのように入手できます。
-[Alternate Start - Live Another Life](http://skyrim.2game.info/detail.php?id=9557):ゲームをさまざまな場所から派閥に所属した状態でスタート出来るMOD。
-[A Closer Look - Simple Smooth Hotkey Zoom](http://skyrim.2game.info/detail.php?id=64981):ホットキーによるズームを可能にします
-[PapyrusUtil - Modders Scripting Utility Functions](http://skyrim.2game.info/detail.php?id=58705):高機能なSKSEプラグイン
-[Quick Menus](http://skyrim.2game.info/detail.php?id=74133):宝箱等のコンテナや家、NPC、あらゆるオブジェクトに簡単にアクセスする為のメニューを提供します。
--必須MOD: UIExtensions, PapyrusUtil
--[Quick Menus Adult Plugin 日本語マニュアル](https://mod-quickmenus-02.blogspot.jp/p/about-001.html):Quick Menusの成人向けプラグインです。
-[Customizable Camera](http://skyrim.2game.info/detail.php?id=37347):ゲーム内でカメラ位置やズームスピードを動的に変更可能になります。
--[Customizable Camera with MyTPC](http://skyrim.2game.info/detail.php?id=49262):オリジナル版のカメラ位置規定機能に加え、肩越し視点（納刀3人称カメラ位置）をキーボードのカーソルキーで上下左右へずらせる機能（以下MyTPC）が追加されています。動画撮影向き。
---[LL #6378](http://www.loverslab.com/topic/19129-where-can-i-find-non-adult-skyrim-requests/page-319?hl=mytpc):15年の10月4日に、雑談スレに1.13が上がってる
-[Better Free Camera](http://skyrim.2game.info/detail.php?id=78389):スクリーンショット撮影に便利なホットキーを追加します。
-[On-off console with Rshift](http://skyrim.2game.info/detail.php?id=5975):コンソールの起動・終了コマンドを『半角/全角』から『右shift』に変更します。
-[Mfg Console](http://skyrim.2game.info/detail.php?id=44596):コンソールコマンドの追加。コンソール自体の機能も使いやすいように拡張。
-[RaceMenu](http://skyrim.2game.info/detail.php?id=29624):キャラクターエディット画面(ShowRaceMenu)を大幅に拡張します。
-[SkyUI - show armor slots - updated](http://skyrim.2game.info/detail.php?id=84957):SkyUI環境下で防具の装備スロットを表示できるアドオンの、v5.1正式対応版。

##コンソールコマンド 
|プレイヤー移動|ヴェックス|player.moveto 28938|
||エイドリアン・アヴェニッチ|player.moveto 1a67c|
||アーンゲール|player.moveto 886b3|
||カーリア|player.moveto 58F1A|
||セラーナ|player.moveto 2002b74|
|馬の場所に移動|購入した馬|player.moveto 68d74|
||シャドウメア|player.moveto 9ccd8|
||フロスト|player.moveto 97e1f|
||その他の馬|player.moveto 10160c|
|||player.moveto 10160d|
|||player.moveto 798eb|
|||player.moveto 5c5ab|
|馬を呼び出す(複製)|馬|player.placeatme 68cfa|
||シャドウメア|player.placeatme 9ccd7|
||フロスト|player.placeatme 97e1e|
|コンソール移動|テストセル（セーブ用）|coc QAsmoke|
||ホワイトラン|coc WhiterunOrigin|
||ドーンガード砦|coc DLC1HunterWorldFort02|
||Zaz animation test|coc zbftestzone|

## 環境 
###キャラメイク 
-[Character Preset PRISONER for ECE 3](http://killingdoll.com/?p=13790):ちょっと目付きがキツくて気が強そうな美人CMEファイル。ダウンロードしたCMEファイルを、C:\Users\アカウント名\Documents\My Games\Skyrim\CME_save内に入れておき、キャラ作成画面にてプリセットを読み込む事によりキャラデータを読み込めます。（Enhanced Character Editの機能）

###スクリーンショット 
-[KurooNeko Photo Studio](http://skyrim.2game.info/detail.php?id=76962):リバーウッドにSS撮影のためのスタジオを追加します。スリーピングジャイアント裏手、落とし戸から移動できます。
-[Nausicaa - Photo Studio](http://skyrim.2game.info/detail.php?id=52833):SS撮影のためのスタジオを追加します。 NPCは魔法、PCは装備にて。
-[Jaxonz Positioner](http://skyrim.2game.info/detail.php?id=52583):オブジェクトを自由に配置できるようにするMOD。掴めるオブシェクトだけでなく、設置されているオブジェクトも動かせます。
-[ScreenshotPad](http://skyrim.2game.info/detail.php?id=69120):ホットキー長押しによるプレイヤーキャラクターの位置調整・回転・拡大縮小を可能にします。
-[Relationship Dialogue Overhaul - RDO](http://skyrim.2game.info/detail.php?id=74568):50種類以上のボイスタイプに対して、完全に音声つきのNPCのダイアローグを5,000行分以上追加します。
--[Relationship Dialogue Overhaul - RDO - Japanese](http://skyrim.2game.info/detail.php?id=82374):ダイアログ改変modの決定版Relationship Dialogue Overhaul - RDOの日本語音声パッチ。

##サウンド 
--[Lucidity Sound FX](http://skyrim.2game.info/detail.php?id=73838):現バージョンでバニラ効果音の100%、計4681のサウンドファイルがリプレイスされます。ヘッドフォンやPCのスピーカーを通じて素晴らしい聴き心地となるよう全ての工程で手を抜かずに作られたとのこと。espは無効にしても可。

##ENB 
-[ENB Man - An ENB Manager](http://skyrim.2game.info/detail.php?id=57620):ENB管理ツール。Microsoft .NET Framework v4.0が必要。

-[IMAGINATOR - Visual Control Device for Skyrim](http://skyrim.2game.info/detail.php?id=13049):ゲーム内でコントラスト・彩度・空の明るさ・太陽光の調整など
変更できるヘルパーを召喚できるようになります。

 Pixarを0.1上げるだけでも違う。

 現在の設定。
 Presets:
 Magic Hour 0.5
 Pop Photo Shoot 0.2
 Pixar 0.2
 Contrast 25
 Brightness 0
 Saturation -100
 Cinemagic:
 Sunlight 2
 Sky -3
 Tintor:
 Blue 10
 Cyan 10
 Green 10

-[PerformanceXP ENB](http://skyrim.2game.info/detail.php?id=53083):視覚効果を最小限に抑えたパフォーマンスに優しいENBプリセットです。
--[Skyrim　MOD導入記録 ENBの導入を始めよう。](http://bonk7.hatenablog.com/entry/2015/02/19/085111):動作が軽い、PerformanceXP ENB を使います。

-[Air ENB](http://skyrim.2game.info/detail.php?id=56020):Pure Weather専用に調整されたENBです。
--[Purity](http://skyrim.2game.info/detail.php?id=65242):Pure Weather,Pure Waters,Pure Waters - Waterfallsをマージした上で再調整した景観オーバーホールです。

-[RealLike ENB](http://skyrim.2game.info/detail.php?id=22056):美しさと軽さを重視したENBセッティングです。
-[VandB ENB Nature](http://skyrim.2game.info/detail.php?id=65584):ENBセッティング。
-[DYNAVISION - Dynamic Depth of Field](http://skyrim.2game.info/detail.php?id=12525):ゲーム内でDepth of Field（焦点付近以外をぼかす視覚効果）の
ON/OFF切り替えが可能になります。ENBのDoFとは違いゲームのパフォーマンスが低下することはありません。
-[Toric law of nature ENB](http://skyrim.2game.info/detail.php?id=53878):Pure Weather用に設定されているENBセッティング。
 ●必須
 Skyrim ENB Helper
 Skyrim particle patch for ENB
 ENB本体から "d3d9.dll" ファイルと"enbhost"ファイルが必要です（v0.264推奨）
 http://www.enbdev.com/download_mod_tesskyrim.htm
 ●SkyrimPrefs.ini設定
 bTreesReceiveShadows=1
 bDrawLandShadows=1
 bFloatPointRenderTarget=1
 Skyrimのランチャーまたはグラフィックカードドライバからアンチエイリアシングと異方性フィルタリングを無効にして下さい
-[RedShift Performance ENB Preset](http://skyrim.2game.info/detail.php?id=55134):映像クオリティとハイパフォーマンスを両立させたプリセット。
-[Kwanon ENB](http://skyrim.2game.info/detail.php?id=85321):女性キャラ用エディットパーツの総合美化Mod Fair Skin Complexion 等で有名な、HHaleyy氏によるENBプリセット。
-[Meiko and Hana ENB](http://skyrim.2game.info/detail.php?id=75632):２つのENBプリセット、Meiko ENBとHana ENBです。ファンタジー寄りの色相です。色が強く、そこに光と影があり、 明るい室内、暗すぎない夜。
-[Kwanon ENB](https://skyrim.2game.info/detail.php?id=85321):Fair Skin Complexion 等で有名な、HHaleyy氏によるENBプリセット。
-[Gameplay Performance ENB](https://skyrim.2game.info/detail.php?id=53100):フレームレートの低下を最小限に抑えながらイマージョンを向上します。
-[RYA ENB](https://skyrim.2game.info/detail.php?id=90473):DLCの土地やModで追加された土地の天候にも幅広く対応したフォトリアルなENB

##結婚 
-[Marriage Mod - To Have And To Hold](http://skyrim.2game.info/detail.php?id=50121):結婚システム拡張MOD。結婚式イベントの拡張や、離婚や重婚の実装など。
-[divorce](http://skyrim.2game.info/detail.php?id=2224):コンソールから伴侶を選択し bat divorce と入力すると離婚できるMODです。再度結婚が可能になるには24時間以上時間をすすめる必要があります。
 open console
 target an NPC
 bat divorce
-[Marriable Serana](http://skyrim.2game.info/detail.php?id=28685):DawnguardのメインクエストKindred Judgment(同類の判断)と母親への助言を完了後
セラーナとの結婚を可能にします。
-[Lovers in Skyrim - Multiple Lovers - Adopt child and pet - Not Multiple Marriage](http://skyrim.2game.info/detail.php?id=71707):正式に結婚した配偶者以外に恋人を作ることができるようになります。結婚している状態で他の恋人候補たちに、マーラのアミュレットを装備したまま話しかけると専用の選択肢が追加され、恋人にすることができます。
--[Serana is My Lover... and my spouse.](http://skyrim.2game.info/detail.php?id=71972):セラーナと恋人関係になれるMODです。

##養子 
-[Dolls- children Overhaul](http://skyrim.2game.info/detail.php?id=72569):子供の美化MOD。じゃがいもフェイスからアニメ調に生まれ変わります。
-[Hearthfire multiple adoptions - Now with custom home support for kids and spouse](http://skyrim.2game.info/detail.php?id=29249):Hearthfireで最大6人の養子を迎える事ができるようになります。
--[Comphy Pool Breezehome](http://skyrim.2game.info/detail.php?id=38393):ブリーズホーム改装MOD。広大な地下エリアが追加されます。
-[Skyrim Unadoption Mod](http://skyrim.2game.info/detail.php?id=47259):養子縁組を解除する魔法（パワー）を追加します。コンソールを開き、子供をクリックしたのち、"addfac XX04290 1"と入力し、実行する。（XXはHearthfires.esmのロードオーダー）

##別荘 
-[Wind Path](http://skyrim.2game.info/detail.php?id=74283):イヴァルステッド近郊の山中にプレイヤーの家を追加。DLC不要。
-[Leaf Rest](http://skyrim.2game.info/detail.php?id=33661):リバーウッドにプレイヤーの家を追加。
-[White River Cottage](http://skyrim.2game.info/detail.php?id=54479):White River Cottage追加。場所はリバーウッドの橋の近く。購入費用は15000、家族が暮らすのにうってつけの物件です。
-[Player House Elsidor Jorvaskr with companions](http://skyrim.2game.info/detail.php?id=11039):ファルクリース北に「Elsidor Jorvaskr」通称 娼婦の館を追加します。
-[Heros Hideout](http://skyrim.2game.info/detail.php?id=37934):ホワイトランの地下に、家となる居住空間を構えます。
-[Dragonstead - Multiple Adoption Friendly](http://skyrim.2game.info/detail.php?id=52980):場所はイリナルタ湖東岸。リバーウッドの南西の岸辺です。SSを見ると、レイクビュー邸の対岸に位置しているようです。
-[Teleport Room magic](http://skyrim.2game.info/detail.php?id=73599):セーブ部屋や自宅として使える部屋に出入りする魔法を追加します。魔法書の入手はコンソールかAddItemで。
-[Eden AO Retreat by Brendan62](http://skyrim.2game.info/detail.php?id=34327):カースワステン北東にドゥーマー式の建造物「Eden AO Retreat」を追加します。
多くの絵画、彫像、奴隷、裸のNPC、拷問器具、牢屋などアダルト指向な家になっており、
ガード、商人、コック、鍛冶屋、フォロワー、ハスキーなど総勢88人以上のNPCがいます。
商人から鞭や奴隷用装備、このMODのガードと同じ装備を購入出来ます。
敷地は広大で庭園、馬付きの厩舎、各種生産設備、プール、武器庫、バー、アリーナ、
ライブラリ、ベッドルーム、拷問部屋、監獄など有り。

##風呂 
-[Open-air bath in cities - Yukemuri Skyrim](http://skyrim.2game.info/detail.php?id=58865):スカイリムの都市に、市内からシームレスに利用できる露天風呂を追加します。
-[Underground Bathhouse and Paradise Valley](http://skyrim.2game.info/detail.php?id=27361):ホワイトラン東に10人の女性NPCが住む浴場「Underground Bathhouse」を追加します。
--[Underground Bathhouse - Friendlier Guards Patch](http://skyrim.2game.info/detail.php?id=52090):Underground Bathhouse and Paradise Valley のためのパッチです。外から連れてきたフォロワー化可能な一部のNPCに対して地下大浴場の警備兵が敵対反応してしまう不具合を直します。
--[Underground Bathhouse and Paradise Valley Mod Follower Facial Plastic Surgery](http://skyrim.2game.info/detail.php?id=76205):Underground Bathhouse and Paradise ValleyのNPCの容姿を変更します。
-[Lakeview Manor Avant Garden for Hearthfire](http://skyrim.2game.info/detail.php?id=36960):Lakeview Pool and Hot Bath for Hearthfireの第2弾。レイクビュー邸の購入や建築に干渉しません。
-[Heljarchen Pool and Hot Bath for Hearthfire](http://skyrim.2game.info/detail.php?id=36776):ヘリヤーケン・ホール横に露天風呂とプールを追加します。
-[Bathing Beauties or Beefcake - Luxury Suite](http://skyrim.2game.info/detail.php?id=11427)ホワイトラン東に美人が集う「Luxury Suite」公衆浴場的な建物を追加します。
--[BBLuxurySuiteNpcSp Ver 1.2](http://www.pinktower.com/?http://cyclotron.moe.hm/up/skyrim/fileup/src/cysk1287.7z.html):美化mod

##マネキン 
-[Mannequin body replacers](http://skyrim.2game.info/detail.php?id=22126):マネキンを女性NPCの姿に置換します。狩猟の女神アエラ、アルバ（モーサルの吸血悪女）、リセッテ（ソリチュードの吟遊詩人）、リディア、ホロキ、セラーナ、イソルダから一人選ぶ。
-[Stags Rest Player Home](http://skyrim.2game.info/detail.php?id=23847):ウィンドヘルム南西にプレイヤーの家「Stags Rest」を追加します。各種設備有り。9大神の祠、石牌、本棚、マスクラック、各アイテムストレージ、マネキン54、大量のディスプレイケース、武器ラック93、シールドプラーク18。

##クエスト 
-[Alternate Start - Live Another Life](http://skyrim.2game.info/detail.php?id=9557):ゲームをさまざまな場所から派閥に所属した状態でスタート出来るMOD。
--[Alternate Start - Japanese Voice Patch](http://skyrim.2game.info/detail.php?id=85823):Alternate Start - Live Another Life用の日本語音声パッチ。
-[Falskaar](http://skyrim.2game.info/detail.php?id=37994):600年前にノルドが住み着いたとされる新大陸「Falskaar」を追加します。アンインストールはサポートされていません。
-[VIGILANT](http://skyrim.2game.info/detail.php?id=67103):決して注意を怠ってはいけない闇の物語。
-[Unslaad](http://skyrim.2game.info/detail.php?id=80425):VIGILANTやVicn Creature Packで有名なVicn氏による、新規小クエストの追加MOD。半竜に関するクエストと、もっふもふな装備やクリーチャーを追加します。
-[Legacy of the Dragonborn (Dragonborn Gallery)](http://skyrim.2game.info/detail.php?id=52248):スカイリム最大規模を誇るギャラリーをソリチュードのブルー・パレス脇に追加します。
--[Legacy of The Dragonborn Patch Central](http://skyrim.2game.info/detail.php?id=72921):Legacy of the Dragonborn (Dragonborn Gallery) に追加するMOD。インストール時に該当MODがある場合自動的にチェックピンが付きます。

###以下、お試し 
-[Mannequin Hall](http://skyrim.2game.info/detail.php?id=67906):ファルクリースの鍛冶屋の裏に「Mannequin Hall」に行ける地下への扉があります(マップマーカーあり)。十字状の通路に100以上のマネキンと展示箱があります。出口は入ったところの天井に。
-[Dovahkiin - Wardrobe Room - a lot Mannequins](http://skyrim.2game.info/detail.php?id=11444):ブリーズホームなど、５つの自宅にマネキン180体(Maximum versionは260体)のある空間にワープする扉を追加します。
-[Sjel Blad Castle](http://skyrim.2game.info/detail.php?id=41612):リバーウッド南東に広大な城「Sjel Blad Castle」を追加します。
城内では数多くのNPCが生活しています。屋内にあるオーブから各部屋へテレポート可能。武器庫、マネキン80体の他500以上の展示箱及び武器ラック。

###マネキン化可能フォロワー 
-[Pretty Assassin Companion Ari](http://skyrim.2game.info/detail.php?id=17302)

##その他 
-[Green Water Fix](http://skyrim.2game.info/detail.php?id=14007):水の中で視界が効くようになるFix。
-[Death Alternative - Your Money or Your Life](http://skyrim.2game.info/detail.php?id=45894):プレイヤーのHPが尽きた際、リスタートでなくペナルティを付加してプレイを継続させるMOD。
-[Fuz Ro D-oh - Silent Voice](http://skyrim.2game.info/detail.php?id=14884):音声のない会話に、無音の音声と口パク、文章の長さに合わせた待機時間を追加します。

###リンク 
-[真のノルドの覚え書き](http://blog.livedoor.jp/kotaz/)
--[Mod Organizerとちちくりあう再構築](http://blog.livedoor.jp/kotaz/archives/34628805.html)

##日本語化 
-[英語版Skyrimを日本語化する　～かんたん新手順～](http://blog.livedoor.jp/eeeop/archives/26431490.html)
-[sseTranslator](http://skyrimspecialedition.2game.info/detail.php?id=134):翻訳ツール。TESVTranslatorはバージョン2.0Beta12(2016年8月2日付)でFallout4Translatorと統合され、さらにsseTranslator(2016年11月2日付)と統合されました。
--[TESVTranslator](http://skyrim.2game.info/detail.php?id=29148):現在主流の日本語化ツール。esp・esm以外にStrings・MCMのTranslate・PapyrusPexに対応標準で日本語UIに対応している。
--[Skyrim MODを日本語化できるTESVTranslatorのダウンロードから使い方](http://zedlabo.com/skyrim-mod-japanese-tesvtranlator/)
-[Skyrim Strings Localizer](http://skyrim.2game.info/detail.php?id=2889):翻訳ツール。多言語に対応しています。通称「SSL」。
-[Japanese Custom Font](http://skyrim.2game.info/detail.php?id=69230):日本語圏向けのカスタムフォント。

#美化MOD 
##髪型 
-[ApachiiSkyHair](http://skyrim.2game.info/detail.php?id=10168):sims2、Oblivion、Witcherからヘアスタイルを追加します。
--[ApachiiSkyHair natural Retexture](http://skyrim.2game.info/detail.php?id=35092):髪MOD「ApachiiSkyHair」のリテクスチャ。ApachiiSkyHair - version 1_5_Full のいくつかをより自然になるよう変更。オリジナル導入後上書きしてください。

##顔 
-[Adorable Face](http://skyrim.2game.info/detail.php?id=61178):女性のフェイステクスチャを変更します。
--[作者ブログ](https://luminalion.blogspot.jp/)

##体 
-[Sunburn for UNP and CBBE](http://skyrim.2game.info/detail.php?id=14322):フル、Decolored Nipples(乳首脱色)、ビキニ、Swimsuit 1(競泳) 2(スクール水着系)、Thong(下のみ日焼け)の６タイプ。(Nexus側に画像あり)。
-[Sporty Sexy Sweat - wet body skin texture - CBBE UNP UNPB ADEC Vanilla](http://skyrim.2game.info/detail.php?id=28946):女性のボディテクスチャを濡れたスポーティなテクスチャにリプレイスします。
-[nice skin](http://skyrim.2game.info/detail.php?id=83431):nisetanaka氏が作成した肌（体2k・顔2k・手2k*1k）テクスチャ、UNP系用です。
--[The Amazing World of Bikini Armour!](http://www.loverslab.com/topic/77092-the-amazing-world-of-bikini-armour/):LLコメント欄にリンクあり。
-[Leyenda Skin](http://skyrim.2game.info/detail.php?id=73512):CBBE・UNPユーザー向け、ボディ＆フェイステクスチャ。

##NPC 
###NPC追加 
-[Immersive Wenches](http://skyrim.2game.info/detail.php?id=51189):スカイリムの宿屋と酒場に、ウェイトレスを追加します。

###NPC置き換え 
-[Tiny Serana and adoptable children plus Babette](http://skyrim.2game.info/detail.php?id=65155):セラーナ、ヴァレリカ、バベットの容姿を変更します。
-[Small Housecarls](http://skyrim.2game.info/detail.php?id=76588):リディア先輩とジョディス先輩、イオナ先輩を極めてロアアンフレンドリーなメイドさんに置き換えます。
-[Bijin NPCs](http://skyrim.2game.info/detail.php?id=71054):Skyrim内の特徴的なネーム付き女性NPCの外観をリプレイスします。
-[Bijin Warmaidens](http://skyrim.2game.info/detail.php?id=40038):女性フォロワーの容姿を変更します。特にソードメイデンのジョディス。
-[Bijin Wives](http://skyrim.2game.info/detail.php?id=63473):結婚可能な女性NPC(カミラ、イソルダ、シルグジャ、テンバ、ターリエ)の容姿を変更します。
-[Others Lover Ver1.1 (85人)](http://seesaawiki.jp/teslab/d/NPC%B4%E9%CA%D1%B9%B9):各男首長に愛人追加、人妻、他人の恋人などの顔を整形するmodです。
-[ChitamaNpcReplacer SeranaAndValerica](http://skyrim.2game.info/detail.php?id=81232):セラーナとヴァレリカをリプレイスとカスタムします。体型はSeveNBase Bombshell。
-[Female Bandit 2](http://blog.naver.com/sidearmf93/90190941021):要SGhair 268、SG Female Brows 
--[SG Female Eyebrows](http://skyrim.2game.info/detail.php?id=35327):26種の眉毛を追加します。また眉の色と髪の色が一致するようになります。
-[Fresh Women](http://seesaawiki.jp/teslab/d/NPC%B4%E9%CA%D1%B9%B9):ランダム生成される女性NPCを整形。
-[Younger Delphine and Smaller Ulfric and Tullius](http://skyrim.2game.info/detail.php?id=78052):エリシフ、デルフィン、リッケ特使をリプレイスします。

###モンスター置き換え 
-[Beautiful Draugr](http://seesaawiki.jp/teslab/d/NPC%B4%E9%CA%D1%B9%B9):ドラウグルを美少女に変更。
-[Falin(ファルマー Elin化)](http://c.2ch.net/test/-.lll/pinkcafe/1429690536/3-)

##リンク 
-[NPC美化 おすすめMOD順](http://skyrim.2game.info/tag/NPC%E7%BE%8E%E5%8C%96/#id37861)
-[【Skyrim】バニラNPCと関連システムを改善する定番MOD](http://skmod.hatenablog.com/entry/mod/osusume9)
-[【美人化】ゼロから始める初心者向けスカイリムMOD導入情報まとめ【2016年版】](http://matome.naver.jp/odai/2146687437160173801)

##CBBE 
--[Caliente's Beautiful Bodies Edition -CBBE-](http://skyrim.2game.info/detail.php?id=2666):UNP系ボディと並ぶ定番の女性裸体MOD、略称「CBBE」
---[CBBEv3M Body Repalacer](http://skyrim.2game.info/detail.php?id=13180):CBBEのお尻や太ももを大きくします
--[Body Options](http://skyrim.2game.info/detail.php?id=27352):CBBEのPubic Hairを20以上から選択して変更できます。バージョンアップでUNPにも対応し、ほくろを追加するファイル、乳首の色を変更するファイルも追加されました。
---How to blend:
 Now navigate to your "Skyrim/Data/CalienteTools/Body Options Blender" folder and double click "TexBlend.exe".
 1) At "Set:" select "Body and Feet".
 2) At "Type:" select "Color".
 3) Select what you want to blend from the middle list.
 Make sure you stick to the priority list. But if you don't want Body Muscles for example simply skip to Priority 2.
 4) Click on "Preview".
 5) Click on "Blend Images".
 6) Hit "OK" when completed.
 Repeat step 2 to 6 for any other options you want to blend.
 You NEED to reselect "Color" (step 2) as well as click on "Preview" every time  you blend a new option, if you don't do this Texture Blender wont reset what has been used last time. And you end up double blending everything.

--[Alternative Nude Texture for CBBE](http://skyrim.2game.info/detail.php?id=6232):CBBEのリテクスチャ。乳首や下の毛などの変更がはいっています。
---[Nipple Fix for Alternative Nude Texture for CBBE](http://skyrim.2game.info/detail.php?id=14415):CBBEのリテクスチャ「Alternative Nude Texture」の乳首を修正します。先にCBBEとオリジナルの導入が必要です。

--[CLAMS OF SKYRIM PROJECT Inni Outie HDT Vagina 5.1](https://www.loverslab.com/files/file/1829-clams-of-skyrim-project-inni-outie-hdt-vagina/):コリジョン。

###CBBE衣装 
--[R18Pn 00 - Heilige Mutter Armor for UNP and CBBE V3](http://skyrim.2game.info/detail.php?id=13098):Heilige Mutter Armorを追加します。UNP、CBBE、Weight対応。
---[Heilige Mutter Armor - CBBEv3M](http://skyrim.2game.info/detail.php?id=13243):Heilige Mutter Armorのお尻と太ももを少し大きくします。
オリジナルのCBBEverを導入後上書きして下さい。
--[Maxi Armor by Hentai -Nexus Exclusive-](http://skyrim.2game.info/detail.php?id=13386):Maxi Armorを追加します。UNP用、導入後はクラフト可能です。
---[Maxi Armor CBBEv3M](http://skyrim.2game.info/detail.php?id=14137):Maxi ArmorのCBBEv3Mバージョン(太ももやお尻がふっくら)を追加します。CBBE用、
オリジナル導入後上書きしてください。
--[Craftable Panties Bras and Stockings for CBBEv3M](http://skyrim.2game.info/detail.php?id=16837):パンティを追加します。CBBEv3M用、導入後は皮なめしの棚でクラフト可能です。バージョンアップでブラ、ストッキングも追加されました。

##UNP 
--[DIMONIZED UNP female body](http://skyrim.2game.info/detail.php?id=6709):自然なフォルムで人気の体型変更MOD。略称「UNP」
---[UNP Replacer Configuration Package](http://skyrim.2game.info/detail.php?id=20884):UNP、UNPB体型のNMM用インストールパッケージ
---[UNP HDT-PE BBP TBBP](http://skyrim.2game.info/detail.php?id=21199):UNPの標準体型をTBBP(乳と尻揺れ)に対応させた体型MODです。このMODにはfemalebody_0.nifとfemalebody_1.nifのみ含まれるため、別のUNP体型をインストールした後、こちらで上書きしてください。

###UUNP衣装 
--[Mini Dress Set UUNP FULL HDT](http://wtfuun.tumblr.com/post/162723717950/wtfuuun-mini-dress-set-uunp-full-hdt-require)

##UNPetite 
--[UNPetite](http://skyrim.2game.info/detail.php?id=35748):Aカップでくびれがあり、お尻が大きい体型です。
###UNPetie衣装 
--[UNP or UNPetite - Smithy Sex](http://skyrim.2game.info/detail.php?id=49680):裸に直接着用する鍛冶屋のエプロンを追加します。スタンドアロンUNP用とUNPetite用があります。
--[UNP or UNPetite - Hmm What To Wear](http://skyrim.2game.info/detail.php?id=22168):皮の鎧のUNP/UNPetite用リモデル。
--[UNP - Bondage - A MashUp by Nightasy](http://skyrim.2game.info/detail.php?id=19067):UNP用の「Bondage Armor」を追加します。
---[UNPetite - Bondage](http://skyrim.2game.info/detail.php?id=36046):UNPetite用にしたもの。

##UNPK 
###UNPK衣装 
--[Sexy Adventurer's Outfit with butt bounce UNPK](http://skyrim.2game.info/detail.php?id=53419):Adventurer's Outfit UNP-family compatibleアダルト版。
--[Black Rose - UNPK -](http://mitakusaner.blog.fc2.com/blog-entry-430.html)
---[Black Rose / n8k Black Rose II](http://mitakusaner.blog.fc2.com/blog-entry-290.html#more)

##UNPB 
--[UNP BLESSED BODY- UNPB REDUX PROJECT](http://skyrim.2game.info/detail.php?id=37900):UNPBチームによるUNPB体型のインストーラーパッケージ。UNPB 2.5
 既存のUNPB体型に加えTBBPや歩行モーションなど一式が揃えられた同梱版MODです。
 BAINとFomod形式に対応しています。
 ※スキンテクスチャはUNPのものを使用可能です。
---[TroubleMakers Clothing - UNPB UNP BBP BBPx TBBP MTM HDT-PE Female Body Replacer](http://skyrim.2game.info/detail.php?id=20227):DIMONIZED UNP female bodyより調整できるバストサイズ大きくした「UNPB」、UNPBを乳揺れ(BBP)に対応させた体型「UNPB BBP」、乳揺れを大きくする「UNPB BBPx」、お尻も揺らせる「UNPB TBBP」、またはUNPを乳揺れに対応させる「UNP BBP」を導入します。
--[7B＆UNPB向けのパンティMODを作ってみました -PS Lace Panty-](http://reachthepinksky.blog.fc2.com/blog-entry-66.html):リバーウッド入口付近にある簡易キャンプ近くの木のふもとにチェストあり
---[FF12アーシェの衣装を作ってみました -FF12 Ashe Outfit-](http://reachthepinksky.blog.fc2.com/blog-entry-65.html)
--[Lingerie Set for the UNPB BBP Body](http://skyrim.2game.info/detail.php?id=34308):ランジェリー「NPR Lingerie Set」を追加します。TES4MODから移植されたMOD。UNPB-BBP用、重量スライダー対応。

##UNPB Classic (HDT-SMP vers) 
-[UNPB Classic (HDT-SMP vers)](http://skyrim.2game.info/detail.php?id=88921&no=1)

##UNPBO 
###UNPBO衣装 
--[fox57 Armor](http://eiheispot1.blog.fc2.com/blog-entry-656.html):重装タイプの下着を追加します。ウェイト100専用。衣装は通常版とスケスケ版の二種類あります。
--[Dark Rose 2 UNPBO](http://mitakusaner.blog.fc2.com//blog-entry-1830.html)
---[Dark Rose 2 (UNP)](http://mitakusaner.blog.fc2.com/blog-entry-1274.html)

##7BCH 
###7BCH衣装 
--[R18PN 04 - Amy AM Set - 7BCH -](http://mitakusaner.blog.fc2.com/blog-entry-771.html):NPR氏のOblivion用MOD、 R18PN 04 - Amy AM Set (Nexus) のSkyrimへの移植 。

##TMB 
###TMB衣装 
--[Vanilla Armors and Clothes – TMB](http://robton.nu/vanilla-armors-and-clothes-tmb/)

##UN7B 
-[UN7B and New (High Heels) Feet - A New Body Replacer made by Alan and H2CO3 from ANK](https://www.nexusmods.com/skyrim/mods/54814/)

##[Skyrim Mod データベース](http://skyrim.2game.info/) 

--[ECE(Enhanced Character Edit)](http://skyrim.2game.info/detail.php?id=12951):ヘッドパーツの追加・修正、スライダーの追加、追加種族、
現実的なカラーの追加
--[ShowRaceMenu Alternative](http://skyrim.2game.info/detail.php?id=20394):専用の空間に飛んだあと、修正されたキャラメイク画面に移行
--[ShowRaceMenu Precache Killer](http://skyrim.2game.info/detail.php?id=33526):キャラクターエディット(showRaceMenu)実行時メモリ不足によりCTDしてしまうの防ぐ
--[univision Face](http://skyrim.2game.info/detail.php?id=14569):美顔Mod。導入すると美顔キャラが圧倒的に作りやすくなる。
--[SG Female Textures Renewal](http://skyrim.2game.info/detail.php?id=35267):CBBE・UNPユーザー向け、ボディ＆フェイステクスチャ
--[Female Facial Animation](http://skyrim.2game.info/detail.php?id=35303):女性の表情、会話時の口の動きを改善します。
--[Face to face conversation](http://skyrim.2game.info/detail.php?id=30533):NPCとの距離に応じてFOV変更機能
--[Girl of the Innocence](http://skyrim.2game.info/detail.php?id=76405):同作者さんのAdorable Faceよりリアル寄りでちょっと光源に強い。以下のテクスチャを上書き。
---SG Female Textures Renewal
---univision Face
---ECE(Enhanced Character Edit)
---UNP Replacer Configuration Package
--[Mikan Eyes](http://skyrim.2game.info/detail.php?id=56056):人間種族用に新しい目を追加します
--[Body Options](http://skyrim.2game.info/detail.php?id=27352):CBBEのPubic Hairを20以上から選択して変更できます。バージョンアップでUNPにも対応し、ほくろを追加するファイル、乳首の色を変更するファイルも追加されました。
--[BodyChange - A Multi-Bodyshape System](http://skyrim.2game.info/detail.php?id=37546):体型及びフェイステクスチャをゲーム内で動的に変更出来るようになります。
--[Fair Skin Complexion](http://skyrim.2game.info/detail.php?id=51602):女性キャラクター用エディットパーツの総合美化Mod。顔、体、眉、歯、そばかす、化粧をリプレイスします。
--[Meridia's Light](http://skyrim.2game.info/detail.php?id=32842):メリディアの杖「Meridia's Light」を追加します。装備中はあたりを照らし、近くにいるアンデッドや吸血鬼に太陽ダメージをわずかに与えます。防御キーで魔力の盾を展開します。
--[UNP Spice Gear Collection](http://skyrim.2game.info/detail.php?id=68028):UNP Minidresses Collectionの作者によるバニラ装備（ARMOR）のリプレイス。ノーマルとBBP版のファイルが有ります。

##[Eihei Spot!](http://eiheispot1.blog.fc2.com/) 

###導入済み 
--[RANs FFT-Archer](http://eiheispot1.blog.fc2.com/blog-entry-214.html):戦乙女の炉付近のチェストから入手 :◎
--[Shedding Lace UD](http://eiheispot1.blog.fc2.com/blog-entry-485.html):革カテゴリでクラフト可能 : ◎
--[Heilige Mutter Armor](http://eiheispot1.blog.fc2.com/blog-entry-86.html):革カテゴリでクラフト可能: ◎
--[Summer Breeze](http://eiheispot1.blog.fc2.com/blog-entry-377.html):軽装タイプの衣装MOD。導入後は革カテゴリでクラフト可能です。各パーツは胴装備と一体化しています。パンツは付属していません。
--[Spring Dress](http://eiheispot1.blog.fc2.com/blog-entry-361.html):オブリビオンMODから移植された衣服MOD。
--[Mini Sage Outfit](http://eiheispot1.blog.fc2.com/blog-entry-215.html):衣服『Mini Sage Outfit』を追加します。
--[Chapi JC Collection](http://eiheispot1.blog.fc2.com/blog-entry-65.html):セクシー衣装パックMOD。
--[Kasprutz Muses Clothing](http://eiheispot1.blog.fc2.com/blog-entry-458.html):黒い砂漠で登場する衣装MOD。パーツは頭、アミュレット、胴、手、パンツ、足に分かれていました。導入後はドラゴンズリーチにある鞄から入手できます。
--[Dorothy Shepherdess](http://eiheispot1.blog.fc2.com/blog-entry-465.html)
マビノギ英雄伝で登場する衣装MOD。導入後はドラゴンズリーチにある金庫から入手します。
--[Vindictus Mini Dress](http://eiheispot1.blog.fc2.com/blog-entry-272.html):マビノギ英雄伝で登場する衣装MOD。UNP。導入後はコンソールから入手。
--[Honoka Rodeo Time](https://eiheispot1.blog.fc2.com/blog-entry-951.html):DEAD OR ALIVE で登場する衣装MOD。CBBE。導入後はコンソールから入手。パーツは帽子（サークレット）、アミュレット、胴、腕、ホルスター、ストラップ、ベルト、パンツ、スカート、足に分かれていました。
--[Li Honoka](https://eiheispot1.blog.fc2.com/blog-entry-977.html):DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手。パーツはウィッグ（頭）、胴、ストラップ、パンツ、スカート、足に分かれていました。
--[DOA5 Honoka](https://eiheispot1.blog.fc2.com/blog-entry-984.html):DEAD OR ALIVE 5 で登場する衣装MOD。導入後はコンソールから入手。パーツは胴、パンツ、足に分かれていました。
--[[Honoka Officer Suit [CBBE]:https://eiheispot1.blog.fc2.com/blog-entry-993.html]]:DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手。パーツは胴、スカート、足に分かれていました。
--[Honoka Halloween 2017](https://eiheispot1.blog.fc2.com/blog-entry-999.html):DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手。UNPBO。パーツはウィッグ（頭）、胴、スカート、足に分かれていました。
--[Honoka Cheerleader](https://eiheispot1.blog.fc2.com/blog-entry-1019.html):DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手してください。CBBE。パーツは胴、腕、手、スカート、パンツ、足に分かれていました。
--[Kokoro Halloween](https://eiheispot1.blog.fc2.com/blog-entry-1022.html):DEAD OR ALIVE 5 で登場するハロウィンコスチュームMOD。導入後はコンソールから入手。CBBE。パーツはカチューシャ、ウィッグ（頭）、アミュレット、胴、羽、腕、手、
腹、ベルト、スカート、パンツ、ストッキング、足に分かれていました。
--[IcyV Haku Wedding Dress](https://eiheispot1.blog.fc2.com/blog-entry-998.html):軽装タイプのウェディングドレスを追加します。UNP。パーツはサークレット、胴、手、足に分かれていました。衣装名が文字化けしています。ショートタイプは白のみ。

###テスト中 
--[UNP Minidresses Collection Full Standalone](http://killingdoll.com/?p=21478):ミニなロアフレ衣装の決定版。バニラの装備類を全てミニ丈に改変したMOD 。
--[SexyVest](http://eiheispot1.blog.fc2.com/blog-entry-842.html):UNPB、パーツは胴のみです。
--[BNS valentine's fasion](http://eiheispot1.blog.fc2.com/blog-entry-583.html):ブレイドアンドソウルで登場する衣装MOD。
--[Yarl Dress](http://eiheispot1.blog.fc2.com/blog-entry-595.html):衣服タイプのドレスを追加します。UUNP HDT/ SeveNBase版。
--[Miyus Clothes Mix](http://eiheispot1.blog.fc2.com/blog-entry-829.html):軽装タイプの衣装パックを追加します。制服。
--[Short Sleeve Mini Dress](http://eiheispot1.blog.fc2.com/blog-entry-815.html):SeveNBase、軽装タイプの衣装を追加します。導入後はコンソールから入手。パーツは胴のみです。
--[Kailani Bikini](http://eiheispot1.blog.fc2.com/blog-entry-899.html):衣服タイプの水着を追加します。導入後はコンソールから入手。パーツはアミュレット、胴、スカート、パンツ、足に分かれていました。
--[LOVE LIVE CLOTHING](https://eiheispot1.blog.fc2.com/blog-entry-932.html):ラブライブ！で登場する衣装MOD。導入後はコンソールから入手。パーツは帽子（サークレット）、胴、手、パンツ、足に分かれていました。
--[Leifang Hot Summer](https://eiheispot1.blog.fc2.com/blog-entry-1008.html):DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手。CBBE。パーツはメガネ、耳、上衣、胴、腕、パンツに分かれていました。
--[[Leifang Aqua Plus [CBBE]:http://eskrimmods.blogspot.com/2017/11/leifang-aqua-plus-cbbe.html]]
--[Half Vampire Wedding Dress](https://eiheispot1.blog.fc2.com/blog-entry-1041.html):軽装タイプのドレスを追加します。導入後はコンソールから入手。UNPB。パーツは胴、腕、パンツ、足に分かれていました。
--[Asker Rhian](https://eiheispot1.blog.fc2.com/blog-entry-1078.html):オンラインゲーム『Asker』 で登場する衣装MOD。導入後はコンソールから入手。パーツはウィッグ（頭）、胴、リボン、スカート、足に分かれていました。
--[Asker Black Eye Kid](https://eiheispot1.blog.fc2.com/blog-entry-1080.html)オンラインゲーム『Asker』 で登場する衣装MOD。導入後はコンソールから入手。パーツは帽子（頭）、ウィッグ（頭)、胴、パンツ、足に分かれていました。
--[High Society](https://eiheispot1.blog.fc2.com/blog-entry-1097.html):DEAD OR ALIVE で登場する衣装MOD。導入後はコンソールから入手。パーツは胴、パンツ、足に分かれていました。
--[DEM Linen](https://eiheispot1.blog.fc2.com/blog-entry-1092.html):HDT-SMP対応の衣装。導入後はコンソールから入手。パーツはウィッグ（頭）、耳、アミュレット、胴、足に分かれていました。
--[Wuyi8](https://eiheispot1.blog.fc2.com/blog-entry-1098.html):軽装タイプの防具を追加します。導入後はコンソールから入手。パーツはヘルメット（頭）、バックパック、胴、手、足に分かれていました。
--[Cre FF Tifa](https://eiheispot1.blog.fc2.com/blog-entry-1115.html):ファイナルファンタジーで登場する衣装MOD。ウェイト100専用。導入後はコンソールから入手。パーツは胴、手、足に分かれていました。
--[Bloodcrystal Dress](https://eiheispot1.blog.fc2.com/blog-entry-1161.html):軽装タイプのドレスを追加します。パーツは胴と足に分かれていました。UNP。
--[Rock Lady](https://eiheispot1.blog.fc2.com/blog-entry-1162.html):軽装タイプの衣装を追加します。パーツは胴、パンツ、足に分かれていました。UNPB。
--[Sinful Trench Coat and Lingerie](https://eiheispot1.blog.fc2.com/blog-entry-1178.html):衣服タイプ、コンソールから入手。7BO。パーツは胴、ブラ、パンツに分かれていました。

###ペンディング中 
--[Poser Sweet dreams clothes](http://eiheispot1.blog.fc2.com/blog-entry-460.html):ドラゴンズリーチにあるチェストから入手：CBBE
--[Artificial Academy](http://eiheispot1.blog.fc2.com/blog-entry-483.html):ドラゴンカテゴリでクラフト可能：CBBE
--[Hentai SchoolGirl Uniform](http://eiheispot1.blog.fc2.com/blog-entry-481.html):皮なめしの棚で作成可能：CBBE
--[Galoneal Dress](http://eiheispot1.blog.fc2.com/blog-entry-308.html):ドラゴンとデイドラカテゴリでクラフト可能：CBBE
--[Vamp](http://eiheispot1.blog.fc2.com/blog-entry-171.html):皮カテゴリでクラフト可能：UNPB
--[Ashara Princes of the Woods](http://eiheispot1.blog.fc2.com/blog-entry-219.html):鋲付きカテゴリでクラフト可能：UNPB
--[Classy Dress](http://eiheispot1.blog.fc2.com/blog-entry-370.html):ドラゴンカテゴリでクラフト可能：UNP(CTD)
--[Nuova Donna](http://eiheispot1.blog.fc2.com/blog-entry-368.html):革カテゴリでクラフト可能：UNP(CTD)
--[Motto ToLove RU](http://eiheispot1.blog.fc2.com/blog-entry-417.html):革カテゴリでクラフト可能：UNP(CTD)
--[Shuffle Uniform and Hat](http://eiheispot1.blog.fc2.com/blog-entry-495.html):革カテゴリでクラフト可能：NG

##[LoversLab](http://www.loverslab.com/) 
###Fox 
-[Fox Collection update 29th september](http://www.loverslab.com/files/file/1873-fox-collection/)
--[Fox 14](http://killingdoll.com/?p=17336):3 Piece Girls Clothing。まな板仕様のドレス3着です。
--[Fox 19](http://killingdoll.com/?p=17507):fox6000氏の衣装MODシリーズの19着目の衣装。CBBE体型用。ワカメばりのパンツ丸見えミニドレスと他2着です。
--[Fox 27](http://killingdoll.com/?p=17914):体操着、ロリ衣装+ランドセル、裸エプロン風ワンピースの3着。
--Fox 39:Lingerie
--[FoxGirlsClub](http://skyrim.2game.info/detail.php?id=73021):毎度おなじみFoxさんの店MOD。今回はプレイルームやショールーム、ミルク製造室？らしき部屋があり、搾りたて生ミルクや大人の玩具も発売してる模様。女性達が着ている装備は店の中で手に入ります
---[FaceHugger 4.0](http://modtype.doorblog.jp/archives/47962975.html#more):フェイスハガーMOD。FoxGirlsClub内(FoxGirlsClub同梱)。フェイスにはハグしない。装備すると喘ぎ声が出る。装備すると汁が出る。

-[Fox Collection Merged Patch](http://tepodon.blog.jp/archives/8415856.html):Fox衣装を一括で追加するMOD。導入後は「AddItemMenu」で入手。（鍛冶・クラフトも可能）

-[FoxMerged 2 2.6](http://www.loverslab.com/files/file/977-foxmerged-2/):FOXシリーズ全種類の服や防具を１つのESPファイルにまとめたFoxMerged 2 2.3を追加してくれるMod。導入後は、鍛冶の各カテゴリにてクラフト又はリバーウッドに設置されるFox Shopで全て入手出来ます。

###SOS 
-[SOS schlong for females - UNP](http://www.loverslab.com/topic/20211-sos-schlong-for-females-unp/):女性用
--[SOS - Schlongs of Skyrim 3.00.004](http://www.loverslab.com/files/file/498-sos-schlongs-of-skyrim/):SOSが必要
--[XP32 Maximum Skeleton - XPMS](http://www.nexusmods.com/skyrim/mods/26800/?):XPMSが必要
---[Realistic Ragdolls and Force](http://www.nexusmods.com/skyrim/mods/601/?):XPMSのRequirement

###Private needs 
-[Private Needs Discreet](http://www.loverslab.com/files/file/948-private-needs-discreet/)
--[PND Overhaul Patch Vol3.5 Shinshi Edition （魔改造パッチ）](http://tepodon.blog.jp/archives/12157912.html):NPCの会話時の行為要求選択肢に「ここで全裸になってくれ」という選択肢を追加。

###OSex 
-[Osex](http://skyrim.2game.info/detail.php?id=69448):アニメーション再生のための新しいフレームワーク "OSA" で利用できるアダルトモジュール。
--[OSA - Skyrim Ascendancy Engine](http://skyrim.2game.info/detail.php?id=76744):アニメーションのためのフレームワークです。
--[NetImmerse Override](http://skyrim.2game.info/detail.php?id=37481)
-[TropicalIsland](http://skyrim.2game.info/detail.php?id=81267):ヌーディストビーチ「Tropical Island」を追加します。ウィンドヘルム港のグジャランド・ソルトセイジに話しかけ、運賃を払って島に移動します。
-[Poser Module for OSA](http://www.loverslab.com/files/file/3086-poser-module-for-osa-skyrim-ascendancy-engine/):A simple module for OSA that includes an intuitive and very easy to navigate list of Poses.

###sexlab 
-[Sexy Adventures in Skyrim 1.4](http://www.loverslab.com/files/file/148-sexy-adventures-in-skyrim/)
-[Downloads - SexLab Framework](http://www.loverslab.com/forum/51-downloads-sexlab-framework/):アニメーションや基本的な動作をまとめ、基礎としたMOD。
--[えびろぐ](http://hogepiyo-game.blogspot.jp/2013/10/skyrim-eromod.html?zx=31582c3aa4555285)
---[Skyrim SexLab プラグイン解説](http://hogepiyo-game.blogspot.jp/p/skyrim-sexlab.html)
-[[SexiS - Sex in Skyrim [Alpha] [Inactive] :http://www.loverslab.com/topic/15205-sexis-sex-in-skyrim-alpha-inactive/]]:統合的なシリーズ
---SexiS Core:基本MOD
---SexiS Cupid:弓矢で撃った2体にSexをさせる。
---SexiS Defeated:敗北時にレイプされる
-[Skyrim SexLab - Sex Animation Framework](http://www.loverslab.com/files/file/150-skyrim-sexlab-sex-animation-framework-v162-updated-jun-3rd-2016/)
--[Skyrim SexLab プラグイン解説 ](http://hogepiyo-game.blogspot.jp/p/skyrim-sexlab.html?zx=c0b231436e2ba5c1)
--[SexLab Index](http://www.loverslab.com/topic/19588-sexlab-index/)
---[Dangerous Nights](http://www.loverslab.com/files/file/500-sexlab-dangerous-nights-2/):野外で寝ると近くのNPCにレイプされるMOD。
---[SexLab Books of Love](http://www.loverslab.com/topic/17557-wip-sexlab-books-of-love/):Cupid Arrow系。強制的にレイプしたりさせたりする魔法を追加する。
---[SexLab Horny Followers](http://www.loverslab.com/files/file/189-sexlab-horny-followers/):Your followers are sick of you always throwing all the heaviest loot over in their bags and now they demand to use you in a slightly different manner...
--[SexLab Tools v3.0](http://www.loverslab.com/files/file/2018-sexlab-tools-v30/):SexLab Tools is a simple mod that aim to give the player some tools to control a sexlab sex scene, mainly the pose & tags, using menus from the UIExtension mod.

###sexlab plugin 
-[SexLab Defeat](http://www.loverslab.com/files/file/286-sexlab-defeat/):攻撃を受けて体力が指定したパーセンテージより下がると、対象にレイプされる。
--[TESLab SexLab Defeat](http://seesaawiki.jp/teslab/d/SexLab%20Defeat)
|割当キー|説明|補足|
|アクションキー（デフォルトG）||Defeat用のアクションキー、状況によって色々な行動を開始させる事が可能になる。|
||戦闘時遠距離|山賊などがしてくる相手を威嚇するモーションを行う。|
||武器構え時近距離|カーソルを合わせた対象にスタミナを消費して組み付く動作が発動する。判定に成功すれば相手に膝を着かせる事ができる。武器を構えていれば街中でも発動する。座っている相手や鍛冶等の作業モーションに入っている相手には発動しない点に注意。|
||膝を着いた相手|カーソルを合わせた相手を対象とした選択肢が発生し、レイプや所持品を奪う等の行動が可能。武器を構えている場合は殺害する選択肢しか出ない点に注意。|
||死体|通常の調べるの他にネクロフィリア（死姦）を行うかどうかの選択肢が発生する。|
||SEX中のNPC|武器収納時には喧嘩の観戦中にNPCが行うような囃し立てるモーションを再生する。武器を構えている場合はカーソルを合わせたNPCが行っているSEXを中断させる。|
||眠っている相手|レイプや盗みを行うかどうかの選択肢が表示される。武器を構えている場合は相手を殺害するかどうかの選択肢が表示される。|
|Shiftキー+アクションキー（デフォルトG）|SEX中のNPC|選択肢が発生し、カーソルを合わせた対象が行っているSEXのモーションを変更したりステージの進行を変更する事ができる。|
|コンパニオンアクションキー（デフォルトH）||フォロワーに組み付きやレイプ等の行動を行わせたい時に使用する。|
||フォロワー|カーソルを合わせているフォロワーを命令の対象にする。|
||NPC|上記の操作で対象にしたフォロワーに対して、カーソルを合わせたNPCに組み付くよう命令を出す。組み付いた時プレイヤーと同様の判定を行い、成功した場合はNPCが膝を着いた状態に移行する。プレイヤーの時と同様に武器を構えていないと組み付きが発動しない点に注意。|
||膝を付いたNPC時|フォロワーにレイプ等を行わせる選択肢が表示される。フォロワーとNPC、プレイヤーでの3Pを行う選択肢も追加される。プレイヤー時と同様に武器を構えている場合は殺害する選択肢、武器を構えていない時はレイプや盗みの選択肢になる点に注意。膝を付かせるのはプレイヤーでもフォロワーでもどちらでもよい。|
|アクティベートキー（デフォルトE）|SEX中のNPC|武器を収めた状態で押すと選択肢が発生。|

-[Sexlab Aroused Redux](http://www.loverslab.com/files/file/1421-sexlab-aroused-redux-december-05-2016/):人間タイプに性欲パラメータを追加する。
--[SexLab Aroused Animations](http://www.loverslab.com/files/file/603-testwip-sexlab-aroused-animations-v2014-01-09/):性欲が溜まったNPCの仕草が変化します。
-[Zaz Animation Pack](http://www.loverslab.com/files/file/156-zaz-animation-pack-v70-2017-05-16/):各種アニメーションのパック。導入後はZaz Animation PackのMCMからSexLabを開き、SexLab AnimationsのREGISTERをクリックして、SexLab側に認識させておく必要がある。
|コンソール|説明|
|coc zbftestzone|奴隷系の道具が揃っている専用施設に移動できる|
|player.placeatme XX010001|専用施設にある宝箱を入手できる|

--[Zaz DoggyStyle Animation Fix (Zaz Animation Pack V7.0 and V.8.0) 1.0.0](https://www.loverslab.com/files/file/4829-zaz-doggystyle-animation-fix-zaz-animation-pack-v70-and-v80/):This is a patch that fixes zaz doggy style Animations.It was a typo.

-[SexLab Romance](http://www.loverslab.com/files/file/158-sexlab-romance-including-source-updated-19th-aug-2014/):NPCとの会話から行為に持ち込めます。
-[SexLab Lover's Comfort](http://www.loverslab.com/files/file/160-wip-sexlab-lovers-comfort-2013-12-30/):夫婦や近親者がSEXするようになります。
--[Further Lover's Comfort](http://www.loverslab.com/files/file/1788-wip-further-lovers-comfort-2016-12-04/):配偶者(結婚相手)や恋人候補と懇ろな行為を作る Mod。フォロワーを誘うことが出来ます。
-[SexLab RapeSpell](http://skup.dip.jp/?andor=and&sword=sexlab+rapespell&mode=ret):NPCとSEX対決　自分でNPCに魔法をかけて即座に襲わせるか、また魔法なしでも設定した確率で襲われます。
-[SexLab MatchMaker](http://www.loverslab.com/files/file/163-sexlab-matchmaker-updated-09172014/):NPC、PCともにエロ行為をする幻惑魔法を追加。複数人数可能。
-[SexLab Dangerous Nights](http://www.loverslab.com/files/file/500-sexlab-dangerous-nights-2/):ロケーションによるレイプの可能性を追加。
-[Devious Devices - Integration](http://seesaawiki.jp/teslab/d/SexLab%20Framework%20Add%2dOn#Devious_Devices):エログッズや、それを使ったモーションの拡張。また、クエストも追加されます。
--[Devious Devices - Assets](http://www.loverslab.com/files/file/269-devious-devices-assets/):This is a collection of BDSM-themed gear and devices for CBBE-HDT (Bodyslide) and UUNP female bodies.
-[Spouses Enhanced](http://seesaawiki.jp/teslab/d/SexLab%20Framework%20Add-On#se):会話から嫁を誘える。他のアドオンと違い、断られることはほぼ無い。
--[Shared Serana Dialogue - Modder's Resource 1.1](http://www.loverslab.com/files/file/704-shared-serana-dialogue-modders-resource/):Shared Serana Dialogue is a modder's resource that allows you to easily use Serana's default voice files in your own mod, for a more natural experience.
-[More Nasty Critters](http://seesaawiki.jp/teslab/d/CreatureBodyMod):統合したクリチャーヌード＋新規クリチャーアニメーションMOD。
-[Hentai Creatures](http://seesaawiki.jp/teslab/d/SexLab%20Framework%20Add-On#Hentai_Creatures):エロクリーチャーを召還する魔法を追加します。様々なクリーチャーを呼び出してフォロワー代わりに連れて歩けます。魔法書はリバーウッドトレーダーで購入できます。
-[I'll Take The Display Model](http://tdyk542.blog.fc2.com/blog-entry-418.html):NPCを奴隷オブジェクトとして自宅などに飾れるMOD 。
-[Devious Devices - Captured Dreams Shop](http://www.loverslab.com/files/file/492-devious-devices-captured-dreams-shop-v415-updated-6-11-2017/):Devious Devicesを拡張するアドオンです。Devious DevicesとZAZ Animation Packの装備を売買できる店が追加されます。
-[Apropos Classic](http://seesaawiki.jp/teslab/d/LoversLab%20Mod%20%B4%CA%B0%D7%A5%EA%A5%B9%A5%C8):セックス(エロ)シーンを文字で官能的に表現。またセックスすると性器にダメージが付いてデバフとなる。Slavetatsと連動して身体に暴行の痕がつく。
-[Puppet Master](https://www.loverslab.com/files/file/463-puppet-master/):NPCに操り人形の呪文を掛けて、好きなことをさせられるMOD。
--[Sexlab Puppet Master 1.7 日本語化](http://skup.dip.jp/up/up13957.7z)
-[SexLab Yet Another Combat Rape](http://skup.dip.jp/up/up14037.zip)
--[[SKYRIM エロMOD晒しスレ 89 [無断転載禁止]©bbspink.com:http://mercury.bbspink.com/test/read.cgi/pinkcafe/1514033560/]]
 更新は上書き後、コンソールから stopquest sslyacr → startquest sslyacr 
-[Immersive Gender Change v1.10](https://www.loverslab.com/files/file/1582-immersive-gender-change/):女キャラにSexlabの性別は男にできる。
-[Sexy Bandit Captives (mod to Sex Slaves for Vanilla Bandit Camps) Beta 0.941](https://www.loverslab.com/files/file/4423-sexy-bandit-captives-mod-to-sex-slaves-for-vanilla-bandit-camps/):山賊共のキャンプに性奴隷追加

###sexlab animations 
-[SexLab Animation Loader 1.5](http://www.loverslab.com/files/file/2488-sexlab-animation-loader/):This mod makes it easy to register new animations in SexLab.
-[SLAL - Animations By Leito](http://www.loverslab.com/files/file/2615-slal-animations-by-leito-91216/):It contains all the animations that are found in Non-Sexlab Animations Pack and Forerunner's Leito pack and shares the same tags and names.
-[Katzumis SLAL Pack fur AnubiSs2167 Animation holded 3a](http://www.loverslab.com/files/file/2852-katzumis-slal-pack-fur-anubiss2167-animation-holded/):This is an Pack for AnubiSs2167 Animations so you can use them with Sexlab Animation Loader.
-[FunnyBizness (v25) SLAL Pack by Shashankie v12.0](http://www.loverslab.com/files/download/2702-funnybizness-v25-slal-pack-by-shashankie/):This is the SLAL pack for FunnyBizness's Animations updated to v25.1
-[RohZima Animation's SLAL Pack003c](https://www.loverslab.com/files/file/5224-rohzima-animations-slal/):This mod contains animations depicting non consensual sex acts. 
-[ZaZ Animation Pack - Tara's Edition V.8.0 plus](https://www.loverslab.com/files/file/5211-zaz-animation-pack-v80-plus/):ZaZ And XaZ
-[Anub's animation dump (REBORN) Updated 27.05.2018](https://www.loverslab.com/topic/53457-anubs-animation-dump-reborn-updated-27052018/)

###SexAddicts 
-[SexAddicts](http://www.loverslab.com/files/file/224-sexaddicts/):

###その他 
-[LDW's Crimson Closet for UNP Slim, UNP, UNP?, and UNPB 14](http://www.loverslab.com/files/file/229-ldws-crimson-closet-for-unp-slim-unp-unp-and-unpb/)
---Simple Chain-Mail Top Add-On for UNP-Slim, UNP and UNPB
---Arcane Knickers Ver. 1.3 for UNP-Slim,UNP and UNPB
---Arcane Heat for UNP-Slim, UNP and UNPB
---Winter Sweaters for UNP-Slim
---White and Black sweater Update for Winter Sweaters
---Vampirella for UNP Slim and UNP And Now UNPB

-[SexAddicts](http://www.loverslab.com/files/file/224-sexaddicts/):This is a sex mod that is mainly about combat rape scenarios and has a random rape (or sex) function as well. It was developed prior to the SexLab sex framework so it's effectively the all-in-one sex mod that the SexLab framework and it's supporting mods replaces.
 B = Cancel current sex act involving the player
 G = Reverse positions between the player and the NPC
 H = Move to the next phase of the sex act
 Shift H = Move to the previous phase of the sex act (Cannot reverse once the last phase has started though)
 X = Move the player closer to the NPC
 Shift X = Move the player further from the NPC
 Y = Switch to the next sex animation
 Z = Move the player up (vertically) vs. the NPC
 Shift Z = Move the player down vs. the NPC

-[Blush When Aroused 1.3](http://www.loverslab.com/files/file/1724-blush-when-aroused/):性欲が高まる、裸になった時に顔が赤面する。Ver1.3で表情機能が追加。
-[Sexy Bandit Captives (mod to Sex Slaves for Vanilla Bandit Camps) ](http://seesaawiki.jp/teslab/d/LoversLab%20Mod%20%B4%CA%B0%D7%A5%EA%A5%B9%A5%C8):山賊共のキャンプに性奴隷追加
-[SlaveTats](https://www.loverslab.com/files/file/619-slavetats/):涙、傷、吸血痕、汗などの表現をレベル毎にMCMから設定出来ます。
--[Quick Menus Adult Plugin 日本語マニュアル](http://mod-quickmenus-02.blogspot.jp/p/rape-004.html?zx=c05f79f9b43b4bf1)
-[Amputator Framework](http://seesaawiki.jp/teslab/d/LoversLab%20Mod%20%B4%CA%B0%D7%A5%EA%A5%B9%A5%C8):手足切断欠損表現MOD。リョナ系 PCとNPC両方有効。独自のモーションや義手義足アイテムなどあり。
-[Sexist/Derogatory Guards, NPCs and Player Comments](http://seesaawiki.jp/teslab/d/LoversLab%20Mod%20%B4%CA%B0%D7%A5%EA%A5%B9%A5%C8):ドヴァ娘がセクハラ発言されるmod。最大の特徴は、ドヴァ娘がしゃべること。山賊になんかされないか心配したり、ヤラレてる最中にヨガったり、薄着でプレイさせてるあなたに文句を言ったりします。

##[Sky TM](http://mitakusaner.blog.fc2.com/) 

###導入済み 
--[Rob’s tumblr gifts](http://mitakusaner.blog.fc2.com/blog-entry-1415.html)
--[Kasumi School Sweater Skyrim](http://mitakusaner.blog.fc2.com/blog-entry-1405.html)
--[Hentai LiLi](http://mitakusaner.blog.fc2.com/blog-entry-1310.html)
--[Vampirella](http://mitakusaner.blog.fc2.com/blog-entry-596.html)
--[Black Vinyl Strap](http://mitakusaner.blog.fc2.com/blog-entry-1316.html)
--[Witch Armor II](http://mitakusaner.blog.fc2.com/blog-entry-1445.html#more)
--[Sexy Mix](http://mitakusaner.blog.fc2.com/blog-entry-1477.html):サムネイルなし
--[SPB Heart Girl](http://mitakusaner.blog.fc2.com/blog-entry-1026.html)
--[Conversion Pack for Bisquits' Oblivion Outfits](http://mitakusaner.blog.fc2.com/blog-entry-1105.html):Oblivionからの移植MODです。Pain BringerとPriestess of Mara(POM)の2種類入ってます。
--[Crazy Belle III Outfit](http://mitakusaner.blog.fc2.com//blog-entry-1786.html):水着装備が4色入ってます。
--[Aradia Leather Outfit](http://mitakusaner.blog.fc2.com/blog-entry-1219.html)『Aradia Leather Armor Skimpy』のリテクスチャ＆一部改変バージョンです。TBBP対応。
--[MMT-ShirtSet + MMJSB](http://mitakusaner.blog.fc2.com/blog-entry-424.html):CBBE / 7Base 対応MODです。Tシャツ装備は胸の大きさの違いで2種類+各4色あります。
--[B&S qhc (qing hua ci)](http://mitakusaner.blog.fc2.com/blog-entry-1757.html):UN7B 対応MODです。『Blade&Soul』に登場する衣装MOD。胴体装備のみ。
--[YoungTrap - CBBE BBP / UNPB BBP](http://mitakusaner.blog.fc2.com/blog-entry-227.html):制服MODスカートが短いので後ろから見るとパンツ丸見え。
---[YoungTrap - 7BCH -](http://mitakusaner.blog.fc2.com/blog-entry-718.html):YoungTrap - UNPB BBP の 7BCHバージョン。ストッキングは Elewin Pumps 2 - High Heels and Stockings for UNP のハイヒールに合わせているので必須。
--[Maid To Order](http://mitakusaner.blog.fc2.com/blog-entry-774.html):かなり細かくパーツが分かれてます。全てのパーツがアクセサリ的な扱い。UNP/7Base体型。
--[Apron](http://mitakusaner.blog.fc2.com/blog-entry-1291.html):スケスケのエプロン装備MODです。胴体装備のみ2種類。
--[BDO Ranger NewCloth](http://mitakusaner.blog.fc2.com/blog-entry-1965.html):UNPB。MMORPG『黒い砂漠』に登場する衣装MOD。ノーマルと「broken」2種類の装備が入ってます。
--[LDW Goth Maid](http://mitakusaner.blog.fc2.com/blog-entry-934.html):メイド装備です。DemonFetは3色。CBBEは5色入ってます。
--[LovelyCloth](http://mitakusaner.blog.fc2.com/blog-entry-1912.html):UN7B / UUNP 対応、HDT仕様。首のパーツと耳が独立した装備になってます。デフォの体型はUN7Bかそれに近いオリジナル体型と思われます。
--[Tama Cosplay](http://mitakusaner.blog.fc2.com/blog-entry-1847.html):
『ハンドシェイカー』に登場する「阿波座こだま」の衣装MODです。細かくパーツが分かれてます。UUNP。

###テスト中 
--[Cops Lady Uniform 2](http://mitakusaner.blog.fc2.com/blog-entry-959.html):『DEAD OR ALIVE 5』に登場する衣装MOD。
--[Maxwell Outfit](http://mitakusaner.blog.fc2.com/blog-entry-565.html):スカート・パンツは個別装備になってます。
--[Les Sucettes Outfit](http://mitakusaner.blog.fc2.com/blog-entry-1881.html):UNP 対応MODです。3色入り。スカートとパンツは個別装備になってます。
--[Kalilies TUMBLR GIFTS FOR SKYRIM](http://mitakusaner.blog.fc2.com/blog-entry-1820.html):UNP 対応MODです。胴体装備が4種類。アクセサリ2種類。髪も追加されます。
--[GalonealDress](http://mitakusaner.blog.fc2.com/blog-entry-1753.html):UNP 対応MODです。胴体・腕装備は4色。ブーツは2色入ってます。
--[Vindictus Mix Robes](http://mitakusaner.blog.fc2.com/blog-entry-574.html):Inner と Robes の2種類入ってます。
--[Blade and Soul chenshan](http://mitakusaner.blog.fc2.com/blog-entry-1485.html):『Blade&Soul』に登場する衣装MOD。UUNPはブラ・パンティ有り、ブラ無し、シャツのみ、パンティのみの4種類あります。
--[Gothic Lynn](http://mitakusaner.blog.fc2.com/blog-entry-1934.html):Gothic & Lolitaな衣装MOD。スカートが個別装備。UNP対応。
--[Lady Blood (LB Blood Mage)](http://mitakusaner.blog.fc2.com/blog-entry-127.html):CHSBHC / CBBE BodySlideはブーツが2種類。ジャケットも袖ありと袖なしの2種類。パンツが9種類。UNPB / UUNPはespが違うので、ジャケットやスカート・パンツが個別装備になってません。
--[Sassee Lass](http://mitakusaner.blog.fc2.com/blog-entry-1980.html):胴体装備のみ入ってます。BodySlideはCBBEとUUNP両方入ってます。
--[Sweet Dress](http://mitakusaner.blog.fc2.com/blog-entry-435.html):スケスケのドレス装備です。
---[Sweet Dress UUNP HDT](http://wtfuun.tumblr.com/post/156491120135/sweet-dress-uunp-hdt-main-mod-required-checkout):Main Mod Required. Checkout Retextures. 
--[Bondage Straps](http://mitakusaner.blog.fc2.com/blog-entry-86.html):4種類の胴体装備が入ってます。
--[Beachwear Collection 2017](http://mitakusaner.blog.fc2.com/blog-entry-2087.html):セクシーな水着装備MOD。胴体装備が4種類あります。それぞれ5色入り。アクセサリ類も複数色入ってます。
--[Swimwear for 7BCH](http://mitakusaner.blog.fc2.com/blog-entry-1880.html):かなり露出多めの水着装備です。
--[SexyDress](http://mitakusaner.blog.fc2.com/blog-entry-1598.html):セクシーなドレス衣装MOD。7色あります。
--[Full Metal Bikini](http://mitakusaner.blog.fc2.com/blog-entry-687.html):UNPはUNPC体型と思われます。
--[WUYI](http://mitakusaner.blog.fc2.com/blog-entry-2148.html):セクシーな衣装MOD。胴体装備のみ。色が変わるエフェクト付きです。
--[Naughty Nights](http://mitakusaner.blog.fc2.com/blog-entry-1382.html):上も下も丸出しな下着MOD。トップレス・ボトムレスバージョンも入ってます。全9種類。
--[Mini Apron](http://mitakusaner.blog.fc2.com/blog-entry-1549.html):セクシーなエプロン装備MOD。10色(種類)あります。
--[Tropical pack](http://mitakusaner.blog.fc2.com/blog-entry-719.html):種類豊富な水着MODです。UUNPのBodySlideは一部のみ対応してます。
--[Lethal Majesty](http://mitakusaner.blog.fc2.com/blog-entry-448.html):
Oblivionからの移植MOD。BodySlideはUNPCMがベースです。7Baseは作者が違うため、装備内容が一部異なります。
--[DEM clothes Collection](http://mitakusaner.blog.fc2.com/blog-entry-1469.html):ハイクオリティな装備が4種類入ってます。CBBE / CBBE BodySlide 対応。
--[BDO Dark Knight Puff Mini](http://mitakusaner.blog.fc2.com/blog-entry-2168.html):MMORPG『黒い砂漠』に登場する衣装MOD。下着系の装備も豊富です。
--[Amazon Outfit](http://mitakusaner.blog.fc2.com/blog-entry-2158.html):胴体装備は胸や脚のパーツの有無で3種類あります。それぞれ2～4色入ってます。UNPBはHDT、CBBE BodySlideはNIOverride highheels対応。
--[Pure Elegance](http://mitakusaner.blog.fc2.com/blog-entry-1006.html):4色の装備MODです。ベースのCBBEは全身一体型。手の周りにエフェクトがあります。BodySlideは胴体装備が2種類あり、細かくパーツが分かれてます。帽子、武器も4色あります。
--[KillerIsDead Betty](http://mitakusaner.blog.fc2.com/blog-entry-2193.html):UUNP対応MOD。
--[Delphin Outfits DOA LeiFang Coustume](http://mitakusaner.blog.fc2.com/blog-entry-2201.html):『DEAD OR ALIVE5 Last Round』に登場する衣装MOD。スカート無しやメガネもあります。
--[Pink Butterfly Pink / Dark version](http://mitakusaner.blog.fc2.com/blog-entry-469.html):CHSBHC / CBBE BodySlide / 7Base 対応MODの紹介です。2色あります。
--[Nezzar's Ultimate Lingerie Collection](http://mitakusaner.blog.fc2.com/blog-entry-2296.html):大量の下着装備が入ってます。
--[QT Nightwear](http://mitakusaner.blog.fc2.com/blog-entry-2315.html):UUNP 対応MODの紹介です。3色入りです。それぞれに透過処理有り・無しが用意されてます。
--[DF_T5](http://mitakusaner.blog.fc2.com/blog-entry-2335.html):CBBE 対応。
--[DV Intimate V1](http://mitakusaner.blog.fc2.com/blog-entry-2332.html):CBBE BodySlide 対応MOD。水着系が7色。下着系が2色入ってます。
--[DOA5 Wedding](http://mitakusaner.blog.fc2.com/blog-entry-2350.html):『DEAD OR ALIVE 5』に登場する衣装MODです。UUNP。
--[Ryuko Matoi School costume from Kill la Kill](http://mitakusaner.blog.fc2.com/blog-entry-2397.html):『キルラキル KILL la KILL』に登場する衣装MODです。UNPB。
--[Mabinogi 2016 Summer](http://mitakusaner.blog.fc2.com/blog-entry-1945.html):『マビノギ英雄伝』に登場する衣装MODです。UNPB/CBBE。
--[Wedding Dress-3](http://mitakusaner.blog.fc2.com/blog-entry-2541.html),[Nini wedding dress(Google Drive)](https://drive.google.com/drive/folders/1y44HyRjsq8wyuWUQfe7zpY4HQ5EQFNBp)

###ペンディング中 
--[Ibuki Schoolgirl outfit](http://mitakusaner.blog.fc2.com/blog-entry-1410.html)
--[Ebon Shroud Mashup](http://mitakusaner.blog.fc2.com/blog-entry-930.html)
--[BridalSet](http://mitakusaner.blog.fc2.com/blog-entry-1191.html)
--[Aradia Kato](http://mitakusaner.blog.fc2.com/blog-entry-595.html)
--[Naughty Red Riding Hood Clothes](http://mitakusaner.blog.fc2.com/blog-entry-1352.html#more)
--[Ling - Wedding Dress](http://mitakusaner.blog.fc2.com/blog-entry-1190.html)
--[Games Conversion](http://mitakusaner.blog.fc2.com/blog-entry-1783.html)

###アンインストール 
--[Blade and Soul chenshan](http://mitakusaner.blog.fc2.com/blog-entry-1485.html):CTD
--[Blade and Soul Maoyi](http://mitakusaner.blog.fc2.com/blog-entry-1490.html):CTD
--[Backsteppo’s PE Dress](http://mitakusaner.blog.fc2.com/blog-entry-1475.html):CTD
--[Red Roses](http://mitakusaner.blog.fc2.com/blog-entry-1377.html):ダウンロードできず
--[N8k Little Carmine Dress](http://mitakusaner.blog.fc2.com/blog-entry-1476.html):サムネイルなし
--[Dark Rose 2](http://mitakusaner.blog.fc2.com/blog-entry-1274.html):サムネイルなし
--[UNPB130](http://mitakusaner.blog.fc2.com/blog-entry-2000.html):baiduダウンローダーが必要。
--[LB Clothing](http://mitakusaner.blog.fc2.com/blog-entry-1552.html):透明になる不具合

##[killingdoll](http://killingdoll.com/) 

###導入済み 
--[NieR](Automata by Dint999:http://killingdoll.com/?p=20596):NieR:Automataのヨルハ二号B型の衣装MOD。CBBE、CBBE Bodyslide、UNP体系用（要ファイル解凍）スカート部分に物理演算が組み込まれているので、みんなの大好きな尻モロ、パンチラが見放題だ。HDTヘアー2種と刀もセットになってるぜ。

###テスト中 
--[Fresh Women Darkness](http://killingdoll.com/?p=22756):ダンジョンなどにセクシーな女型モンスターを追加するMOD。現在はドワーフ、ファルメル、ドラウグル系の敵が数タイプづつ配置されます。
--[Rhian Mashup](http://killingdoll.com/?p=24539):MMORPGのAsker onlineというゲームに登場する装備MOD。
--[Azera Sorceress armor](http://killingdoll.com/?p=24588):MMORPG「AZERA」に登場する装備MOD。UNPB体型用。

###インストール予定 
--[Full HDT Maid Outfit with Cleavage](http://killingdoll.com/?p=16457):胸揺れ+スカートひらひらのメイド衣装MOD。視線を感じる…
--[Backsteppo’s French Maid for UNPCM](http://killingdoll.com/?p=15347):Backsteppoさんのフレンチメイドの衣装MOD
--[Amazing Caves – Adult](http://killingdoll.com/?p=18496):酒池肉林な我が家を追加するMOD。入口横にある切り替えスイッチを押すと、スカイリムに登場する男性・女性フォロワーや主要NPCを出現させる事ができます。リバーウッドのすぐ傍です。
--[BnS Uniform Set](http://killingdoll.com/?p=19691):ヨツオさん作の女子高生の制服MOD。
--[Midnight Light Armor for UNP and UUNP (Mashup)](http://killingdoll.com/?p=20969):ロアフレンドリーかつミニ丈な装備MOD。UNP、UUNP体型用。
--[Aether Suite 3.1.0 – Heartbeat, Heartbreak](http://killingdoll.com/?p=12672):SS撮影用のロケーションを追加するMOD。学校、ホテル、近未来風の街、和風旅館・露天風呂、絶妙な光源が配置された撮影スタジオなどなど、一つのMODで多数の部屋や建物が導入されます。
---[Aether Suite Teleport Menu](http://killingdoll.com/?p=20981):Aether Suiteにある各ロケーションへテレポートが可能になるMOD。
--[The Grand Bathhouse](http://killingdoll.com/?p=20030):ウィンドヘルムの南東に、マイホーム兼ゴージャスなバスハウスを新設するMOD。
--[Angel](http://killingdoll.com/?p=26590):スケスケの天使の装備MOD。UNP体型用。

##[Nini](https://www.patreon.com/ninirim/posts?tag=published%20mod) 
--[Bless HV 0102](http://mitakusaner.blog.fc2.com/blog-entry-2241.html):CBBE BodySlide / UUNP 対応MODの紹介です。DLしたファイルには大量の装備が入ってます。
--[Nini Stuff 1.1](http://ninirimpiracy.blog.fc2.com/page-2.html)
--[Nini Stuff 2](http://ninirimpiracy.blog.fc2.com/page-0.html)
--[Nini COS Bodyslide UPDATE 170729](http://ninirimpiracy.blog.fc2.com/page-2.html):Breast and leg shape changed and fix the seam of pussy.
--[Nini Hair Pack](http://ninirimpiracy.blog.fc2.com/page-4.html)
--[Nini Skin](https://www.loverslab.com/topic/76711-trying-to-get-the-ninirim-look/?page=3)
--[Nini Follower UNP HDT 1.0.0](https://www.loverslab.com/files/file/5231-nini-follower-unp-hdt/): This mod add a new cute follower to your game. Location: Silver-Blood Inn (Markarth) 
--[9204 MBO 0022M(圣绣白凤) by Team TAL](https://www.patreon.com/posts/9204-mbo-0022m-19952136)
--[[[NINI X TAL] MBO 0048 (挂月松石):https://www.patreon.com/ninirim]]
--[9204 Bless MS0101 by Team TAL](https://www.patreon.com/posts/9204-bless-by-19385995)

##その他サイト 
###[[みちのくオブリビオン [OBLIVION]:http://mitinokuoblivion.blog118.fc2.com/]] 
-[Cute Frills](http://mitinokuoblivion.blog118.fc2.com/blog-entry-1689.html):普段着のような防具MOD。タートルネック＋ノースリーブ＆フリルスカートの組み合わせ。
-[Sexy Elves 7B](http://mitinokuoblivion.blog118.fc2.com/blog-entry-1730.html):エルフの下着っぽい感じの衣装MOD。高貴なお生まれのエルフに相応しいエレガントな見た目の下着。上下ともに布の面積がかなり小さいです。

###[JackGa Skyrim](http://jacksh123.mysinablog.com/index.php?op=Default&Date=201501) 
-[DOA5 mods/followers list in LoversLab](http://www.loverslab.com/topic/19186-jackgas-stuff/#entry446370)
--[Skyrim MOD 美人館 JackGa Shop for CBBEv3](http://yamatogame.web.fc2.com/02mon0jachshop3.html):スクリーンショット多数。

###[SKYRIM MODTYPE](http://modtype.doorblog.jp/) 
-[DOA followers](http://modtype.doorblog.jp/archives/28430222.html)

###[nsfwmods.com](https://nsfwmods.com) 
-[UNPB Naughty Red Riding Hood Clothes 1.0.0](https://nsfwmods.com/files/file/66-unpb-naughty-red-riding-hood-clothes/):

###[PINK SKY! スカイリムMOD導入日記](http://reachthepinksky.blog.fc2.com/blog-entry-127.html) 
-[スタンダードなプリーツスカートを作ってみました -PS Pleated Skirt-](http://reachthepinksky.blog.fc2.com/blog-entry-127.html)

###[ESkyrim](http://eskrimmods.blogspot.com/) 
-[[Lolita Dress [UNP] :http://eskrimmods.blogspot.com/2017/09/lolita-dress-unp.html]]
-[Modern Clothes](http://eskrimmods.blogspot.com/2017/03/modern-clothes.html)
-[[Bo Dress [UNP] :http://eskrimmods.blogspot.com/2017/02/bo-dress-unp.html]]
-[[Training Cube [CBS/UBS/COS]:http://eskrimmods.blogspot.com/2017/11/training-cube-cbsubscos.html]]
-[[Tecmo Anniversary DLC [CBBE]:http://eskrimmods.blogspot.com/2017/12/tecmo-anniversary-dlc-cbbe.html]]
-[[9204 Nier Automata 2B Pack [HDT Cloth] :https://www.patreon.com/posts/9204-nier-2b-by-19195156]]
-[[Dragons Crown Sorceress Outfit [UNP]:https://eskrimmods.blogspot.com/2017/07/dragons-crown-sorceress-outfit-unp.html]]
--[SMP-PE path](https://www.youtube.com/redirect?redir_token=Y215en39FM8ssNpsiSzws_LRpgp8MTUzNDE2NjkyNkAxNTM0MDgwNTI2&q=https%3A%2F%2Fpan.baidu.com%2Fs%2F1gfnbjGJ&v=u_a9NN8vxqs&event=video_description)
-[[Crystal Rose [UNP/SMP]:https://eskrimmods.blogspot.com/2017/08/crystal-rose-unpsmp.html]]:smp-pe付き
-[[K-Girl Outfits for Skyrim [UNP/UBS] :https://eskrimmods.blogspot.com/2019/02/k-girl-outfits-for-skyrim-unp.html]]

###[TRE-MAGA](https://tre-maga.com/) 
-[Hot Uniforms Maid](https://tre-maga.com/3272)
-[Emfy Cleric Robes](https://tre-maga.com/4078)
-[BridalSet](https://tre-maga.com/4051)
-[Vindictus Mini Dress (SMP)](https://tre-maga.com/4329)
-[Aion Opulent](https://tre-maga.com/4352)

##その他、衣装MOD 
###導入済み 
--[R18Pn 00 - Fiona Armor for UNP](http://skyrim.2game.info/detail.php?id=13082):PS2ゲーム「DEMENTO（デメント）」の主人公、フィオナ・ベリの服を追加します。Fiona Armorとブーツを2色づつ。UNP用、Weight対応。導入後はホワイトラン画像の位置にチェストが追加されます。
--[You Call That Skimpy - UNP](http://skyrim.2game.info/detail.php?id=11951):バニラ装備をSEXYな装備へリプレイスします。UNP用
--[Osare Panty - UNP](http://skyrim.2game.info/detail.php?id=26305):パンティ「Osare Panty」を24種追加します。UNP用。
--[Osare Underwear - UNP](http://skyrim.2game.info/detail.php?id=14294):Osare Underwear。 縞パン20種以上を追加します。UNP用
--[Osare Maid Outfit - UNP](http://skyrim.2game.info/detail.php?id=13569):メイド服、Osare Maid Outfitを追加します。UNP用
--[HDT HighHeels System](http://skyrim.2game.info/detail.php?id=36213):ハイヒールMODなどで地面に足が埋まってしまうのを防ぐMOD。略称「HHS」
---[Summer Dress Sets for UNP by Yurica](http://skyrim.2game.info/detail.php?id=65777):「Summer Dress Sets」を追加します。服・靴・帽子の3セットの他ブレスレットが2種類あり。
---[Mage Dress for UNP by Yurica](http://skyrim.2game.info/detail.php?id=55900):UNP用装備「Yurica Mage Dress」を追加します。
--[HENTAIGALE Armor by Hentai - Nexus Exclusive -](http://skyrim.2game.info/detail.php?id=12491):HENTAIGALE Armorを追加クラフト可能にします。UNP用
--[TWO CASUAL WEARS BY HENTAI - File Fixed -](http://skyrim.2game.info/detail.php?id=12957):CASUAL WEARSを追加します。ビキニとセーターの2種とブーツ。UNP用
--[Gwendolic Armor - UNP](http://skyrim.2game.info/detail.php?id=12334):Gwendolic Armorを追加します。王冠やパンティも有り、UNP用。
--[TTLL Ship – Beta v0.1](http://gzlife.sakura.ne.jp/ntnk-sky/?page_id=640):交易船TTLL Shipエリアが追加されます。リバーウッド外れに船に通じる入口が追加されます。
--[MaMa Armor](http://modtype.doorblog.jp/archives/37443655.html#more):ソウルキャリバーの装備MOD。
--[Aradia Devious](http://modtype.doorblog.jp/archives/44670601.html#more):貞操帯。
--[Kitty Corset - Bombshell BBP](http://mitinokuoblivion.blog118.fc2.com/blog-entry-1479.html):コルセットとパンツの組み合わせなシンプルなコルセットMOD
--[Edhildils Dwemer Cyborg BBP](http://skyrim.2game.info/detail.php?id=43891):手足が「ドワーフ・スフィア」の様になるアーマー。
--[Nirwana Armor Bandage](http://skyrim.2game.info/detail.php?id=59923):るろうに剣心の佐之助の衣装からインスパイアしたらしいです。
--[Refracting Stalhrim CBBE UNP 7Base with optional transparency](http://skyrim.2game.info/detail.php?id=53067):透明職人skysan4298さんによるスタルリム装備のメッシュ、テクスチャなどの変更によって透明感のある雰囲気に変更CBBE、UNPやDual Sheath Reduxなど対応。
--[BDO Ranger Sitaila UUNP HDT](http://wtfuun.tumblr.com/post/159040901960/bdo-ranger-sitaila-uunp-hdt-main-mod-required-by)
--[BnS Renzuneiyi Dress UUNP HDT](http://wtfuun.tumblr.com/post/153861968285/bns-renzuneiyi-dress-uunp-hdt-install-the)

###テスト中 
--[Ashara Imperial Outfit - UNP - 7B - Sundracon](http://skyrim.2game.info/detail.php?id=51682):冠、腕輪、サンダル、ドレスとパーツが別れています。革なめしの棚で制作可能。サンダルが「その他」、それ以外は「インペリアル」のカテゴリです。
--[ARMO no.5： Loli Airy Dress](http://blog.livedoor.jp/crystaluna/archives/1004838818.html):フラットな装備がいっぱい詰まったアーマーパッケLolilabsから。
--[BaekMuSae UNPB-TBBP](http://skyrimfollower.blog.fc2.com/blog-entry-21.html):黒い砂漠に登場する衣装(白ワンピ)を追加します。
--[例のニットセーター for UNPCM](http://helloworld-tes.com/2017/02/25/post-1381/):ツイッターで童貞を殺す服として話題となったこのニットセーター。
--[Kalilies’ Tumblr Gifts](http://mitinokuoblivion.blog118.fc2.com/blog-entry-1756.html):フリル付きのゴスロリチックなドレス。正面のスカートの丈が短く下半身がもろに見えるありがたいタイプ。
--[Srongs](http://mearalikesmead.tumblr.com/post/147584552199/so-i-finally-got-off-my-ass-standalone-sarongs-8):Standalone sarongs, 8 color variants, UNP/UNPB compatible. All retextured from Newmillers Pareo outfit.
---[Mearalikesmeads Sarongs – TMB](http://robton.nu/mearalikesmeads-sarongs-tmb/)
--[Northgirl Armor UNP and the Retexture from clethcleth and Gamwich](http://skyrim.2game.info/detail.php?id=38053):ニット素材の軽装「Northgirl light armor」を追加します。UNP用。
--[Tes4Mod for skyrim](http://skyrim.2game.info/detail.php?id=59867):TES4 Oblivion装備MODを数種類CBBE体系向けに移植した装備MODです。
--[Dadag4-5](http://minerva-net.sumomo.ne.jp/html/mod0293.html):多数の妖精やドレス、現代風の衣装を追加してくれるMod。CBBE体型用です。
--[Leather Armor for UNPB-TBBP](http://skyrim.2game.info/detail.php?id=76445):重装扱いのレザーアーマーを追加します。
---[Leather Armor for UNPB-TBBP Recolor](http://skyrim.2game.info/detail.php?id=79997):Leather Armor for UNPB-TBBP by gekkou1992の、リカラーテクスチャ。
--[BnS Maoyi Outfit UUNP HDT](http://wtfuun.tumblr.com/post/152466058380/bns-maoyi-outfit-uunp-hdt-main-required-here)
--[Memeru Outfit - UNP](http://skyrim.2game.info/detail.php?id=18802):メルルのアトリエで登場する軽装「Memeru Outfit」を追加します。UNP用。クラウン赤と黒、ドロワーズ、スカート、上着など各パーツ別れており黄色と黒の2色有り。
--[Honey’s Ugly Grandma Sweaters](http://architeuthisinfitialis.tumblr.com/post/139436762039/honeys-ugly-grandma-sweaters-hugs-for-everyone-3):3 knit tops, 4 colors each! Compatible with UNP
--[RR Octavia Set for UNP](https://skyrim.2game.info/detail.php?id=68150):あるゲームで使用されている武器とアーマー(UNP体型)を追加します。
--[RR Skirmish Armor for UNP](https://skyrim.2game.info/detail.php?id=88980):とあるゲームに登場する鎧っぽいもの一式(重装)を追加します。

###ペンディング中 
--[Ashara Princes of the Woods for UNP and male](http://skyrim.2game.info/detail.php?id=18008):軽装「Ashara Princess of the Woods」を追加します。UNP用、6色有り。
---[DreamBurrows Princess of The Woods Retexture](http://skyrim.2game.info/detail.php?id=23626):Ashara Princessのリカラーテクスチャ。UNP用、オリジナル導入後上書きしてください。
---[Princess of the wood addons and alternative sexy textures](http://skyrim.2game.info/detail.php?id=24310):装備MOD「Princess of the wood」用に盾、ブーツ、スカート、パンティを追加します。UNP用
革のカテゴリでクラフト可能。またOPTINAL FILESでAlternative Sexy Texturesも配布しています。

#便利MOD 
-[Unread Books Glow](http://skyrim.2game.info/detail.php?id=10012):まだ読んでいない本が光るようになります。
-[Blocksteal Redux - Prevents accidentally pick up](http://www.nexusmods.com/skyrim/mods/61605/?):誤爆でアイテムを盗んでしまう事態を阻止してくれます。
-[Floating Healthbars](http://www.nexusmods.com/skyrim/mods/58728/?):戦闘になった時、NPCに体力ゲージが表示されます。
-[Face Light](http://www.nexusmods.com/skyrim/mods/13457/?):キャラの顔にライトを当ててくれる超有名MOD。
-[Haven Bag](http://skyrim.2game.info/detail.php?id=21454):どこでも袋の中(倉庫的な場所)にワープできる「Haven Bag」を追加します。
-[Player Home Map Markers](http://skyrim.2game.info/detail.php?id=2723):プレイヤーの家にファストトラベル出来るようになります。
-[Simple Horse](http://skyrim.2game.info/detail.php?id=78689):機能を呼び出しや非戦闘化に絞った軽量・安定・シンプルな馬拡張modです。
-[AreYouThere - Actor(NPC) Explorer](http://skyrim.2game.info/detail.php?id=76051):有効になっているすべてのMODのActorをリストアップするMODです。Actorを選択してコマンドの対象にできます。
-[No Boring Sleep-Wait Menu](http://skyrim.2game.info/detail.php?id=12625):睡眠/待機メニューの24時間リミットを削除し744時間(31日)まで選択できるようになります。
コンソールから tfc と入力してから実行すると待機時間が高速化されます。

#動作MOD 
-[Bowlegged jump animation Fix](http://skyrim.2game.info/detail.php?id=7416):がに股ジャンプを修正します。
-[Animated Prostitution - Skyrim - WIP](http://skyrim.2game.info/detail.php?id=10748):NPCとのSEXが可能になるMOD。通称「AP」。導入後、結婚相手に話しかけるか、持ち物に追加されるAPディベラのアミュレットを装備してNPCに話しかける。すべてのNPCはゲーム内時間で1時間のクールダウン時間を持つ。
-[My Home is Your Home (MHiYH 2plus)](http://skyrim.2game.info/detail.php?id=62040&no=1):フォロワーそれぞれに家を設定可能にします。
-[XP32 Maximum Skeleton Extended - XPMSE](http://skyrim.2game.info/detail.php?id=68000)
-[HDT Physics Extensions](http://skyrim.2game.info/detail.php?id=53996):物理演算で髪や乳、お尻、服などを計算して揺らすことのできる SKSE Plugin。
-[MARIRO kickarts](http://killingdoll.com/?p=18919):素手の攻撃モーションを挌闘ゲーム風に変更するMOD。かかと落としや飛び蹴りなど、ステゴロは全て華麗な足技に変更されます。
-[Flower Girls for Skyrim 32bit](http://skyrim.2game.info/detail.php?id=81241):主要都市６つに配置した"フラワーガールズ"達や、その他とあれやこれやするMOD。
-[Auto Unequip Ammo](http://skyrim.2game.info/detail.php?id=10753):弓を装備していない場合、自動的に矢の装備も外れます。装備する際は最後に装備していた矢を選択します。
-[aModestSkyrim](http://seesaawiki.jp/teslab/d/LoversLab%20Mod%20%B4%CA%B0%D7%A5%EA%A5%B9%A5%C8#sx_animation):裸の時に局部を隠すようになる。
-[HDT SKIRT (Remake)](http://skyrim.2game.info/detail.php?id=82538):HDTで揺れるスカートを追加します。
--[HDT Test Skirts](http://www.loverslab.com/files/file/508-hdt-test-skirts/):This is the HDT Test Skirts by anano combined in one nice file and renamed so you can have both installed at the same time. Missing textures are added also.
--[Empire Coat](http://www.loverslab.com/files/file/813-empire-coat-a-hdt-test/):The dress is based on Camilla Welton's Empire Coat design.
-[All-in-One HDT Animated Pussy 3.3](http://www.loverslab.com/files/file/2476-all-in-one-hdt-animated-pussy/):This All-in-One mod includes 10 pre-builded Unified UNP Special bodies and 10 pre-builded CBBE bodies with HDT Vagina with XML attached to meshes in order to have collisions with hands, belly, schlongs and some creatures.
--[Slick Silk Body (Preset) v3.0](https://www.loverslab.com/files/file/3424-slick-silk-body-preset/):かなり素敵な乳揺れをするようになります。Slick Silk Body Preset を使う場合は、All in One HDT Animated Pussy をFomodで導入する際に、揺れ方を数種類から選択するんですが、「Option B- Naturalistic Jiggle」を選択した方が良いそうです。
-[Female Animation Pack](http://skyrim.2game.info/detail.php?id=29408):キャラクタのアニメーション（モーション）を女性らしくするMOD。本MODの全てのhkxファイルが\meshes\actors\character\animations\femaleにある状態で本MODをインストールする。

##HDT+SMP(検証中) 
-[HDT Skinned Mesh Physics Tutorial 1.1](https://www.loverslab.com/files/file/1817-hdt-skinned-mesh-physics-tutorial/)
-[A Guide to HDT-SMP Users/Modders](https://forums.nexusmods.com/index.php?/topic/3800385-a-guide-to-hdt-smp-usersmodders/)
-[All-In-One hdtSkinnedMeshPhysics Setup 2.0b (FOMOD)](https://www.loverslab.com/topic/68009-all-in-one-hdtskinnedmeshphysics-setup-20b-fomod/)

##視点 
-[Crawl on fours animation](http://skyrim.2game.info/detail.php?id=33097):隠密(スニーク)モーションを四つん這いで進むように変更します。女性向け。
-[Immersive First Person View](http://skyrim.2game.info/detail.php?id=49036):一人称視点時、下を向いた時に自キャラの体が見えるようになるMOD。
-[Skyrim - Enhanced Camera](http://skyrim.2game.info/detail.php?id=57859):
一人称視点で自分の身体が見えるようになる SKSE のプラグイン。espはありません。
-[Archery Gameplay Overhaul](http://skyrim.2game.info/detail.php?id=69033):弓プレイの拡張＆調整を行うMod。

##FNIS 
-[Fores New Idles in Skyrim - FNIS](http://skyrim.2game.info/detail.php?id=11811):NPCやプレイヤーをアニメーションさせます。略称「FNIS」
 1. data/tools/GenerateFNIS_for_Users/GenerateFNISforUsers.exe 実行(管理者権限)
 2. Update FNIS Behavior 実行

--[a little sexy apparel replacer with LSAR Addon](http://skyrim.2game.info/detail.php?id=5564):バニラ装備をリプレイスします。UNP/CBBE/ADEC/UNPBに対応（UNPBのみBBP対応(version 4.00)）
FOMMインストーラーにより、下着やスカートの有無、軽装か重装のどちらかのみ導入など画像を見ながら選択できます（NMMなどインストーラに対応したMOD管理ツールでの導入推奨）また装備も追加されています。

--[Blow up -a little sexy apparel replacer addon-](http://skyrim.2game.info/detail.php?id=24536):風を巻き越してスカートをめくります。CBBE、UNP版があります。導入後は自動で追加されるシャウト「Blow up」を使用してください。

--[EstrusForSkyrim](http://skyrim.2game.info/detail.php?id=33102):TES4でも人気のあった発情＆触手MOD「Estrus」のSkyrim版

--[Sexy Adventures in Skyrim](http://skyrim.2game.info/detail.php?id=34675):Fores New Idles in Skyrim - FNIS 用の追加モーション。
キス、ハグ、SEXモーションを追加し、C4～C22を変更します。
導入後、FNIS説明ページを参考に必ずGenerateFNISforUsers.exeを実行して下さい。
 C4 = 男性用モーション1 = Missionary
 C5 = 女性用モーション1 = Missionary
 C6 = 男性用モーション2 = キス
 C7 = 女性用モーション2 = キス
 C8 = 男性用モーション3 = BJ
 C9 = 女性用モーション3 = BJ
 C10 = 男性用モーション4 = Cowgirl
 C11 = 女性用モーション4 = Cowgirl
 C12 = 男性用モーション5 = Standing doggy-style
 C13 = 女性用モーション5 = Standing doggy-style
 C14 = 男性用モーション6 = Doggy-style anal
 C15 = 女性用モーション6 = Doggy-style anal
 C16 = 男性用モーション7 = Doggy-style vaginal
 C17 = 女性用モーション7 = Doggy-style vaginal
 C18 = 男性用モーション8 = Flexible position (anal)
 C19 = 女性用モーション8 = Flexible position (anal)
 C20 = 男性用モーション9 = Fisting
 C21 = 女性用モーション9 = Fisting
 C22 = 男女共用モーション10 = Masturbation

--[OSex - Legacy Version 1.06](http://skyrim.2game.info/detail.php?id=77973):シームレスにアダルトモーションを制御する新しいフレームワーク。
--[Animated Prostitution - Skyrim - WIP](http://skyrim.2game.info/detail.php?id=10748):NPCとのSEXが可能になるMOD。通称「AP」

--[Adult Show XXX - ASX](http://skyrim.2game.info/detail.php?id=8714):Adult Show MODです

--[Cupid Arrows - Russian](http://skyrim.2game.info/detail.php?id=38574):自分やNPC同士をエッチさせるキューピッドの矢を追加します。
モーションのバリエーションはいくつか有り、ランダムで行為が行われます。ボイス付き。

-[SexiS導入しますた](http://blog.goo.ne.jp/nyao-nyaa7da4/e/f60761cb0cd50fa7db855a84003738c8)

##POSE 
-[Halo's Mods](http://mod.dysintropi.me/)
--[Halo’s Poser S1.5](http://mod.dysintropi.me/halos-poser-s1-5/)
-[Zaz Resources - Whips Restraints and Bondage](http://skyrim.2game.info/detail.php?id=24023):拷問・束縛・調教モーション＆ポーズを30種追加します。
-[Aloe poser](http://aloe-ygroot.tumblr.com/post/115535676262/aloe-poser-%E5%87%BA%E6%9D%A5%E3%81%9F%E3%82%88)
-[GomaPeroPero](http://gomaperopero.tumblr.com/post/143319652380/gomapero-poses-6)
--[GomaPero Poses v10](http://mod.dysintropi.me/gomapero/)
--[GomaPero Follower v1.5](http://mod.dysintropi.me/gomapero/)
-[Fuwapose](http://fuwasan.tumblr.com/tagged/fuwapose)
-[FNIS Ero Idle Spell 14-02-02](http://www.loverslab.com/files/file/19-fnis-ero-idle-spell/)
-[Poser Hotkeys](http://skyrim.2game.info/detail.php?id=72623):MCMからホットキーを設定し、ポーズを再生するMODです。
-[Poser Hotkeys Plus](http://skyrim.2game.info/detail.php?id=90896):Poser Hotkeysの最終バージョン(v1.06)を拡張してShowPoseMenuのようなリストから直接選定できるポーズメニューを追加します。このPoser Hotkeys Plusを導入するとMCMで設定したポーズメニューキーを押すだけでポーズの一覧が表示されポーズの選択が簡単になります。
-[Kinoko Pose](http://skyrim.2game.info/detail.php?id=58394):バラエティ豊かなポーズや、本などオブジェクト付きのポーズをPCやNPCにとらせることができる指輪とパワーを追加します。
-[BakaFactory's Pose Pack Vol 1.2V](https://www.patreon.com/posts/bakafactorys-vol-14732378)

###ポーズ関連リンク 
-[ポーズMOD画像集](http://rrovin.web.fc2.com/skyrim/ppa/ppindex.html):現在公開されているポーズMODの画像を収めたアルバムです。 ブラウザでの閲覧。
-[ShowPoseMenu](http://sesamin.tumblr.com/showposemenu):複数のMODのポーズを１つのメニューにまとめて表示して、選択できる様にするMod。
-[ポーズmodの導入について](http://mvssf.blog.fc2.com/blog-entry-983.html)
-[ポーズMOD カタログ](http://blog.livedoor.jp/kotaz/archives/28429838.html)
--[Zaz Resouces](http://blog.livedoor.jp/kotaz/archives/31662202.html):拘束系、器具を捨てると浮く(回収出来ない)バグあり。

##DANCE 
-[ポーズMODを使ったポーズ管理サンプル](http://mod-quickmenus-01.blogspot.jp/p/json-006.html)
--[Dance Together](http://www.sopanxia.com/q/KM5QQGXR17X48A5ZAS2G)
--[Shake It - Dance Animations](http://skyrim.2game.info/detail.php?id=14521)
--[Shake It Some More - Dance Animations Addon and Framework](https://www.nexusmods.com/skyrim/mods/74699/?tab=files)

#チートMOD 
-[Golden Rings Of Crafting](http://skyrim.2game.info/detail.php?id=50994):鍛冶/錬金/付呪を強化する指輪を追加します。ファレンガーの机の金庫から入手できます。
-[Crafting Supplies](http://skyrim.2game.info/detail.php?id=37696):関連するアイテム類が入ったチェストを追加します。

#フォロワー 
-[Amazing Follower Tweaks(AFT)](http://skyrim.2game.info/detail.php?id=15524):フォロワー総合MOD。通称「AFT」。
-[UFO - Ultimate Follower Overhaul](http://skyrim.2game.info/detail.php?id=14037):フォロワーオーバーホールMOD。
--[UFO - Ultimate Follower Overhaul Japanese Translation](http://skyrim.2game.info/detail.php?id=19548):UFO - Ultimate Follower Overhaul 1.2gの日本語化パッチ 
---UFOをアンインストールする際には、必ず「ホタルのティナ」に3回話しかけて、UFOの全機能をデフォルトの状態に戻してください。ティナはリバーウッド村の製材所のある小島の端にいます。
-[Wardrobe Manager](http://skyrim.2game.info/detail.php?id=34222):高機能なフォロワーの自動着替えMOD
-[Skyrim Beautiful Followers - SBF](http://skyrim.2game.info/detail.php?id=37861):全ての既存女性フォロワーNPCの容姿を変更します。
--[FollowerLivePackage](http://skyrim.2game.info/detail.php?id=33002):フォロワーの標準AIを拡張、会話の追加、FLP枠フォロワーとして108体まで勧誘可能。略称「FLP」。
-[Dwarven Doll Followers](http://skyrim.2game.info/detail.php?id=40458):ドワーフ人形のフォロワー5人とドワーフのオートマトンを召喚する魔法を追加します。導入後、セーブ→ロードを行い数時間待機して下さい。

##フォロワー個別 
--[Gunner follower_Cheryl](http://skyrim.2game.info/detail.php?id=59556):ホワイトランのドラゴンズリーチで出会えます。
--[Rabi Follower_Japanese Custom Voice](http://skyrim.2game.info/detail.php?id=71167):ソリチュードのブルー・パレスで会うことができ、所定の会話ののちフォロワーに加えることができます。
--[Vilja in Skyrim](http://skyrim.2game.info/detail.php?id=26393):バナードメアで出会えます。
--[Poet follower](http://skyrim.2game.info/detail.php?id=45862):リバーウッドのスリーピングジャイアントで出会えます。
---[【Skyrim】　Poet はだか化 メモ _14/03/27加筆修正](http://criticaldays2.blogspot.jp/2014/03/skyrim-poet.html)
--[Mary Follower_Japanese Custom Voice](http://skyrim.2game.info/detail.php?id=67507):ホワイトランの死者の間で会うことができ、所定の会話ののちフォロワーに加えることができます。
--[Mango Follower](http://skyrim.2game.info/detail.php?id=73669):リバーウッド南西にある鉱山エンバーシャード鉱山内にいます。
--[Lolidia](http://skyrim.2game.info/detail.php?id=79159):リバーウッドにいる
--[Imo Follower](http://skyrim.2game.info/detail.php?id=61958):ホワイトラン、死者の間にて発見できるでしょう
--[YuiH StandAlone Follower - Merura](http://skyrim.2game.info/detail.php?id=58867):UNPetite体型、バナードメアで会えます。
--[Elina Follower](http://skyrim.2game.info/detail.php?id=65761):ホワイトランにあるドラゴンズリーチで
出逢えます。体型はCBBE、UNPから選べます。
--[GCE Follower Torte](http://skyrim.2game.info/detail.php?id=60126):召喚魔法使いTorte(トルテ)を追加します。ドーンスターの宿屋ウィンドピークに滞在しています。
--[The Three Legal Elves or smaller Meridia](http://skyrim.2game.info/detail.php?id=78881):三人の合法エルフのフォロワーを追加します。
--[Bridget Follower](http://skyrim.2game.info/detail.php?id=69948):ソリチュード ウィンキング・スキーヴァーにいます。
---[SIZE DOES MATTER - NPCs do not rescale shrink resize - less camera restrictions](http://skyrim.2game.info/detail.php?id=41304):元の身長に戻らずにアニメーションが再生されます
---[Kankaraya](http://skyrim.2game.info/detail.php?id=49292):さまざまなアイテムを販売するお店「かんから屋」を追加します。
ファルクリースの北西、マップマーカーが表示されています。UNP体型用。
--[Patricia](http://skyrim.2game.info/detail.php?id=76959):ソリチュード馬屋の屋外にいます。UNP体形、重量は0で結婚はできません。 
---[VVE - Vanilla Voice Expansion (Formerly MFVM)](http://skyrim.2game.info/detail.php?id=36913):フォロワー化対応ボイスを拡張し、vanillaではフォロワーにできなかったMaleElfHaughty等のボイスのキャラクターもフォロワーとして雇用出来るようにします。
--[Ersilia Follower](http://skyrim.2game.info/detail.php?id=73048):ホワイトランのバーナード・メアにErsiliaを追加します。
--[Marie Rose Follower](http://www.loverslab.com/topic/33560-adenzs-follower/):She is the Assassin, Marriable and Essencial.Location: The Arcanaeum, College of Winterhold.
--[Cinnamon Follower](http://ash020108.blog.fc2.com/blog-entry-31.html):彼女の名前はCinnamon(シナモン)。ホワイトランで暮らす女の子です。冒険者に憧れており、ホワイトランにあるキナレス聖堂で冒険に出る日を夢見ています。戦闘では片手武器や弓を駆使して戦い、自己回復の魔法も使えますが戦闘力自体は高くありません。
--[Betty Follower](http://skyrim.2game.info/detail.php?id=76062):ファルクリースにスタンドアローンフォロワーのBettyを追加します。
--[The Avatar of Meridia](http://skyrim.2game.info/detail.php?id=76704):"Avatar of Meridia"を追加します。導入後、キルクリースの共同墓地内に「メリディアの呼び声」という本が追加されます。読むとメリディア像の前に彼女が現れます。一度話しかければ仲間になります。彼女はドーンブレイカー（真打ち）と強化したメリディアビームで闘い、２体のメリディアの分霊「メリディアの威光」、「メリディアの栄光」を呼び出します。分霊もそれぞれメリディアビームで闘います。
--[MashiraFollowers](http://skyrim.2game.info/detail.php?id=74807):4人のスタンドアローンフォロワーを追加します。(Erika,Mikan,Jimi,Nana)
--[Lucille REPLACE](http://skyrimfollower.blog.fc2.com/blog-entry-23.html):Follower Lucille ver 1.0 (ルシール) をより少女っぽくリプレイスします。
--[Follower Nono](http://skyrimfollower.blog.fc2.com/blog-entry-182.html):スタンドアローンフォロワー Nono(ノノ)を追加します。リバーウッド・トレーダーで出会えます。
--[Follower Meril](https://msz-misuzu.jimdo.com/msz-skyrim-mods/followers-characters/): 身体は小さいが、片手剣・盾と弓の扱いに長けたエルフの戦士。ドーンガードの一員。ちょっとした特殊技？を持っている。Location: Dayspring Canyon 
--[Rinko](http://skyrim.2game.info/detail.php?id=77462):名前: Rinko、種族: ノルド、特技: 両手武器、居場所: ロリスクテッド宿屋「フロストフルーツ」
--[Follower_Ruru](http://skyrim.2game.info/detail.php?id=83441):リバーウッド「スリーピングジャイアント」に滞在しています。近接物理とシャウトを使用。ファンネル的なものがついてきます。
--[CFollowersMea](http://skyrim.2game.info/detail.php?id=85897):フォロワー「メア」を追加します。彼女はホワイトランの酔いどれハンツマンにいます。Sevenbase体型。
--[CFollowersRin](http://skyrim.2game.info/detail.php?id=82995):フォロワー「リン」を追加します。彼女はホワイトランの酔いどれハンツマンにいます。Sevenbase体型。
--[MashiraSerana](http://skyrim.2game.info/detail.php?id=75254):セラーナの容姿を変更します。また、容姿を幼くしたLittle Girl Edition, またそれぞれのセラーナと同じ容姿をしたAliceというフォロワーを追加するファイルを別に用意しています。
--[Miu - child witch](http://skyrim.2game.info/detail.php?id=86060):リバーウッドのアルヴォア家に養子のMiu(みう)を追加します。Relationship Dialogue Overhaulが必要。
--[SoranatsuFollowers](http://skyrim.2game.info/detail.php?id=84867):女性3名・男性1名のフォロワーを追加します。
--[Team DOVAHBELIIK](http://skyrim.2game.info/detail.php?id=64518):数人の女性フォロワーを追加。UNPB。Paarthは死者の間（ホワイトラン)。
---[ATF版Alduine 2](https://allthefallen.ninja/index.php?/topic/1892-irinotecans-craptastic-loli-patches-and-other-buggery/page-22#entry194707)
--[Winterhold Shelter](http://skyrim.2game.info/detail.php?id=86736):女性フォロワーAyana(アヤナ)とプレイヤーホーム、ダンジョン、NPCを追加します。
--[Imo Follower](http://skyrim.2game.info/detail.php?id=61958):ホワイトラン、死者の間にて発見できるでしょう。髪の毛・透明化バグ注意。
--[MTNKFollowerAnge](https://ux.getuploader.com/mitinoku/):みちのくさんのロリフォロワー「ANGE（アンジェ）」を追加します 。モーサルの宿屋にいます。
--[Regia Follower](http://skyrim.2game.info/detail.php?id=72263):スタンドアロンフォロワーの姉妹「RegiaとRegiana」を追加します。Regiaはソリチュードの宿屋「ウィンキングスキーバー」、Regianaはウィンターホールドの宿屋「フローズンハース」にいます。
---[こっぺぱんブログ お気に入りフォロワー　Regia Follower ](http://kumama1453.blog.fc2.com/blog-entry-474.html)
--[Yuki-Followers(4Hair-Style)](http://kp4068.tistory.com/1425)
---[Skyrim Girls](http://skyrimfollower.blog.fc2.com/blog-entry-95.html):スタンドアロンフォロワー Yuki(ユキ) を追加します。
--[JD FOLLOWER in SKYRIM](http://zaiaixin.tumblr.com/post/126431872385/by-zaizai-and-%E5%9F%BA%E5%BE%B7-jd-follower-in-skyrim-%E4%BD%BF%E7%94%A8%E8%BF%87%E7%9A%84mod): Dragonsreach  Whiterun
--[follower Momo](https://skyrim.2game.info/detail.php?id=75408):ホワイトランのマーケット付近にいます。
--[Brisa Follower](https://skyrim.2game.info/detail.php?id=79966):ファルクリース宿「デッドマンズ・ドリンク」

###導入済み 
--[Gunner follower_Cheryl](http://skyrim.2game.info/detail.php?id=59556)
--[Poet follower](http://skyrim.2game.info/detail.php?id=45862)
--[Mary Follower_Japanese Custom Voice](http://skyrim.2game.info/detail.php?id=67507)
--[Mango Follower](http://skyrim.2game.info/detail.php?id=73669)
--[Lolidia](http://skyrim.2game.info/detail.php?id=79159)
--[YuiH StandAlone Follower - Merura](http://skyrim.2game.info/detail.php?id=58867)
--[Elina Follower](http://skyrim.2game.info/detail.php?id=65761)
--[GCE Follower Torte](http://skyrim.2game.info/detail.php?id=60126)
--[Bridget Follower](http://skyrim.2game.info/detail.php?id=69948)
--[Patricia](http://skyrim.2game.info/detail.php?id=76959)
--[Ersilia Follower](http://skyrim.2game.info/detail.php?id=73048)
--[Marie Rose Follower](http://www.loverslab.com/topic/33560-adenzs-follower/)
--[Cinnamon Follower](http://ash020108.blog.fc2.com/blog-entry-31.html)
--[Betty Follower](http://skyrim.2game.info/detail.php?id=76062)
--[The Avatar of Meridia](http://skyrim.2game.info/detail.php?id=76704)
--[MashiraFollowers](http://skyrim.2game.info/detail.php?id=74807)
--[Lucille REPLACE](http://skyrimfollower.blog.fc2.com/blog-entry-23.html)
--[Follower Nono](http://skyrimfollower.blog.fc2.com/blog-entry-182.html)
--[Follower Meril](https://msz-misuzu.jimdo.com/msz-skyrim-mods/followers-characters/) 
--[Rinko](http://skyrim.2game.info/detail.php?id=77462)
--[Follower_Ruru](http://skyrim.2game.info/detail.php?id=83441)
--[CFollowersMea](http://skyrim.2game.info/detail.php?id=85897)
--[CFollowersRin](http://skyrim.2game.info/detail.php?id=82995)
--[MashiraSerana](http://skyrim.2game.info/detail.php?id=75254)
--[Miu - child witch](http://skyrim.2game.info/detail.php?id=86060)
--[SoranatsuFollowers](http://skyrim.2game.info/detail.php?id=84867)
--[Winterhold Shelter](http://skyrim.2game.info/detail.php?id=86736)
--[Imo Follower](http://skyrim.2game.info/detail.php?id=61958)
--[MTNKFollowerAnge](https://ux.getuploader.com/mitinoku/)

###テスト中 
--[F177 Followers](http://skyrim.2game.info/detail.php?id=49935):Mira, Monica, Nora, Sandraを追加します。ホワイトラン 酔いどれハンツマンとドラゴンズリーチにいます。
--[Regia Follower](http://skyrim.2game.info/detail.php?id=72263):スタンドアロンフォロワーの姉妹「RegiaとRegiana」を追加します。
--[AVA follower](http://skyrim.2game.info/detail.php?id=59053):中性的なイケメン男性フォロワー「AVA」を追加します。ホワイトラン、バナードメアで出会えます。アップデートで少年バージョンが追加されました。
--[グレット de フォロワー v1.0(Grrette v1.0)](http://minerva-net.sumomo.ne.jp/html-my/my0025.html):体型UNPB-BBP体型になっています。弓・片手剣・軽装・隠密が得意なレンジャータイプで、二刀流も可能になっています。種族はエルフっ娘。導入後はロリクステッドの宿屋「フロストフルーツ」に居ます。
--[Tawara Follower](http://skyrim.2game.info/detail.php?id=89039):スタンドアロンのフォロワーTawaraを追加します。フローキの小屋にいます。戦闘中の移動速度は200、スイング速度は2.5 倍です。
--[ARTA Follower Aurora(Standalone) ](http://skyrim.2game.info/detail.php?id=89011):スタンドアローンフォロワー「 Aurora 」を追加します。電撃魔法が得意で体力が少なくなると治癒魔法で自己を回復します。酔いどれハンツマンにいます。
--[Snippy - Droid Follower](http://skyrim.2game.info/detail.php?id=87967):ドワーフ製のドロイドフォロワーSnippyを追加します。(スターウォーズEP7に登場するドロイドBB-8にインスパイアを受けています)彼は戦闘には参加しませんが、いろいろな機能を提供します。
--[【MOD】haijin Followers - The Bikini Armor Sisters - V1.5](http://helloworld-tes.com/2017/10/21/post-268/):ネム&ネル -リバーウッドのアルヴォア宅前
---[【MOD】HDT Vagina Body in haijin Followers V1.4](http://underground.helloworld-tes.com/2017/05/06/post-973/):廃人aのフォロワーのHDT Vagina体型…つまり、チンチンとか突っ込んだ時にマンマンがくぱぁする体型にするオプションMODです。BodySlide and Outfit Studio or Working Vagina から hdtVagina.xmlがHDTの設定ファイルです。後者のMODの場合、リンク先の下部にある Trepleen-Daie HDT CBBE body + Vagina2.4 + XPMSE v2.50 Collision XML.rar に
同梱されているのでMODそのまま導入するか、中のhdtVagina.xmlを抜き出して Skyrim\Data\SKSE\Plugins の中に入れてください。
---[HDT Bounce and Jiggles UNP](http://skyrim.2game.info/detail.php?id=72030):MISCELLANEOUSからBounce and Jiggles 7.8 - SOS Full Patch SOSにコリジョンを付与するためのパッチです。これがないとマンマンをHDT化しててもセックス時にくぱぁしてくれません。
--[Liliane Follower](http://skyrim.2game.info/detail.php?id=88061):女性フォロワー「Liliane」を追加します。居場所はホワイトランの戦乙女の炉。不死属性、結婚可能、彼女は裸です。
--[Marla](http://skyrim.2game.info/detail.php?id=90801):女性フォロワー「Marla」を追加します。居場所はDragonreach ダンジョン。
--[Follower - Eleonora](http://skyrim.2game.info/detail.php?id=59477):スノーエルフの吸血鬼「エレオノーラ」を追加します。ホワイトランのドラゴンズリーチで出会えます。
--[Liarsa009 Follower](http://kp4068.tistory.com/2657?category=584236):She's skin texture seems quite close to nini char too. At closer look, it isn't just Pure skin. 
--[rk followers](http://skyrim.2game.info/detail.php?id=45578):1.6Yukiと1.7Meiがお薦め。
--[Adernia](http://skyrim.2game.info/detail.php?id=92120):リバーウッドの宿屋（スリーピングジャイアント）にいます。
--[GK Girl Followers Ver.2.6](https://skyrim.2game.info/detail.php?id=86324):ノルドの少女フォロワーを5人追加します。5人は格闘専用に強化された戦闘スキルを所持しています。
--[Follower - Chantez](https://skyrim.2game.info/detail.php?id=60837):ホワイトランの死者の間で出会えます。
--[Ashley](http://killingdoll.com/?p=26611):導入後、大がキナレス聖堂、小が死者の間にいます。

###インストール予定 
--[follower Keto v01](http://skyrim.2game.info/detail.php?id=77533):地黒なのでFace liteの使用をおすすめします。オプションで水着の日焼け跡スキンあり。Location : Sleeping Giant Inn 
--[ARO_Followers](http://skyrim.2game.info/detail.php?id=74815):姉妹の独立型フォロワーを追加します。ロゼッタ(Rosetta)：ジョルバスクル、ヴィオレッタ(Violetta)：バナード・メア
--[Mutimuti Archer Loe](http://skyrim.2game.info/detail.php?id=76192):ソリチュードの東帝都社の倉庫の上にある橋の所にいます。
--[Lazy Moment自作フォロワー第2弾「エレナ」](http://da-moment.ldblog.jp/archives/40450205.html):レンジャーフォロワー「エレナ」を追加します。バナード・メアで出会うことができます。
--[NOG Follower Rebecca 3.0](http://skyrim.2game.info/detail.php?id=74104):Nightgate Innにいます。
--[Skyrim Healer Onean](http://skyrim.2game.info/detail.php?id=72385):カスタムボイスのヒーラーフォロワー追加。場所はホワイトラン。
---[Skyrim healer Onean Cosmetic Patch](http://www.nexusmods.com/skyrim/mods/82533/?tab=2&navtag=http%3A%2F%2Fwww.nexusmods.com%2Fskyrim%2Fajax%2Fmodfiles%2F%3Fid%3D82533&pUp=1)
--[Vampire Follower - Farith Granius](http://skyrim.2game.info/detail.php?id=58969):吸血鬼の少女フォロワー「Farith Granius」を追加します。
彼女とはマーラの目の池（マーラの目の隠れ家）で出会えます。
--[[[REQUEST] Vampire Follower - Farith Granius(loversLab):https://www.loverslab.com/topic/38047-request-vampire-follower-farith-granius/]]

###ペンディング中 
--[Skyrim Beautiful Followers - SBF](http://skyrim.2game.info/detail.php?id=37861):CTD
--[Rabi Follower_Japanese Custom Voice](http://skyrim.2game.info/detail.php?id=71167):  Rabi Follower_JP_1.51 ならOK
--[Vilja in Skyrim](http://skyrim.2game.info/detail.php?id=26393): OutOfMemoryでインストール出来ない
---RomanceSpoilersForVeryNervousSuitors
--[ARO_Followers](http://skyrim.2game.info/detail.php?id=74815):重い
--[Follower Motoyan UNP Petite](http://skyrim.2game.info/detail.php?id=73983):彼女とはRiverwoodの入り口付近で出会えます。ついてこない。
--[しのぷ](https://twitter.com/tes5followers?lang=ja):バニラの子供ボイスから引用して88種の音声を同梱してます。リバーウッドトレーダーにいます。
--[The Erotic Adventures of Misty Skye](http://skyrim.2game.info/detail.php?id=83060):セクシーなフォロワー「ミスティ・スカイ」と、彼女に関するおバカなクエストを追加します。
---[The Erotic Adventures of Misty Skye CC](http://skyrim.2game.info/detail.php?id=85809):The Erotic Adventures of Misty Skyeの姉妹のリプレイス。

#導入済みMOD(その他) 
-[SKSE](http://skse.silverlock.org/)
-[SKY UI](http://www.nexusmods.com/skyrim/mods/3863/?)
-[ECE(Enhanced Character Edit)](http://skyrim.2game.info/detail.php?id=12951)
-[ShowRaceMenu Alternative](http://skyrim.2game.info/detail.php?id=20394)
-[ShowRaceMenu Precache Killer](http://skyrim.2game.info/detail.php?id=33526):Data/SKSE/pluginのshowRaceMenu_preCacheKiller.dllのみでespなし
-[SG Female Textures Renewal](http://skyrim.2game.info/detail.php?id=35267)
-[DIMONIZED UNP female body](http://skyrim.2game.info/detail.php?id=6709):espなし
--[UNP Replacer Configuration Package](http://skyrim.2game.info/detail.php?id=20884):espなし
-[Amazing Follower Tweaks(AFT)](http://skyrim.2game.info/detail.php?id=15524)
--TESVTranslatorで日本語化
-SG Hair Pack 268 Edition

-[Shedding Lace UD](http://eiheispot1.blog.fc2.com/blog-entry-485.html)
-[Heilige Mutter Armor](http://eiheispot1.blog.fc2.com/blog-entry-86.html)

-[Face Light](http://www.nexusmods.com/skyrim/mods/13457/?)
-[Female Facial Animation](http://skyrim.2game.info/detail.php?id=35303)
-[Face to face conversation](http://skyrim.2game.info/detail.php?id=30533)
-[Bowlegged jump animation Fix](http://skyrim.2game.info/detail.php?id=7416)
-[Unread Books Glow](http://skyrim.2game.info/detail.php?id=10012)
-[Blocksteal Redux - Prevents accidentally pick up](http://www.nexusmods.com/skyrim/mods/61605/?)
-[Crafting Supplies](http://skyrim.2game.info/detail.php?id=37696)
-[Floating Healthbars](http://www.nexusmods.com/skyrim/mods/58728/?)

-[univision Face](http://skyrim.2game.info/detail.php?id=14569)
-[Mikan Eyes](http://skyrim.2game.info/detail.php?id=56056)

-[PapyrusUtil - Modders Scripting Utility Functions](http://skyrim.2game.info/detail.php?id=58705)
-[Quick Menus](http://skyrim.2game.info/detail.php?id=74133)
-[Haven Bag](http://skyrim.2game.info/detail.php?id=21454)

-[Customizable Camera](http://skyrim.2game.info/detail.php?id=37347)
-[Crawl on fours animation](http://skyrim.2game.info/detail.php?id=33097)

-[Body Options](http://skyrim.2game.info/detail.php?id=27352):
--[BodyChange - A Multi-Bodyshape System](http://skyrim.2game.info/detail.php?id=37546)
-[Fair Skin Complexion](http://skyrim.2game.info/detail.php?id=51602)

##テスト中 
-[Fores New Idles in Skyrim - FNIS](http://skyrim.2game.info/detail.php?id=11811):NPCやプレイヤーをアニメーションさせます。略称「FNIS」

##ペンディング中 
-[UFO - Ultimate Follower Overhaul](http://skyrim.2game.info/detail.php?id=14037): AFTを優先
--[UFO - Ultimate Follower Overhaul Japanese Translation](http://skyrim.2game.info/detail.php?id=19548): AFTを優先
-[Wardrobe Manager](http://skyrim.2game.info/detail.php?id=34222):複数フォロワーが不安定
-[Girl of the Innocence](http://skyrim.2game.info/detail.php?id=76405)
--以下のテクスチャを上書き。UNP Replacerは再インストール、GoIのhead部分のみ残す。
---SG Female Textures Renewal
---univision Face
---ECE(Enhanced Character Edit)
---UNP Replacer Configuration Package

##通常OFF 
-[You Call That Skimpy - UNP](http://skyrim.2game.info/detail.php?id=11951)
-[[SexiS - Sex in Skyrim [Alpha] [Inactive] :http://www.loverslab.com/topic/15205-sexis-sex-in-skyrim-alpha-inactive/]]
---SexiS Core
---SexiS Cupid
---SexiS Defeated

-[Skyrim SexLab - Sex Animation Framework](http://www.loverslab.com/files/file/150-skyrim-sexlab-sex-animation-framework-v162-updated-jun-3rd-2016/)
---[SexLab Books of Love](http://www.loverslab.com/topic/17557-wip-sexlab-books-of-love/)
--[SexLab Horny Followers](http://www.loverslab.com/files/file/189-sexlab-horny-followers/)

-[Body Options](http://skyrim.2game.info/detail.php?id=27352)

##アンインストール 
-[Skyrim Beautiful Followers - SBF](http://skyrim.2game.info/detail.php?id=37861):CTD

#リンク 
-[Skyrim Wiki JP](http://wiki.skyrim.z49.org/)
-[ラプンツェルの塔](http://blog.livedoor.jp/eeeop/archives/1469699.html)
-[独創的な狂人たち@skyrim](http://ransumo.blog.fc2.com/blog-entry-57.html)
-[【2016年版】いまさら始める「SKYRIM」：最初に入れたいMod編 ](http://graffito.blog14.fc2.com/blog-entry-2478.html)
-[【SKYRIM】 おすすめMOD一覧紹介](http://rabilinth.blog.fc2.com/blog-entry-113.html)
-[Skyrimの個人的おすすめMODリスト（必須系）](http://skmod.hatenablog.com/entry/mod/osusume2)
-[世界のノドでシャウトしよう！ - 凡人向け PC 版 Skyrim の遊び方ガイド](http://www.ownway.info/Skyrim/)

#導入済みMOD 以前の控え 
-[SKSE](http://skse.silverlock.org/)
-[SKY UI](http://www.nexusmods.com/skyrim/mods/3863/?)
-[ECE(Enhanced Character Edit)](http://skyrim.2game.info/detail.php?id=12951)
-[ShowRaceMenu Alternative](http://skyrim.2game.info/detail.php?id=20394)
-[ShowRaceMenu Precache Killer](http://skyrim.2game.info/detail.php?id=33526)
-SG Hair Pack 268 Edition
-[DIMONIZED UNP female body](http://skyrim.2game.info/detail.php?id=6709)
-[Caliente's Beautiful Bodies Edition -CBBE-](http://skyrim.2game.info/detail.php?id=2666)
-[CBBEv3M Body Repalacer](http://skyrim.2game.info/detail.php?id=13180)
-[R18Pn 00 - Heilige Mutter Armor for UNP and CBBE V3](http://skyrim.2game.info/detail.php?id=13098)
-[univision Face](http://skyrim.2game.info/detail.php?id=14569)

-[R18Pn 00 - Fiona Armor for UNP](http://skyrim.2game.info/detail.php?id=13082)
-[SG Female Textures Renewal](http://skyrim.2game.info/detail.php?id=35267)
-[Amazing Follower Tweaks(AFT)](http://skyrim.2game.info/detail.php?id=15524)
-TESVTranslator
-[UFO - Ultimate Follower Overhaul](http://skyrim.2game.info/detail.php?id=14037)
--[UFO - Ultimate Follower Overhaul Japanese Translation](http://skyrim.2game.info/detail.php?id=19548)
-[Gunner follower_Cheryl](http://skyrim.2game.info/detail.php?id=59556)

-[Vilja in Skyrim](http://skyrim.2game.info/detail.php?id=26393):NG
-[Rabi Follower_Japanese Custom Voice](http://skyrim.2game.info/detail.php?id=71167):NG
-[Skyrim Beautiful Followers - SBF](http://skyrim.2game.info/detail.php?id=37861):NG
