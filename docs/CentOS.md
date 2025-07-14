[[seta.go.dyndns.org]]
*yumの使い方 [#z66e98c5]
 $ sudo yum check-update
 $ sudo yum update

*ddclientの設定 [#e43b0cfc]
ddclientのインストール
 $ wget http://cdn.dyndns.com/ddclient.tar.gz
 $ tar zxvf ddclient.tar.gz
 $ cd ddclient-3.7.3
 $ sudo cp ddclient /usr/sbin/
 $ sudo mkdir /etc/ddclient
 $ sudo cp sample-etc_ddclient.conf /etc/ddclient/ddclient.conf
 $ sudo mkdir /var/cache/ddclient
ddclient.confの編集
 daemon=600
 
 ## To obtain an IP address from Web status page (using the proxy if defined)
 use=web, web=checkip.dyndns.org/, web-skip='IP Address'
 
 login=user-login-name
 password=user-password
 wildcard=yes
 
 ##
 ## dyndns.org dynamic addresses
 ##
 ## (supports variables: wildcard,mx,backupmx)
 ##
 server=members.dyndns.org,  ¥
 protocol=dyndns2            ¥
 seta.go.dyndns.org
自動起動の設定
 $ sudo chmod 400 /etc/ddclient/ddclient.conf
 $ sudo cp sample-etc_rc.d_init.d_ddclient /etc/rc.d/init.d/ddclient
 $ sudo /sbin/chkconfig --add ddclient
 $ sudo /etc/rc.d/init.d/ddclient start
