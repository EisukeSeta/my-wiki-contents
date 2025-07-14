[[seta.go.dyndns.org]]

#目次 
#contents

#apt 
##aptの使い方 （aptitudeを推奨）
 aptitude install YYXXXYY
 aptitude search XXX

 apt-get {update|upgrade|dist-upgrade}
 apt-get install YYXXXYY
 apt-cache pkgnames XXX
 apt-cache show YYXXXYY

インストール済みパッケージ一覧
 dpkg -l

###apt-line 
 deb http://ftp.debian.org/debian lenny main contrib non-free
 
 deb http://security.debian.org/ lenny/updates main contrib non-free
 deb http://volatile.debian.org/debian-volatile lenny/volatile main contrib non-free 
 
 deb http://ftp.jp.debian.org/debian-volatile lenny/volatile main contrib non-free

[lenny/Package](http://debian.fam.cx/index.php?lenny%2FPackage)

###Debian Backports 
testing や unstable から Backport したパッケージを提供している。
どんなパッケージが提供されているかは、 http://packages.debian.org/lenny-backports/ を参照。

 deb http://ftp.jp.debian.org/debian-backports lenny-backports main contrib non-free
 deb-src http://ftp.jp.debian.org/debian-backports lenny-backports main contrib non-free

上記以外のミラーは Debian Backports - Mirrors を参照。

使い方は Debian Backports - Instructions や パッケージの FAQ - Backports を参照。

まずは debian-backports-keyring パッケージをインストールし、公開鍵を入手して下さい。

###apt-get 
 apt-get install debian-backports-keyring
 apt-get install aptitude

 aptitude install php5
 aptitude install ddclient
 aptitude install mysql-server
 aptitude install php5-mysql

##apt以外でインストール 
###tarball 
 pukiwiki-1.4.7_notb_utf8.tar.gz
 wordpress-3.0.1-ja.tar.gz

#パッケージのインストールメモ 
//**apache2 
///etc/apache2/apache2.confのユーザー、グループを変更。
// User www-data
// Group www-data
///var/www/html以下も適宜変更。

##MySQL 
###参考URL 
+[Debian etch に MySQL 5 と設定ツールを導入する](http://asaasa.tk/wiki/?Debian%2FServer%2FMySQL)
+[debianにMySQLをインストールして設定する - 見果てぬ夢](http://d.hatena.ne.jp/Loups-garous/20080919/1221816870)

###インストール 
 $ sudo aptitude install mysql-server
 $ sudo aptitude install php5-mysql

###起動確認 
 $ mysqladmin ping -u root -p
 mysqld is alive

###uft-8設定 
/etc/mysql/my.cnfを編集。
 [client]
 default-character-set=utf8
 
 [mysql] 
 default-character-set=utf8
 
 [mysqld]
 default-character-set=utf8
 language=/usr/share/mysql/japanese
 skip-character-set-client-handshake

文字コード確認。
 mysql> status
 mysql> SHOW VARIABLES LIKE 'char%'; 

##WordPress日本語版 
###参考URL 
+[WordPress.日本語](http://wpdocs.sourceforge.jp/)
+[wordpressの設定 -metalglue](http://d.hatena.ne.jp/metalglue/20061204/1165231144)

###インストール 
[WordPress.日本語](http://wpdocs.sourceforge.jp/)の[WordPressのインストール](http://wpdocs.sourceforge.jp/WordPress_%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)に従い、最新版のWordPress日本語版をダウンロード（[ja.wordpress.org](http://ja.wordpress.org/)）。

MySQLデータベースの準備。
 $ mysql -u root -p
 mysql> CREATE DATABASE wordpress;
 mysql> GRANT ALL PRIVILEGES ON wordpress.* TO "wordpressusername"@"localhost"
    -> IDENTIFIED BY "password";
 mysql> FLUSH PRIVILEGES;

wordpressのインストール
+[http](//seta.mydns.jp/html/wordpress/wp-admin/install.php:http://seta.mydns.jp/html/wordpress/wp-admin/install.php)にアクセス。
+「5分でできるインストールプロセス」を実施。
+最初の書き込みをチェックして終わり。

###アクセス 
[http](//seta.mydns.jp/html/wordpress:http://seta.mydns.jp/html/wordpress)
