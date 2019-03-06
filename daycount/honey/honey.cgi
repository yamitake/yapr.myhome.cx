#!/usr/bin/perl

#┌─────────────────────────────────
#│ Honey Board v2.1 - 2004/02/06
#│ Copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────
$ver = 'Honey Board v2.1';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問は一切お受けいたしておりません。
#└─────────────────────────────────
#
# 【ファイル構成例】
#
#  public_html (ホームディレクトリ)
#      |
#      +-- honey / honey.cgi    [705]
#            |     honeylog.cgi [606]
#            |     jcode.pl     [604]
#            |
#            +-- img / *.gif
#            |
#            +-- lock [707] /
#
#
# [ チェックモードの仕方 ] : mode=check という引数を付けて呼出す
#
#  例  http://～～/honey.cgi?mode=check

#-------------------------------------------------
#  基本設定
#-------------------------------------------------

# 文字コードライブラリ取込み
require './jcode.pl';

# タイトル名
$title = "Honey Board";

# タイトル文字の色
$t_color = "#DD0000";

# タイトル文字のタイプ
$t_face = "ＭＳ Ｐゴシック";

# タイトル文字サイズ
$t_point = '24px';

# 本文の文字サイズ
$b_size = '13px';

# スクリプト名
$script = './honey.cgi';

# ログファイル名
$logfile = './honeylog.cgi';

# 管理用パスワード
$pass = '1202';

# 最大記事数（これを超える記事は古い順に削除されます）
$max = 50;

# 戻り先
$home = "../index.html";

# 画像格納ディレクトリ
# → フルパスなら http:// から記述する
# → 最後は / を閉じない
$imgurl = "./img";

# 背景色、文字色
$bgrnd = "";		# 壁紙
$bgcol = "#FFFFFF";	# 背景色
$text  = "#452815";	# 文字色
$link  = "#0000FF";	# リンク色：未訪問
$vlink = "#800080";	# リンク色：既訪問
$alink = "#DD0000";	# リンク色：訪問中

# 記事タイトル色 / 記事Noの色
$onepnt = "#008000";

# 文字色
@colors = ('#800000','#DF0000','#008040','#0000FF','#C100C1','#FF80C0','#FF8040','#000080');

# Ｅメールアドレスの必須入力 (0=no 1=yes)
$in_email = 0;

# 記事の更新は method=POST 限定 (0=no 1=yes)
#  --> 連続投稿などの荒らし対策
$postonly = 1;

# 同一IPアドレスからの連続投稿時間（秒数）
#  --> 連続投稿などの荒らし対策
#  --> 値を 0 にするとこの機能は無効になります
$wait = 60;

# URLの自動リンク (0=no 1=yes)
$autolink = 1;

# １ページあたりの記事表示件数
$logview = 7;

# レスがついたらツリー毎トップへ移動 (0=no 1=yes)
$top_sort = 1;

# ロックファイル機構 (0=no 1=symlink関数 2=mkdir関数)
$lockkey = 2;

# ロックファイル名
$lockfile = "./lock/honey.lock";

# メール通知機能
#  --> 0 : no
#  --> 1 : yes 自分の投稿記事もメール通知する
#  --> 2 : yes 自分の投稿記事はメール通知しない
$mailing = 0;

# sendmailのパス（メール通知する場合）
$sendmail = '/usr/lib/sendmail';

# メール通知先アドレス（メール通知する場合）
$mailto = 'xxx@xxx.xxx';

# キャラクタを指定（上下の配列はペアで)
@icon1 = (
	'cake1.gif','aomusi.gif','budo.gif','cake2.gif','flyingrabi.gif',
	'icon07.png','icon8.gif','icon08.png','icon9.png','kame.gif','kata.gif',
	'ken.jpg','lespaul_ys120.gif','mm120.gif','neko.gif','strato.gif','robo1-3-4.gif');
@icon2 = (
	'ケーキ','あおむし','ぶどう','ケーキ２','飛ぶウサギ',
	'OL風1','OL風2','OL風3','中国風','カメ','カタツムリ',
	'ケンちゃん','レスポール','ミュージックマン','勉強ネコ','ストラト','ロボ');

# 管理者用アイコン
#  --> 管理アイコンを指定する場合は「削除キー」欄に管理用パスワードを
#      同時に入力する必要があります。
$mgr_icon = "master.gif";

# タグ広告挿入オプション
#   → <!-- 上部 --> <!-- 下部 --> の代わりに「広告タグ」を挿入する。
#   → 広告タグ以外に、MIDIタグ や LimeCounter等のタグにも使用可能です。
$banner1 = '<!-- 上部 -->';	# 掲示板上部に挿入
$banner2 = '<!-- 下部 -->';	# 掲示板下部に挿入

# アクセス制限（半角スペースで区切る）
#  → 拒否するホスト名又はIPアドレスを記述（アスタリスク可）
#  → 記述例 $deny = '*.anonymizer.com 211.154.120.*';
$deny = '70.86.213.16 82.209.225.* 193.201.103.80 204.113.91.19 210.165.203.83 219.102.48.50 66.117.48.64 212.98.168.142 82.209.247.139 81.216.80.40 216.130.157.51 194.126.200.17 210.165.203.* 211.193.148.80 210.105.108.155 157.181.162.22 61.32.96.145 203.194.209.* 213.249.155.239';

# タイトル画像を使う場合
#  --> 画像URLを http:// から記述
$ImgT = "";
$ImgW = 150;  # 画像横幅
$ImgH = 50;   # 画像縦幅

# 投稿後の処理
#  → 掲示板自身のURLを記述しておくと、投稿後リロードします
#  → ブラウザを再読み込みしても二重投稿されない措置。
#  → Locationヘッダの使用可能なサーバのみ
$location = '';

# ホスト取得方法
# 0 : gethostbyaddr関数を使わない
# 1 : gethostbyaddr関数を使う
$gethostbyaddr = 0;

# 他サイトから投稿排除時に指定する場合（セキュリティ対策）
#  → 掲示板のURLをhttp://から書く
$baseUrl = '';

# 親記事の吹出色
# → 順に、「幅」「下地色」「画像ファイル名」
$oyaWid = 500;
$oyaCol = "#E7FFFF";
@oyaCol = ("bl1.gif","bl2.gif","bl3.gif","bl4.gif","bl5.gif","bl6.gif");

# レス記事の吹出色
# → 順に、「幅」「下地色」「画像ファイル名」
$resWid = 380;
$resCol = "#EFEFEF";
@resCol = ("lg1.gif","lg2.gif","lg3.gif","lg4.gif","lg5.gif","lg6.gif");

#-------------------------------------------------
#  設定完了
#-------------------------------------------------

&decode;
&axscheck;
if ($mode eq 'regist') { &regist; }
if ($mode eq 'find') { &find; }
if ($mode eq 'howto') { &howto; }
if ($mode eq 'admin') { &admin; }
if ($mode eq 'usrdel') { &usrdel; }
if ($mode eq 'image') { &image; }
if ($mode eq 'res') { &res_msg; }
if ($mode eq 'check') { &check; }
&html;

#-------------------------------------------------
#  アクセス制限
#-------------------------------------------------
sub axscheck {
	# ホスト名取得
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if ($host eq "") { $host = $addr; }

	local($flag)=0;
	foreach ( split(/\s+/, $deny) ) {
		s/\*/\.\*/g;
		if ($host =~ /$_/i || $addr =~ /$_/i) { $flag=1; last; }
	}
	if ($flag) { &error("アクセスを許可されていません"); }
}

#-------------------------------------------------
#  記事表示処理
#-------------------------------------------------
sub html {
	local($no,$reno,$date,$name,$eml,$sub,$icon,$icon2,
		$com,$color,$url,$host,$pw,$i,$top,$next,$back);

	# ヘッダ
	&header;
	print "<div align=center>\n";
	if ($banner1 ne "<!-- 上部 -->") { print "$banner1\n<p>\n"; }

	# タイトル部
	if ($ImgT) {
		print "<img src=\"$ImgT\" width=$ImgW height=$ImgH alt=\"$title\">\n";
	} else {
		print "<font color=\"$t_color\" face=\"$t_face\" size=5\"><b><span>$title</span></b></font>\n";
	}

	print <<EOM;
<hr width="530">
[<a href="$home" target="_top">トップに戻る</a>]
[<a href="$script?mode=howto">留意事項</a>]
[<a href="$script?mode=find">ワード検索</a>]
[<a href="$script?mode=admin">管理用</a>]
<hr width="530">
EOM

	# フォームを表示
	&form_view;

	$i=0;
	open(IN,"$logfile") || &error("Open Error: $logfile");
	$top = <IN>;
	while (<IN>) {
		($no,$reno,$date,$name,$eml,$sub,$icon,$icon2,$com,$color,$url,$host,$pw) = split(/<>/);
		if ($reno eq "") { $i++; }
		if ($i < $page + 1) { next; }
		if ($i > $page + $logview) { last; }

		if ($eml) { $name = "<a href=\"mailto:$eml\">$name</a>"; }
		if ($url) {
			if ($url !~ /^http/i) { $url = "http://$url"; }
			$url = "<a href=\"$url\" target=\"_blank\"><img src=\"$imgurl/home.gif\" border=0 align=top alt=home></a>";
		}

		# １マスの大きさ
		$pix = 18;

		# レス記事
		if ($reno) {
			$wide = $resWid;
			$iro  = $resCol;
			@gif  = ("",@resCol);

		# 親記事
		} else {
			$wide = $oyaWid;
			$iro  = $oyaCol;
			@gif  = ("",@oyaCol);
		}

		# 記事を表示
		if (!$reno) { print "<br><br>\n"; }
		print "<TABLE BORDER=0><TR>\n";

		# 反転対象部分1
		if (!$flag) {
			print "<TD><img src=\"$imgurl/$icon\"></TD>\n";
			print "<TD><table border=0 cellpadding=0 cellspacing=0><tr>\n";
			print "<td width=$pix><br></td>\n";
		} else {
			print "<TD><table border=0 cellpadding=0 cellspacing=0><tr>\n";
		}

		print "<td><img src=\"$imgurl/$gif[1]\" width=$pix height=$pix></td>\n";
		print "<td width=$wide bgcolor=\"$iro\"><br></td>\n";
		print "<td><img src=\"$imgurl/$gif[2]\" width=$pix height=$pix></td>\n";

		# 反転対象部分2
		if ($flag == 0) {
			print "</tr>";
			print "<tr><td><img src=\"$imgurl/$gif[5]\" width=$pix height=$pix></td>\n";
		} else {
			print "<td width=$pix><br></td></tr>\n<tr>\n";
		}

		print "<td bgcolor=\"$iro\"><br></td>\n";
		print "<td width=\"$wide\" bgcolor=\"$iro\">\n";
		print "<font color=\"$onepnt\"><b>$sub</b></font><br>\n";
		if (!$reno) { print "投稿者："; }
		print "<b>$name</b> - $date <font color=\"$onepnt\">No\.$no</font> ";

		if (!$reno) {
			print "[<a href=\"$script?mode=res&no=$no\">返信</a>] &nbsp; \n";
		}

		print "$url<br>\n";
		print "<blockquote><font color=\"$color\">$com</font></blockquote>\n";
		print "</td><td bgcolor=\"$iro\"><br></td>\n";

		if ($flag == 1) {
			print "<td><img src=\"$imgurl/$gif[6]\" width=$pix height=$pix></td>\n";
		}
		print "</tr><tr>\n";

		# 反転対象部分3
		if ($flag == 0) { print "<td width=$pix><br></td>\n"; }

		print "<td><img src=\"$imgurl/$gif[4]\" width=$pix height=$pix></td>\n";
		print "<td width=\"$wide\" bgcolor=\"$iro\">　</td>\n";
		print "<td><img src=\"$imgurl/$gif[3]\" width=$pix height=$pix></td>\n";

		if ($flag == 1) { print "<td width=$pix><br></td>\n"; }
		print "</tr></table>\n";

		if ($flag == 1) {
			print "</TD><TD><img src=\"$imgurl/$icon\">\n";
		}
		print "</TD></TR></TABLE>\n";

		if (!$reno) {
			if ($flag == 0) { $flag=1; } else { $flag=0; }
		}
	}
	close(IN);

	$next = $page + $logview;
	$back = $page - $logview;

	print "<blockquote><table align=left cellpadding=0 cellspacing=0><tr>\n";
	if ($back >= 0) {
		print "<td><form action=\"$script\">\n";
		print "<input type=hidden name=page value=\"$back\">\n";
		print "<input type=submit value=\"前の$logview件\"></td></form>\n";
	}
	if ($next < $i) {
		print "<td><form action=\"$script\">\n";
		print "<input type=hidden name=page value=\"$next\">\n";
		print "<input type=submit value=\"次の$logview件\"></td></form>\n";
	}
	print "</tr></table>\n";
	print "<table align=right><tr>\n";
	print "<td nowrap align=center><form action=\"$script\" method=\"POST\">\n";
	print "<input type=hidden name=mode value=\"usrdel\">\n";
	print "記事No<input type=text name=no size=3>\n";
	print "削除キー<input type=password name=pwd size=4 maxlength=8>\n";
	print "<input type=submit value=\"削除\"></form></td>\n";
	print "</tr></table></blockquote><br clear=all>\n";

	# 著作権表示（削除不可）
	print "<div align=center>$banner2<p><!-- $ver -->\n";
	print "<span style='font-size:10px;font-family:Verdana,Helvetica,Arial'>\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Honey Board</a> -\n";
	print "</span></div>\n</body></html>\n";
	exit;
}

#-------------------------------------------------
#  書きこみ処理
#-------------------------------------------------
sub regist {
	# 投稿チェック
	if ($postonly && !$post_flag) { &error("不正なアクセスです"); }
	if ($baseUrl) { &refCheck; }

	# フォーム内容をチェック
	if ($in{'name'} eq "") { &error("名前が入力されていません"); }
	if ($in{'comment'} eq "") { &error("コメントが入力されていません"); }
	if ($in_email && $in{'email'} !~ /[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,5}$/) {
		&error("メールアドレスの入力が不正です");
	}
	if ($in{'url'} eq "http://") { $in{'url'} = ''; }

	# 管理者アイコン処理
	if ($in{'icon'} eq $mgr_icon && $in{'pwd'} ne $pass) {
		&error("管理者アイコンは管理者以外は使用できません");
	}

	# ロック処理
	&lock if ($lockkey);

	open(IN,"$logfile") || &error("Open Error: $logfile");
	@lines = <IN>;
	close(IN);

	# 記事NO処理
	$top = shift(@lines);
	($no,$ip,$time2) = split(/<>/, $top);
	$no++;

	# 連続投稿チェック
	if ($addr eq $ip && $wait > $times - $time2)
		{ &error("連続投稿はもうしばらく時間をおいて下さい"); }

	# 削除キーを暗号化
	if ($in{'pwd'} ne "") { $PW = &encrypt("$in{'pwd'}"); }

	# URL自動リンク
	if ($autolink) { &auto_link($in{'comment'}); }

	# 親記事の場合
	if ($in{'reno'} eq "") {

		# 最大記事数処理
		while ($max <= @lines) { pop(@lines); }

		unshift(@lines,"$no<><>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		unshift(@lines,"$no<>$addr<>$times<>\n");

		# 更新
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @lines;
		close(OUT);

	# レス記事の場合：トップソートあり
	} elsif ($in{'reno'} && $top_sort) {
		$f=0;
		$match=0;
		@new=();
		@tmp=();
		foreach (@lines) {
			($no2,$reno2) = split(/<>/);

			if ($in{'reno'} eq $no2) {
				if ($reno2) { $f++; last; }
				$match=1;
				push(@new,$_);

			} elsif ($in{'reno'} eq $reno2) {
				push(@new,$_);

			} elsif ($match == 1 && $in{'reno'} ne $reno2) {
				$match=2;
				push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
				push(@tmp,$_);

			} else { push(@tmp,$_); }
		}
		if ($f) { &error("不正な返信要求です"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		}
		push(@new,@tmp);

		# 更新
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

	# レス記事の場合：トップソートなし
	} else {
		$f=0;
		$match=0;
		@new=();
		foreach (@lines) {
			($no2,$reno2) = split(/<>/);

			if ($match == 0 && $in{'reno'} eq $no2) {
				if ($reno2) { $f++; last; }
				$match=1;

			} elsif ($match == 1 && $in{'reno'} ne $reno2) {
				$match=2;
				push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
			}
			push(@new,$_);
		}
		if ($f) { &error("不正な返信要求です"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		}

		# 更新
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);
	}

	# ロック解除
	&unlock if ($lockkey);

	if ($in{'cook'} eq 'on') {
		&set_cookie($in{'name'},$in{'email'},$in{'url'},$in{'pwd'},$in{'color'},$in{'icon'});
	}

	# メール通知処理
	if ($mailing == 1) { &mail_to; }
	elsif ($mailing == 2 && $in{'email'} ne $mailto) { &mail_to; }

	# リロード
	if ($location) {
		if ($ENV{'PERLXS'} eq "PerlIS") {
			print "HTTP/1.0 302 Temporary Redirection\r\n";
			print "Content-type: text/html\n";
		}
		print "Location: $location?\n\n";
	} else {
		&header;
		print "<div align=center><hr width=400>\n";
		print "<h3>投稿は正常に処理されました</h3>\n";
		print "<form action=\"$script\">\n";
		print "<input type=submit value='掲示板へ戻る'></form>\n";
		print "<hr width=400></div>\n</body></html>\n";
	}
	exit;
}

#-------------------------------------------------
#  ワード検索
#-------------------------------------------------
sub find {
	local($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$res,$url);

	&header;
	print <<"EOM";
[<a href="$script?">戻る</a>]
<ul>
<li>検索したい<b>キーワード</b>を入力し「検索」を押してください。
<li>キーワードは「半角スペース」で区切って複数指定することができます。
<form action="$script" method="POST">
<input type=hidden name=mode value="find">
キーワード <input type=text name=word size=35 value="$in{'word'}">
検索条件 <select name=cond>
EOM

	foreach ("AND", "OR") {
		if ($in{'cond'} eq $_) {
			print "<option value=\"$_\" selected>$_\n";
		} else {
			print "<option value=\"$_\">$_\n";
		}
	}

	print <<EOM;
</select>
<input type=submit value="検索">
</form>
</ul>
EOM

	# ワード検索の実行と結果表示
	if ($in{'word'} ne "") {

		# 入力内容を整理
		$in{'word'} =~ s/　/ /g;
		@wd = split(/\s+/, $in{'word'});

		# 検索処理
		print "<dl>\n";
		$i=0;
		open(IN,"$logfile") || &error("Open Error : $logfile");
		$top = <IN>;
		while (<IN>) {
			$flag=0;
			foreach $wd (@wd) {
				if (index($_,$wd) >= 0) {
					$flag=1;
					if ($in{'cond'} eq 'OR') { last; }
				} else {
					if ($in{'cond'} eq 'AND') { $flag=0; last; }
				}
			}
			next if (!$flag);

			# 結果を表示
			$i++;
			($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$res,$url) = split(/<>/);
			if ($mail) { $name = "<a href=\"mailto:$mail\">$name</a>"; }
			if ($url) {
				if ($url !~ /^http/i) { $url = "http://$url"; }
				$url = "[<a href=\"$url\" target='_blank'>HOME</a>]";
			}

			print "<dt><hr>[<b>$no</b>] <b>$sub</b> ",
			"投稿者：<b>$name</b> 投稿日：$date $url<br><br><dd>$com<br>\n";
		}
		close(IN);
		print "<dt><hr>検索結果は <b>$i</b>件です。\n";
	}
	print "<dt><hr></dl>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  管理モード
#-------------------------------------------------
sub admin {
	if ($in{'pass'} ne "" && $in{'pass'} ne $pass) {
		&error("パスワードが違います");
	}

	&header;
	print "[<a href=\"$script?\">掲示板に戻る</a>]\n";

	if ($in{'pass'} eq "") {
		print "<p><center><h4>パスワードを入力して下さい</h4>\n";
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"del\">\n";
		print "<input type=password name=pass size=8>";
		print "<input type=submit value=\" 認証 \">\n";
		print "</form>\n";

	} else {

		# 削除処理
		if ($DEL[0]) {

			# ロック処理
			&lock if ($lockkey);

			# 削除情報をマッチングし更新
			@new=();
			open(IN,"$logfile") || &error("Open Error : $logfile");
			$top = <IN>;
			while (<IN>) {
				$flag=0;
				($no,$reno,$date) = split(/<>/);
				foreach $del (@DEL) {
					if ($no eq "$del" || $reno eq "$del") {
						$flag=1; last;
					}
				}
				if ($flag == 0) { push(@new,$_); }
			}
			close(IN);

			# 更新
			unshift(@new,$top);
			open(OUT,">$logfile") || &error("Write Error : $logfile");
			print OUT @new;
			close(OUT);

			# ロック解除
			&unlock if ($lockkey);
		}

		# 管理を表示
		if ($page eq "") { $page = 0; }
		print "<p><center><table><tr><td>\n";
		print "<ul><li>削除する記事のチェックボックスにチェックを入れ、削除ボタンを押して下さい。\n";
		print "<li>親記事を削除するとレス記事も一括して削除されます。</ul>\n";
		print "</td></tr></table>\n";
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=page value=\"$page\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=action value=\"$in{'action'}\">\n";
		print "<input type=submit value=\"削除する\">";
		print "<input type=reset value=\"リセット\">\n";
		print "<p><table border=0 cellspacing=1>\n";
		print "<tr><th>削除</th><th>記事NO</th><th>投稿日</th><th>タイトル</th>";
		print "<th>投稿者</th><th>URL</th><th>コメント</th><th>ホスト名</th></tr>\n";

		# ページ区切り処理
		$start = $page + 1;
		$end   = $page + $logview;

		open(IN,"$logfile") || &error("Open Error: $logfile");
		$top = <IN>;
		$i=0;
		while (<IN>) {
			($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$color,$url,$host,$pw) = split(/<>/);
			if ($reno eq "") { $i++; }
			if ($i < $start) { next; }
			if ($i > $end) { last; }

			if ($mail) { $name="<a href=\"mailto:$mail\">$name</a>"; }
			($date) = split(/\(/, $date);

			if ($url) {
				if ($url !~ /^http/i) { $url = "http://$url"; }
				$url = "<a href=\"$url\" target='_top'>Home</a>";
			} else { $url = '-'; }

			$com =~ s/<br>//ig;
			$com =~ s/</&lt;/g;
			$com =~ s/>/&gt;/g;
			if (length($com) > 50) {
				$com = substr($com,0,48);
				$com = "$com" . "...";
			}

			if ($reno eq "") { print "<tr><th colspan=8><hr></th></tr>\n"; }

			# 削除チェックボックス
			print "<tr><th><input type=checkbox name=del value=\"$no\"></th>";
			print "<td align=center>$no</td>";
			print "<td><small>$date</small></td><th>$sub</th><th>$name</th>";
			print "<td align=center>$url</td><td><small>$com</small></td>";
			print "<td><small>$host</small></td></tr>\n";

		}
		close(IN);

		print "<tr><th colspan=8><hr></th></tr>\n";
		print "</table></form>\n";
	}

	$next_page = $page + $logview;
	$back_page = $page - $logview;

	print "<p><table cellspacing=0 cellpadding=0><tr>\n";
	if ($back_page >= 0) {
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=page value=\"$back_page\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"$in{'action'}\">\n";
		print "<input type=submit value=\"前の$logview組\">\n";
		print "</td></form>\n";
	}
	if ($next_page < $i) {
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=page value=\"$next_page\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"$in{'action'}\">\n";
		print "<input type=submit value=\"次の$logview組\">\n";
		print "</td></form>\n";
	}
	print "</tr></table></center>\n";
	print "</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  返信レスフォーム
#-------------------------------------------------
sub res_msg {
	&header;
	print <<"EOM";
[<a href="javascript:history.back()">掲示板に戻る</a>]<hr>
<blockquote>
EOM

	$f=0;
	open(IN,"$logfile") || &error("Open Error : $logfile");
	$top = <IN>;
	while (<IN>) {
		($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$color,$url,$host,$pw) = split(/<>/);
		if ($in{'no'} == $no && $reno) { $f++; }
		if ($in{'no'} eq $no || $in{'no'} eq $reno) {

			if ($mail) { $name = "<a href=\"mailto:$mail\">$name</a>"; }
			if ($url)  { $url  = "&lt;<a href=\"http://$url\" target='_top'>Home</a>&gt;"; }
			# レス題名用
			if ($reno eq "") { $res_sub = "Re: $sub"; }

			print "<font color=\"$onepnt\"><b>$sub</b></font> <b>$name</b> - $date $url<p>\n";
			print "<blockquote>$com</blockquote><hr>\n";
		}
	}
	close(IN);
	if ($f) { &error("不正な返信要求です"); }

	&form_view("$in{'no'}");
	print "</blockquote>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  留意事項
#-------------------------------------------------
sub howto {
	&header;
	print <<EOM;
<br><br>
<div align="center">
<table border=1 cellpadding=10 align=center width="90%">
<tr><td bgcolor="#FFFFFF">
<font color="#000000">
<h3 style="color:$t_color">留意事項</h3>
<ol>
<li>この掲示板は<b>クッキー対応</b>です。１度記事を投稿いただくと、おなまえ、Ｅメール、ＵＲＬ、削除キーの情報は２回目以降は自動入力されます。（ただし利用者のブラウザがクッキー対応の場合）
<li>投稿記事には、<b>タグは一切使用できません。</b>
EOM
	if ($in_email) {
		print "<li>記事を投稿する上での必須入力項目は<b>「おなまえ」「メッセージ」「Ｅメール」</b>です。ＵＲＬと削除キーは任意です。\n";
	} else {
		print "<li>記事を投稿する上での必須入力項目は<b>「おなまえ」</b>と<b>「メッセージ」</b>です。Ｅメール、ＵＲＬ、削除キーは任意です。\n";
	}

	print <<EOM;
<li>記事には、<b>半角カナは一切使用しないで下さい。</b>文字化けの原因となります。
<li>記事の投稿時に<b>「削除キー」</b>にパスワード（英数字で8文字以内）を入れておくと、その記事は次回<b>削除キー</b>によって削除することができます。
<li>記事の保持件数は<b>最大 $max件</b>です。それを超えると古い順に自動削除されます。
<li>過去の投稿記事から<b>「キーワード」によって簡易検索ができます。</b>トップメニューの<a href="$script?mode=find">「ワード検索」</a>のリンクをクリックすると検索モードとなります。
<li>管理者が著しく不利益と判断する記事や他人を誹謗中傷する記事は予\告なく削除することがあります。
</ol>
</font>
</td></tr></table>
<p>
<form>
<input type=button value="前画面に戻る" onClick="history.back()">
</form>
</body>
</html>
EOM
exit;
}

#-------------------------------------------------
#  ユーザ記事削除
#-------------------------------------------------
sub usrdel {
	# 投稿チェック
	if ($postonly && !$post_flag) { &error("不正なアクセスです"); }
	if ($baseUrl) { &refCheck; }

	if ($in{'no'} eq '' || $in{'pwd'} eq '') {
		&error("削除Noまたは削除キーが入力モレです");
	}

	# ロック処理
	&lock if ($lockkey);

	open(IN,"$logfile") || &error("Open Error : $logfile");
	@lines = <IN>;
	close(IN);
	$top = shift(@lines);

	$flag=0;
	foreach (@lines) {
		($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$color,$url,$host,$pw) = split(/<>/);
		if ($flag == 0 && $in{'no'} eq $no) {
			$PW = $pw;
			if ($reno eq "") { $flag=2; }
			else { $flag=1; }
		}
		elsif ($flag == 2 && $in{'no'} eq $reno) { next; }
		else { push(@new,$_); }
	}

	if ($flag == 0) { &error("該当記事が見当たりません"); }
	if ($PW eq '') { &error("該当記事には削除キーが設定されていません"); }

	# 削除キーを照合
	$check = &decrypt($in{'pwd'}, $PW);
	if ($check != 1) { &error("削除キーが違います"); }
	else {
		# 更新
		unshift(@new,$top);
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);
	}
}

#-------------------------------------------------
#  デコード処理
#-------------------------------------------------
sub decode {
	local($buf, $key, $val);

	$post_flag=0;
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		$post_flag=1;
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &error("投稿量が大きすぎます"); }
		read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
	} else {
		$buf = $ENV{'QUERY_STRING'};
	}

	foreach ( split(/&/, $buf) ) {
		($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

		# S-JISコード変換
		&jcode'convert(*val, "sjis", "", "z");

		# タグ処理
		$val =~ s/&/&amp;/g;
		$val =~ s/"/&quot;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;

		# 改行処理
		if ($key eq 'comment') {
			$val =~ s/\r\n/<br>/g;
			$val =~ s/\r/<br>/g;
			$val =~ s/\n/<br>/g;
		} else {
			$val =~ s/\r//g;
			$val =~ s/\n//g;
		}

		# 削除情報
		if ($key eq 'del') { push(@DEL,$val); }

		$in{$key} = $val;
	}
	if ($in{'sub'} eq "") { $in{'sub'} = "無題"; }
	$mode = $in{'mode'};
	$page = $in{'page'};

	# 日時の取得
	$ENV{'TZ'} = "JST-9";
	$times = time;
	($min,$hour,$mday,$mon,$year,$wday) = (localtime($times))[1..6];

	# 日時のフォーマット
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
	$date = sprintf("%04d\/%02d\/%02d(%s) %02d\:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min);
}

#--------------#
#  HTMLヘッダ  #
#--------------#
sub header {
	$headflag = 1;
	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<STYLE TYPE="text/css">
<!--
body,tr,td,th { font-size:$b_size }
a:hover { color:$alink }
span { font-size:$t_point }
big { font-size:12pt }
small { font-size:9pt }
-->
</STYLE>
<title>$title</title></head>
<body background="$bgrnd" bgcolor="$bgcol" text="$text" link="$link" vlink="$vlink" alink="$alink">
EOM
}

#-------------------------------------------------
#  エラー処理
#-------------------------------------------------
sub error {
	&unlock if ($lockflag);

	&header if (!$headflag);
	print <<EOM;
<div align="center">
<hr width=400>
<h3>ERROR !</h3>
<font color="#dd0000">$_[0]</font>
<p>
<hr width=400>
<form>
<input type=button value="前画面に戻る" onClick="history.back()">
</form>
</div>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  クッキー発行
#-------------------------------------------------
sub set_cookie {
	local(@cook) = @_;
	local($gmt, $cook, @t, @m, @w);

	@t = gmtime(time + 60*24*60*60);
	@m = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	@w = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# 国際標準時を定義
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$w[$t[6]], $t[3], $m[$t[4]], $t[5]+1900, $t[2], $t[1], $t[0]);

	# 保存データをURLエンコード
	foreach (@cook) {
		s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		$cook .= "$_<>";
	}

	# 格納
	print "Set-Cookie: HoneyBoard=$cook; expires=$gmt\n";
}

#-------------------------------------------------
#  クッキー取得
#-------------------------------------------------
sub get_cookie {
	local($key, $val, *cook);

	# クッキーを取得
	$cook = $ENV{'HTTP_COOKIE'};

	# 該当IDを取り出す
	foreach ( split(/;/, $cook) ) {
		($key, $val) = split(/=/);
		$key =~ s/\s//g;
		$cook{$key} = $val;
	}

	# データをURLデコードして復元
	foreach ( split(/<>/, $cook{'HoneyBoard'}) ) {
		s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("H2", $1)/eg;

		push(@cook,$_);
	}
	return (@cook);
}

#-------------------------------------------------
#  パスワード暗号処理
#-------------------------------------------------
sub encrypt {
	local($in) = @_;
	local($salt, $enc, @s);

	@s = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
	srand;
	$salt = $s[int(rand(@s))] . $s[int(rand(@s))];
	$enc = crypt($in, $salt) || crypt ($in, '$1$' . $salt);
	$enc;
}

#-------------------------------------------------
#  パスワード照合処理
#-------------------------------------------------
sub decrypt {
	local($in, $dec) = @_;

	local $salt = $dec =~ /^\$1\$(.*)\$/ && $1 || substr($dec, 0, 2);
	if (crypt($in, $salt) eq $dec || crypt($in, '$1$' . $salt) eq $dec) {
		return (1);
	} else {
		return (0);
	}
}

#-------------------------------------------------
#  ロック処理
#-------------------------------------------------
sub lock {
	local($retry)=5;

	# 古いロックは削除
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	# symlink関数式ロック
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}

	# mkdir関数式ロック
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag=1;
}

#-------------------------------------------------
#  ロック解除
#-------------------------------------------------
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }

	$lockflag=0;
}

#-------------------------------------------------
#  メール送信
#-------------------------------------------------
sub mail_to {
	local($com, $msub, $mbody);

	# メールタイトルを定義
	$msub = &base64("[$title : $no] $in{'sub'}");

	# 記事復元
	$com  = $in{'comment'};
	$com =~ s/<br>/\n/g;
	$com =~ s/&lt;/</g;
	$com =~ s/&gt;/>/g;
	$com =~ s/&quot;/"/g;
	$com =~ s/&amp;/&/g;

	# メール本文を定義
	$mbody = <<"EOM";
投稿日時：$date
ホスト名：$host
ブラウザ：$ENV{'HTTP_USER_AGENT'}

投稿者名：$in{'name'}
Ｅメール：$in{'email'}
ＵＲＬ  ：$in{'url'}
タイトル：$in{'sub'}

$com
EOM

	# sendmail起動
	if ($in{'email'} eq "") { $email = $mailto; }
	else { $email = $in{'email'}; }

	open(MAIL,"| $sendmail -t");
	print MAIL "To: $mailto\n";
	print MAIL "From: $email\n";
	print MAIL "Subject: $msub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	foreach ( split(/\n/, $mbody) ) {
		&jcode'convert(*_, 'jis', 'sjis');
		print MAIL $_, "\n";
	}
	close(MAIL);
}

#-------------------------------------------------
#  BASE64変換
#-------------------------------------------------
#	とほほのWWW入門で公開されているルーチンを
#	参考にしました。( http://tohoho.wakusei.ne.jp/ )
sub base64 {
	local($sub) = @_;
	&jcode'convert(*sub, 'jis', 'sjis');

	$sub =~ s/\x1b\x28\x42/\x1b\x28\x4a/g;
	$sub = "=?iso-2022-jp?B?" . &b64enc($sub) . "?=";
	$sub;
}
sub b64enc {
	local($ch)="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	local($x, $y, $z, $i);
	$x = unpack("B*", $_[0]);
	for ($i=0; $y=substr($x,$i,6); $i+=6) {
		$z .= substr($ch, ord(pack("B*", "00" . $y)), 1);
		if (length($y) == 2) {
			$z .= "==";
		} elsif (length($y) == 4) {
			$z .= "=";
		}
	}
	$z;
}

#-------------------------------------------------
#  イメージ表示
#-------------------------------------------------
sub image {
	local($i,$j,$stop);

	&header;
	print "<center><hr width=\"75%\">\n";
	print "<b>画像イメージ</b>\n";
	print "<p>- 現在登録されている画像イメージは以下のとおりです -\n";
	print "<hr width=\"75%\">\n";
	print "<p><table border=1 cellpadding=5 cellspacing=0><tr>\n";

	$i=0; $j=0;
	$stop = @icon1;
	foreach (0 .. $#icon1) {
		$i++; $j++;
		print "<th><img src=\"$imgurl/$icon1[$_]\" ALIGN=middle alt=\"$icon1[$_]\"> $icon2[$_]</th>\n";
		if ($j != $stop && $i >= 5) { print "</tr><tr>\n"; $i=0; }
		elsif ($j == $stop) {
			if ($i == 0) { last; }
			while ($i < 5) { print "<th><br></th>"; $i++; }
		}
	}

	print "</tr></table><br>\n";
	print "<form><input type=button value=' CLOSE ' onClick='top.close();'></form>\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  自動リンク
#-------------------------------------------------
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\=\@\;\#\:\%]+)/$1<a href=\"$2\" target='_top'>$2<\/a>/g;
}

#-------------------------------------------------
#  投稿フォーム
#-------------------------------------------------
sub form_view {
	# クッキー情報を取得
	local($cnam,$ceml,$curl,$cpwd,$ccol,$cico) = &get_cookie;
	if ($curl eq "") { $curl = 'http://'; }

	print "<form action=\"$script\" method=\"POST\">\n";
	if ($mode eq "res") {
		print "<input type=hidden name=reno value=\"$_[0]\">\n";
	}

	print <<"EOM";
<input type=hidden name=mode value="regist">
<table>
<tr>
  <td><b>おなまえ</b></td>
  <td><input type=text name=name size=28 value="$cnam"></td>
</tr>
<tr>
  <td><b>Ｅメール</b></td>
  <td><input type=text name=email size=28 value="$ceml"></td>
</tr>
<tr>
  <td><b>タイトル</b></td>
  <td>
    <input type=text name=sub size=34 value="$res_sub">
    &nbsp;
    <input type=submit value="送信する"><input type=reset value="リセット">
  </td>
</tr>
<tr>
  <td colspan=2>
    <b>メッセージ</b><br>
    <textarea name=comment cols=55 rows=7 wrap=soft></textarea>
  </td>
</tr>
<tr>
<tr>
  <td><b>参照先</b></td>
  <td><input type=text name=url size=50 value="$curl"></td>
</tr>
<tr>
  <td><b>イメージ</b></td>
  <td><select name=icon>
EOM
	# イメージの選択フォームを表示
	push(@icon1,"$mgr_icon");
	push(@icon2,"管理者用");
	foreach (0 .. $#icon1) {
		if ($icon1[$_] eq $cico) {
			print "<option value=\"$icon1[$_]\" selected>$icon2[$_]\n";
		} else {
			print "<option value=\"$icon1[$_]\">$icon2[$_]\n";
		}
	}

	print <<"EOM";
    </select> [<a href="$script?mode=image" target="_blank">アイコン参照</a>]
  </td>
</tr>
<tr>
  <td><b>削除キー</b></td>
  <td><input type=password name=pwd size=6 maxlength=8 value="$cpwd">
    <small>(記事の削除時に使用)</small>
  </td>
</tr>
<tr>
  <td><b>文字色</b></td>
  <td>
EOM

	if ($ccol eq "") { $ccol = $colors[0]; }
	foreach (0 .. $#colors) {
		if ($ccol eq "$colors[$_]") {
			print "<input type=radio name=color value=\"$colors[$_]\" checked>";
			print "<font color=\"$colors[$_]\">■</font> \n";
		} else {
			print "<input type=radio name=color value=\"$colors[$_]\">";
			print "<font color=\"$colors[$_]\">■</font> \n";
		}
	}

	if ($_[0]) {
		print "<input type=hidden name=no value=\"$_[0]\">\n";
	}

	print "</td></tr><tr><td></td><td>\n";
	print "<input type=checkbox name=cook value=\"on\" checked> ";
	print "クッキーを保存\n";
	print "</td></tr></table>\n</form>\n";
}

#-------------------------------------------------
#  REFチェック
#-------------------------------------------------
sub refCheck {
	local($ref) = $ENV{'HTTP_REFERER'};
	$ref =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

	$baseUrl =~ s/(\W)/\\$1/g;
	if ($ref && $ref !~ /$baseUrl/i) { &error("不正なアクセスです"); }
}

#-------------------------------------------------
#  チェックモード
#-------------------------------------------------
sub check {
	&header;
	print "<h2>Check Mode</h2>\n";
	print "<ul>\n";

	# ログパス
	if (-e $logfile) {
		print "<li>ログファイルのパス：OK\n";
		# ログパーミッション
		if (-r $logfile && -w $logfile) {
			print "<li>ログファイルのパーミッション：OK\n";
		} else { print "<li>ログファイルのパーミッション：NG\n"; }
	} else { print "<li>ログファイルのパス：NG → $logfile\n"; }

	# ロックディレクトリ
	print "<li>ロック形式：";
	if ($lockkey == 0) { print "ロック設定なし\n"; }
	else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }
		($lockdir) = $lockfile =~ /(.*)[\\\/].*$/;
		print "<li>ロックディレクトリ：$lockdir\n";

		if (-d $lockdir) {
			print "<li>ロックディレクトリのパス：OK\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<li>ロックディレクトリのパーミッション：OK\n";
			} else {
				print "<li>ロックディレクトリのパーミッション：NG → $lockdir\n";
			}
		} else { print "<li>ロックディレクトリのパス：NG → $lockdir\n"; }
	}
	print "</ul>\n</body>\n</html>\n";
	exit;
}


__END__

