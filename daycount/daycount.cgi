#!/usr/bin/perl

#┌─────────────────────────────────
#│ DAY COUNTER v2.6 (2002/08/02)
#│ Copyright(C) KENT WEB 1997-2002
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────
$ver = 'DAY COUNTER v2.6';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問は一切お受けいたしておりません。
#└─────────────────────────────────
#
# [ ディレクトリ構成例 ]
#
#  public_html / index.html (ホームディレクトリ）
#       |
#       +-- daycount / daycount.cgi [755]
#              |       daycount.dat [666]
#              |       gifcat.pl    [644]
#              |
#              +-- gif1 / 0.gif, 1.gif, ..... 9.gif
#              |
#              +-- gif2 / 0.gif, 1.gif, ..... 9.gif
#              |
#              +-- lock [777] /
#
#
# [ タグの書き方の例 ]
#
#  総カウント数 	<img src="パス/daycount.cgi?gif">
#  本日のカウント数 	<img src="パス/daycount.cgi?today">
#  昨日　　〃		<img src="パス/daycount.cgi?yes">
#
#  ▼動作チェックのしかた (ブラウザから最後に ?check をつけて呼出す）
#    http://～～/daycount.cgi?check

#============#
#  設定項目  #
#============#

# 画像連結ライブラリ取込み
require './gifcat.pl';

# 総カウント数の桁数
$digit1 = 5;

# 本/昨日カウント数の桁数
$digit2 = 3;

# 記録ファイル
$logfile = './daycount.dat';

# 総カウント用GIF画像のディレクトリ
#  --> フルパスだと / から始るパス
$gifdir1 = './gif1';

# 本/昨日カウント用GIF画像のディレクトリ
#  --> フルパスだと / から始るパス
$gifdir2 = './gif2';

# IPアドレスの二重カウントチェック
#   0 : チェックしない
#   1 : チェックする
$ip_check = 1;

# ファイルロック形式
#  → 0=no 1=symlink関数 2=mkdir関数
$lockkey = 2;

# ロックファイル名
$lockfile = './lock/daycount.lock';

# カウンタの機能タイプ
#   0 : 総カウント数不要（昨日／本日のみ）
#   1 : 標準タイプ
$type = 1;

#============#
#  設定完了  #
#============#

# 引数を解釈
$mode = $ENV{'QUERY_STRING'};
$mode =~ s/\W//g;

# チェックモード
if (!$mode || $mode eq 'check') { &check; }

# 更新系処理でないならば1秒待たせる
if ($type == 1 && $mode ne "gif") { sleep(1); }
elsif ($type == 0 && $mode eq "yes") { sleep(1); }

# ロック開始
$lockflag=0;
if (($type == 1 && $mode eq "gif" && $lockkey) || ($type == 0 && $mode eq "today" && $lockkey)) { &lock; $lockflag=1; }

# 記録ファイルから読み込み
open(IN,"$logfile") || &error("LK");
$data = <IN>;
close(IN);

# 記録ファイルを分解
($key,$yes,$today,$count,$ip) = split(/<>/, $data);

# 日時を取得
$ENV{'TZ'} = "JST-9";
($mday) = (localtime(time))[3];

# IPチェック
$flag=0;
if ($ip_check) {
	$addr = $ENV{'REMOTE_ADDR'};
	if ($addr eq $ip) { $flag=1; }
}

# 本日のカウント数をキーにしてカウントアップ
if ((!$flag && $type && $mode eq "gif") || (!$flag && !$type && $mode eq "today")) {

	if ($key eq "$mday") { $today++; }
	else {
		$yes   = $today;
		$today = 1;
	}

	# カウントアップ処理
	$count++;

	# 記録ファイルを更新する
	$data = "$mday<>$yes<>$today<>$count<>$addr<>";
	open(OUT,">$logfile") || &error("LK");
	print OUT $data;
	close(OUT);
}

# ロック解除
if ($lockflag) { &unlock; }

# 画像表示
&count_view;
exit;

#-------------------#
# カウンタ出力処理  #
#-------------------#
sub count_view {
	local($length, $fig, $n, $gifdir, @GIF);
	if ($mode eq "gif") {
		$fig = $digit1;
		$gifdir = $gifdir1;
	} else {
		$fig = $digit2;
		$gifdir = $gifdir2;
		if ($mode eq "today") { $count = $today; }
		else { $count = $yes; }
	}

	# 表示画像を配列化
	while (length($count) < $fig) { $count = '0' . $count; }
	$length = length($count);
	@GIF=();
	foreach (0 .. $length-1) {
		$n = substr($count,$_,1);
		push(@GIF, "$gifdir/$n\.gif");
	}

	# 連結画像を出力
	print "Content-type: image/gif\n\n";
	binmode(STDOUT);
	print &gifcat'gifcat(@GIF);
}

#--------------#
#  ロック処理  #
#--------------#
sub lock {
	local($retry)=5;
	# 1分以上古いロックは削除する
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime && $mtime < time - 60) { &unlock; }
	}
	# symlink関数式ロック
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error; }
			sleep(1);
		}
	# mkdir関数式ロック
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error; }
			sleep(1);
		}
	}
	$lockflag=1;
}

#--------------#
#  ロック解除  #
#--------------#
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }
	$lockflag=0;
}

#--------------#
#  エラー処理  #
#--------------#
sub error {
	local($data, @err);

	if ($lockflag) { &unlock; }

	@err = ('47','49','46','38','39','61','2d','00','0f','00','80','00','00','00','00','00','ff','ff','ff','2c', '00','00','00','00','2d','00','0f','00','00','02','49','8c','8f','a9','cb','ed','0f','a3','9c','34', '81','7b','03','ce','7a','23','7c','6c','00','c4','19','5c','76','8e','dd','ca','96','8c','9b','b6', '63','89','aa','ee','22','ca','3a','3d','db','6a','03','f3','74','40','ac','55','ee','11','dc','f9', '42','bd','22','f0','a7','34','2d','63','4e','9c','87','c7','93','fe','b2','95','ae','f7','0b','0e', '8b','c7','de','02','00','3b');

	print "Content-type: image/gif\n\n";
	foreach (@err) {
		$data = pack('C*',hex($_));
		print $data;
	}
	exit;
}

#------------------#
#  チェックモード  #
#------------------#
sub check {
	print "Content-type: text/html\n\n";
	print "<html><head><title>DAY COUNTER</title></head>\n";
	print "<body>\n<h2>Check Mode</h2>\n<UL>\n";

	# ログファイルのパス確認
	if (-e $logfile) {
		print "<LI>ログファイルのパス : OK!\n";
		# ログファイルのパーミッション
		if (-r $logfile && -w $logfile) {
			print "<LI>ログファイルのパーミッション : OK!\n";
		} else {
			print "<LI>ログファイルのパーミッション : NG → $logfile\n";
		}
	} else { print "<LI>ログファイルのパス : NG → $logfile\n"; }

	# 画像ディレクトリ
	foreach ($gifdir1, $gifdir2) {
		# ディレクトリパス確認
		if (-d $_) { print "<LI>画像ディレクトリパス ( $_ ) : OK!\n"; }
		else { print "<LI>画像ディレクトリのパス : NG → $_\n"; }

		# 画像チェック
		foreach $i (0 .. 9) {
			if (-e "$_\/$i\.gif") {
				print "<LI>画像 : $_\/$i\.gif → OK!\n";
			} else {
				print "<LI>画像 : $_\/$i\.gif → NG!\n";
			}
		}
	}

	# ロックディレクトリ
	print "<LI>ロック形式：";
	if ($lockkey == 0) { print "ロック設定なし\n"; }
	else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }
		$lockfile =~ s/(.*)[\\\/].*$/$lockdir = $1/e;
		print "<LI>ロックディレクトリ：$lockdir\n";

		if (-d $lockdir) {
			print "<LI>ロックディレクトリのパス：OK\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<LI>ロックディレクトリのパーミッション：OK\n";
			} else {
				print "<LI>ロックディレクトリのパーミッション：NG → $lockdir\n";
			}
		} else { print "<LI>ロックディレクトリのパス：NG → $lockdir\n"; }
	}

	# 著作権表示：削除禁止
	print "<P><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/'>Day Counter</a> -\n";
	print "</UL>\n</small>\n</body></html>\n";
	exit;
}

__END__

