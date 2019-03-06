#!/usr/bin/perl

#��������������������������������������������������������������������
#�� Honey Board v2.1 - 2004/02/06
#�� Copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'Honey Board v2.1';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������
#
# �y�t�@�C���\����z
#
#  public_html (�z�[���f�B���N�g��)
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
# [ �`�F�b�N���[�h�̎d�� ] : mode=check �Ƃ���������t���Čďo��
#
#  ��  http://�`�`/honey.cgi?mode=check

#-------------------------------------------------
#  ��{�ݒ�
#-------------------------------------------------

# �����R�[�h���C�u�����捞��
require './jcode.pl';

# �^�C�g����
$title = "Honey Board";

# �^�C�g�������̐F
$t_color = "#DD0000";

# �^�C�g�������̃^�C�v
$t_face = "�l�r �o�S�V�b�N";

# �^�C�g�������T�C�Y
$t_point = '24px';

# �{���̕����T�C�Y
$b_size = '13px';

# �X�N���v�g��
$script = './honey.cgi';

# ���O�t�@�C����
$logfile = './honeylog.cgi';

# �Ǘ��p�p�X���[�h
$pass = '1202';

# �ő�L�����i����𒴂���L���͌Â����ɍ폜����܂��j
$max = 50;

# �߂��
$home = "../index.html";

# �摜�i�[�f�B���N�g��
# �� �t���p�X�Ȃ� http:// ����L�q����
# �� �Ō�� / ����Ȃ�
$imgurl = "./img";

# �w�i�F�A�����F
$bgrnd = "";		# �ǎ�
$bgcol = "#FFFFFF";	# �w�i�F
$text  = "#452815";	# �����F
$link  = "#0000FF";	# �����N�F�F���K��
$vlink = "#800080";	# �����N�F�F���K��
$alink = "#DD0000";	# �����N�F�F�K�⒆

# �L���^�C�g���F / �L��No�̐F
$onepnt = "#008000";

# �����F
@colors = ('#800000','#DF0000','#008040','#0000FF','#C100C1','#FF80C0','#FF8040','#000080');

# �d���[���A�h���X�̕K�{���� (0=no 1=yes)
$in_email = 0;

# �L���̍X�V�� method=POST ���� (0=no 1=yes)
#  --> �A�����e�Ȃǂ̍r�炵�΍�
$postonly = 1;

# ����IP�A�h���X����̘A�����e���ԁi�b���j
#  --> �A�����e�Ȃǂ̍r�炵�΍�
#  --> �l�� 0 �ɂ���Ƃ��̋@�\�͖����ɂȂ�܂�
$wait = 60;

# URL�̎��������N (0=no 1=yes)
$autolink = 1;

# �P�y�[�W������̋L���\������
$logview = 7;

# ���X��������c���[���g�b�v�ֈړ� (0=no 1=yes)
$top_sort = 1;

# ���b�N�t�@�C���@�\ (0=no 1=symlink�֐� 2=mkdir�֐�)
$lockkey = 2;

# ���b�N�t�@�C����
$lockfile = "./lock/honey.lock";

# ���[���ʒm�@�\
#  --> 0 : no
#  --> 1 : yes �����̓��e�L�������[���ʒm����
#  --> 2 : yes �����̓��e�L���̓��[���ʒm���Ȃ�
$mailing = 0;

# sendmail�̃p�X�i���[���ʒm����ꍇ�j
$sendmail = '/usr/lib/sendmail';

# ���[���ʒm��A�h���X�i���[���ʒm����ꍇ�j
$mailto = 'xxx@xxx.xxx';

# �L�����N�^���w��i�㉺�̔z��̓y�A��)
@icon1 = (
	'cake1.gif','aomusi.gif','budo.gif','cake2.gif','flyingrabi.gif',
	'icon07.png','icon8.gif','icon08.png','icon9.png','kame.gif','kata.gif',
	'ken.jpg','lespaul_ys120.gif','mm120.gif','neko.gif','strato.gif','robo1-3-4.gif');
@icon2 = (
	'�P�[�L','�����ނ�','�Ԃǂ�','�P�[�L�Q','��ԃE�T�M',
	'OL��1','OL��2','OL��3','������','�J��','�J�^�c����',
	'�P�������','���X�|�[��','�~���[�W�b�N�}��','�׋��l�R','�X�g���g','���{');

# �Ǘ��җp�A�C�R��
#  --> �Ǘ��A�C�R�����w�肷��ꍇ�́u�폜�L�[�v���ɊǗ��p�p�X���[�h��
#      �����ɓ��͂���K�v������܂��B
$mgr_icon = "master.gif";

# �^�O�L���}���I�v�V����
#   �� <!-- �㕔 --> <!-- ���� --> �̑���Ɂu�L���^�O�v��}������B
#   �� �L���^�O�ȊO�ɁAMIDI�^�O �� LimeCounter���̃^�O�ɂ��g�p�\�ł��B
$banner1 = '<!-- �㕔 -->';	# �f���㕔�ɑ}��
$banner2 = '<!-- ���� -->';	# �f�������ɑ}��

# �A�N�Z�X�����i���p�X�y�[�X�ŋ�؂�j
#  �� ���ۂ���z�X�g������IP�A�h���X���L�q�i�A�X�^���X�N�j
#  �� �L�q�� $deny = '*.anonymizer.com 211.154.120.*';
$deny = '70.86.213.16 82.209.225.* 193.201.103.80 204.113.91.19 210.165.203.83 219.102.48.50 66.117.48.64 212.98.168.142 82.209.247.139 81.216.80.40 216.130.157.51 194.126.200.17 210.165.203.* 211.193.148.80 210.105.108.155 157.181.162.22 61.32.96.145 203.194.209.* 213.249.155.239';

# �^�C�g���摜���g���ꍇ
#  --> �摜URL�� http:// ����L�q
$ImgT = "";
$ImgW = 150;  # �摜����
$ImgH = 50;   # �摜�c��

# ���e��̏���
#  �� �f�����g��URL���L�q���Ă����ƁA���e�ナ���[�h���܂�
#  �� �u���E�U���ēǂݍ��݂��Ă���d���e����Ȃ��[�u�B
#  �� Location�w�b�_�̎g�p�\�ȃT�[�o�̂�
$location = '';

# �z�X�g�擾���@
# 0 : gethostbyaddr�֐����g��Ȃ�
# 1 : gethostbyaddr�֐����g��
$gethostbyaddr = 0;

# ���T�C�g���瓊�e�r�����Ɏw�肷��ꍇ�i�Z�L�����e�B�΍�j
#  �� �f����URL��http://���珑��
$baseUrl = '';

# �e�L���̐��o�F
# �� ���ɁA�u���v�u���n�F�v�u�摜�t�@�C�����v
$oyaWid = 500;
$oyaCol = "#E7FFFF";
@oyaCol = ("bl1.gif","bl2.gif","bl3.gif","bl4.gif","bl5.gif","bl6.gif");

# ���X�L���̐��o�F
# �� ���ɁA�u���v�u���n�F�v�u�摜�t�@�C�����v
$resWid = 380;
$resCol = "#EFEFEF";
@resCol = ("lg1.gif","lg2.gif","lg3.gif","lg4.gif","lg5.gif","lg6.gif");

#-------------------------------------------------
#  �ݒ芮��
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
#  �A�N�Z�X����
#-------------------------------------------------
sub axscheck {
	# �z�X�g���擾
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
	if ($flag) { &error("�A�N�Z�X��������Ă��܂���"); }
}

#-------------------------------------------------
#  �L���\������
#-------------------------------------------------
sub html {
	local($no,$reno,$date,$name,$eml,$sub,$icon,$icon2,
		$com,$color,$url,$host,$pw,$i,$top,$next,$back);

	# �w�b�_
	&header;
	print "<div align=center>\n";
	if ($banner1 ne "<!-- �㕔 -->") { print "$banner1\n<p>\n"; }

	# �^�C�g����
	if ($ImgT) {
		print "<img src=\"$ImgT\" width=$ImgW height=$ImgH alt=\"$title\">\n";
	} else {
		print "<font color=\"$t_color\" face=\"$t_face\" size=5\"><b><span>$title</span></b></font>\n";
	}

	print <<EOM;
<hr width="530">
[<a href="$home" target="_top">�g�b�v�ɖ߂�</a>]
[<a href="$script?mode=howto">���ӎ���</a>]
[<a href="$script?mode=find">���[�h����</a>]
[<a href="$script?mode=admin">�Ǘ��p</a>]
<hr width="530">
EOM

	# �t�H�[����\��
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

		# �P�}�X�̑傫��
		$pix = 18;

		# ���X�L��
		if ($reno) {
			$wide = $resWid;
			$iro  = $resCol;
			@gif  = ("",@resCol);

		# �e�L��
		} else {
			$wide = $oyaWid;
			$iro  = $oyaCol;
			@gif  = ("",@oyaCol);
		}

		# �L����\��
		if (!$reno) { print "<br><br>\n"; }
		print "<TABLE BORDER=0><TR>\n";

		# ���]�Ώە���1
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

		# ���]�Ώە���2
		if ($flag == 0) {
			print "</tr>";
			print "<tr><td><img src=\"$imgurl/$gif[5]\" width=$pix height=$pix></td>\n";
		} else {
			print "<td width=$pix><br></td></tr>\n<tr>\n";
		}

		print "<td bgcolor=\"$iro\"><br></td>\n";
		print "<td width=\"$wide\" bgcolor=\"$iro\">\n";
		print "<font color=\"$onepnt\"><b>$sub</b></font><br>\n";
		if (!$reno) { print "���e�ҁF"; }
		print "<b>$name</b> - $date <font color=\"$onepnt\">No\.$no</font> ";

		if (!$reno) {
			print "[<a href=\"$script?mode=res&no=$no\">�ԐM</a>] &nbsp; \n";
		}

		print "$url<br>\n";
		print "<blockquote><font color=\"$color\">$com</font></blockquote>\n";
		print "</td><td bgcolor=\"$iro\"><br></td>\n";

		if ($flag == 1) {
			print "<td><img src=\"$imgurl/$gif[6]\" width=$pix height=$pix></td>\n";
		}
		print "</tr><tr>\n";

		# ���]�Ώە���3
		if ($flag == 0) { print "<td width=$pix><br></td>\n"; }

		print "<td><img src=\"$imgurl/$gif[4]\" width=$pix height=$pix></td>\n";
		print "<td width=\"$wide\" bgcolor=\"$iro\">�@</td>\n";
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
		print "<input type=submit value=\"�O��$logview��\"></td></form>\n";
	}
	if ($next < $i) {
		print "<td><form action=\"$script\">\n";
		print "<input type=hidden name=page value=\"$next\">\n";
		print "<input type=submit value=\"����$logview��\"></td></form>\n";
	}
	print "</tr></table>\n";
	print "<table align=right><tr>\n";
	print "<td nowrap align=center><form action=\"$script\" method=\"POST\">\n";
	print "<input type=hidden name=mode value=\"usrdel\">\n";
	print "�L��No<input type=text name=no size=3>\n";
	print "�폜�L�[<input type=password name=pwd size=4 maxlength=8>\n";
	print "<input type=submit value=\"�폜\"></form></td>\n";
	print "</tr></table></blockquote><br clear=all>\n";

	# ���쌠�\���i�폜�s�j
	print "<div align=center>$banner2<p><!-- $ver -->\n";
	print "<span style='font-size:10px;font-family:Verdana,Helvetica,Arial'>\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Honey Board</a> -\n";
	print "</span></div>\n</body></html>\n";
	exit;
}

#-------------------------------------------------
#  �������ݏ���
#-------------------------------------------------
sub regist {
	# ���e�`�F�b�N
	if ($postonly && !$post_flag) { &error("�s���ȃA�N�Z�X�ł�"); }
	if ($baseUrl) { &refCheck; }

	# �t�H�[�����e���`�F�b�N
	if ($in{'name'} eq "") { &error("���O�����͂���Ă��܂���"); }
	if ($in{'comment'} eq "") { &error("�R�����g�����͂���Ă��܂���"); }
	if ($in_email && $in{'email'} !~ /[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,5}$/) {
		&error("���[���A�h���X�̓��͂��s���ł�");
	}
	if ($in{'url'} eq "http://") { $in{'url'} = ''; }

	# �Ǘ��҃A�C�R������
	if ($in{'icon'} eq $mgr_icon && $in{'pwd'} ne $pass) {
		&error("�Ǘ��҃A�C�R���͊Ǘ��҈ȊO�͎g�p�ł��܂���");
	}

	# ���b�N����
	&lock if ($lockkey);

	open(IN,"$logfile") || &error("Open Error: $logfile");
	@lines = <IN>;
	close(IN);

	# �L��NO����
	$top = shift(@lines);
	($no,$ip,$time2) = split(/<>/, $top);
	$no++;

	# �A�����e�`�F�b�N
	if ($addr eq $ip && $wait > $times - $time2)
		{ &error("�A�����e�͂������΂炭���Ԃ������ĉ�����"); }

	# �폜�L�[���Í���
	if ($in{'pwd'} ne "") { $PW = &encrypt("$in{'pwd'}"); }

	# URL���������N
	if ($autolink) { &auto_link($in{'comment'}); }

	# �e�L���̏ꍇ
	if ($in{'reno'} eq "") {

		# �ő�L��������
		while ($max <= @lines) { pop(@lines); }

		unshift(@lines,"$no<><>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		unshift(@lines,"$no<>$addr<>$times<>\n");

		# �X�V
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @lines;
		close(OUT);

	# ���X�L���̏ꍇ�F�g�b�v�\�[�g����
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
		if ($f) { &error("�s���ȕԐM�v���ł�"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		}
		push(@new,@tmp);

		# �X�V
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

	# ���X�L���̏ꍇ�F�g�b�v�\�[�g�Ȃ�
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
		if ($f) { &error("�s���ȕԐM�v���ł�"); }

		if ($match == 1) {
			push(@new,"$no<>$in{'reno'}<>$date<>$in{'name'}<>$in{'email'}<>$in{'sub'}<>$in{'icon'}<>$icon2<>$in{'comment'}<>$in{'color'}<>$in{'url'}<>$host<>$PW<>\n");
		}

		# �X�V
		unshift(@new,"$no<>$addr<>$times<>\n");
		open(OUT,">$logfile") || &error("Write Error: $logfile");
		print OUT @new;
		close(OUT);
	}

	# ���b�N����
	&unlock if ($lockkey);

	if ($in{'cook'} eq 'on') {
		&set_cookie($in{'name'},$in{'email'},$in{'url'},$in{'pwd'},$in{'color'},$in{'icon'});
	}

	# ���[���ʒm����
	if ($mailing == 1) { &mail_to; }
	elsif ($mailing == 2 && $in{'email'} ne $mailto) { &mail_to; }

	# �����[�h
	if ($location) {
		if ($ENV{'PERLXS'} eq "PerlIS") {
			print "HTTP/1.0 302 Temporary Redirection\r\n";
			print "Content-type: text/html\n";
		}
		print "Location: $location?\n\n";
	} else {
		&header;
		print "<div align=center><hr width=400>\n";
		print "<h3>���e�͐���ɏ�������܂���</h3>\n";
		print "<form action=\"$script\">\n";
		print "<input type=submit value='�f���֖߂�'></form>\n";
		print "<hr width=400></div>\n</body></html>\n";
	}
	exit;
}

#-------------------------------------------------
#  ���[�h����
#-------------------------------------------------
sub find {
	local($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$res,$url);

	&header;
	print <<"EOM";
[<a href="$script?">�߂�</a>]
<ul>
<li>����������<b>�L�[���[�h</b>����͂��u�����v�������Ă��������B
<li>�L�[���[�h�́u���p�X�y�[�X�v�ŋ�؂��ĕ����w�肷�邱�Ƃ��ł��܂��B
<form action="$script" method="POST">
<input type=hidden name=mode value="find">
�L�[���[�h <input type=text name=word size=35 value="$in{'word'}">
�������� <select name=cond>
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
<input type=submit value="����">
</form>
</ul>
EOM

	# ���[�h�����̎��s�ƌ��ʕ\��
	if ($in{'word'} ne "") {

		# ���͓��e�𐮗�
		$in{'word'} =~ s/�@/ /g;
		@wd = split(/\s+/, $in{'word'});

		# ��������
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

			# ���ʂ�\��
			$i++;
			($no,$reno,$date,$name,$mail,$sub,$icon,$icon2,$com,$res,$url) = split(/<>/);
			if ($mail) { $name = "<a href=\"mailto:$mail\">$name</a>"; }
			if ($url) {
				if ($url !~ /^http/i) { $url = "http://$url"; }
				$url = "[<a href=\"$url\" target='_blank'>HOME</a>]";
			}

			print "<dt><hr>[<b>$no</b>] <b>$sub</b> ",
			"���e�ҁF<b>$name</b> ���e���F$date $url<br><br><dd>$com<br>\n";
		}
		close(IN);
		print "<dt><hr>�������ʂ� <b>$i</b>���ł��B\n";
	}
	print "<dt><hr></dl>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �Ǘ����[�h
#-------------------------------------------------
sub admin {
	if ($in{'pass'} ne "" && $in{'pass'} ne $pass) {
		&error("�p�X���[�h���Ⴂ�܂�");
	}

	&header;
	print "[<a href=\"$script?\">�f���ɖ߂�</a>]\n";

	if ($in{'pass'} eq "") {
		print "<p><center><h4>�p�X���[�h����͂��ĉ�����</h4>\n";
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"del\">\n";
		print "<input type=password name=pass size=8>";
		print "<input type=submit value=\" �F�� \">\n";
		print "</form>\n";

	} else {

		# �폜����
		if ($DEL[0]) {

			# ���b�N����
			&lock if ($lockkey);

			# �폜�����}�b�`���O���X�V
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

			# �X�V
			unshift(@new,$top);
			open(OUT,">$logfile") || &error("Write Error : $logfile");
			print OUT @new;
			close(OUT);

			# ���b�N����
			&unlock if ($lockkey);
		}

		# �Ǘ���\��
		if ($page eq "") { $page = 0; }
		print "<p><center><table><tr><td>\n";
		print "<ul><li>�폜����L���̃`�F�b�N�{�b�N�X�Ƀ`�F�b�N�����A�폜�{�^���������ĉ������B\n";
		print "<li>�e�L�����폜����ƃ��X�L�����ꊇ���č폜����܂��B</ul>\n";
		print "</td></tr></table>\n";
		print "<form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=page value=\"$page\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=action value=\"$in{'action'}\">\n";
		print "<input type=submit value=\"�폜����\">";
		print "<input type=reset value=\"���Z�b�g\">\n";
		print "<p><table border=0 cellspacing=1>\n";
		print "<tr><th>�폜</th><th>�L��NO</th><th>���e��</th><th>�^�C�g��</th>";
		print "<th>���e��</th><th>URL</th><th>�R�����g</th><th>�z�X�g��</th></tr>\n";

		# �y�[�W��؂菈��
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

			# �폜�`�F�b�N�{�b�N�X
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
		print "<input type=submit value=\"�O��$logview�g\">\n";
		print "</td></form>\n";
	}
	if ($next_page < $i) {
		print "<td><form action=\"$script\" method=\"POST\">\n";
		print "<input type=hidden name=page value=\"$next_page\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=action value=\"$in{'action'}\">\n";
		print "<input type=submit value=\"����$logview�g\">\n";
		print "</td></form>\n";
	}
	print "</tr></table></center>\n";
	print "</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  �ԐM���X�t�H�[��
#-------------------------------------------------
sub res_msg {
	&header;
	print <<"EOM";
[<a href="javascript:history.back()">�f���ɖ߂�</a>]<hr>
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
			# ���X�薼�p
			if ($reno eq "") { $res_sub = "Re: $sub"; }

			print "<font color=\"$onepnt\"><b>$sub</b></font> <b>$name</b> - $date $url<p>\n";
			print "<blockquote>$com</blockquote><hr>\n";
		}
	}
	close(IN);
	if ($f) { &error("�s���ȕԐM�v���ł�"); }

	&form_view("$in{'no'}");
	print "</blockquote>\n</body>\n</html>\n";
	exit;
}

#-------------------------------------------------
#  ���ӎ���
#-------------------------------------------------
sub howto {
	&header;
	print <<EOM;
<br><br>
<div align="center">
<table border=1 cellpadding=10 align=center width="90%">
<tr><td bgcolor="#FFFFFF">
<font color="#000000">
<h3 style="color:$t_color">���ӎ���</h3>
<ol>
<li>���̌f����<b>�N�b�L�[�Ή�</b>�ł��B�P�x�L���𓊍e���������ƁA���Ȃ܂��A�d���[���A�t�q�k�A�폜�L�[�̏��͂Q��ڈȍ~�͎������͂���܂��B�i���������p�҂̃u���E�U���N�b�L�[�Ή��̏ꍇ�j
<li>���e�L���ɂ́A<b>�^�O�͈�؎g�p�ł��܂���B</b>
EOM
	if ($in_email) {
		print "<li>�L���𓊍e�����ł̕K�{���͍��ڂ�<b>�u���Ȃ܂��v�u���b�Z�[�W�v�u�d���[���v</b>�ł��B�t�q�k�ƍ폜�L�[�͔C�ӂł��B\n";
	} else {
		print "<li>�L���𓊍e�����ł̕K�{���͍��ڂ�<b>�u���Ȃ܂��v</b>��<b>�u���b�Z�[�W�v</b>�ł��B�d���[���A�t�q�k�A�폜�L�[�͔C�ӂł��B\n";
	}

	print <<EOM;
<li>�L���ɂ́A<b>���p�J�i�͈�؎g�p���Ȃ��ŉ������B</b>���������̌����ƂȂ�܂��B
<li>�L���̓��e����<b>�u�폜�L�[�v</b>�Ƀp�X���[�h�i�p������8�����ȓ��j�����Ă����ƁA���̋L���͎���<b>�폜�L�[</b>�ɂ���č폜���邱�Ƃ��ł��܂��B
<li>�L���̕ێ�������<b>�ő� $max��</b>�ł��B����𒴂���ƌÂ����Ɏ����폜����܂��B
<li>�ߋ��̓��e�L������<b>�u�L�[���[�h�v�ɂ���ĊȈՌ������ł��܂��B</b>�g�b�v���j���[��<a href="$script?mode=find">�u���[�h�����v</a>�̃����N���N���b�N����ƌ������[�h�ƂȂ�܂��B
<li>�Ǘ��҂��������s���v�Ɣ��f����L���⑼�l���排�������L���͗\\���Ȃ��폜���邱�Ƃ�����܂��B
</ol>
</font>
</td></tr></table>
<p>
<form>
<input type=button value="�O��ʂɖ߂�" onClick="history.back()">
</form>
</body>
</html>
EOM
exit;
}

#-------------------------------------------------
#  ���[�U�L���폜
#-------------------------------------------------
sub usrdel {
	# ���e�`�F�b�N
	if ($postonly && !$post_flag) { &error("�s���ȃA�N�Z�X�ł�"); }
	if ($baseUrl) { &refCheck; }

	if ($in{'no'} eq '' || $in{'pwd'} eq '') {
		&error("�폜No�܂��͍폜�L�[�����̓����ł�");
	}

	# ���b�N����
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

	if ($flag == 0) { &error("�Y���L������������܂���"); }
	if ($PW eq '') { &error("�Y���L���ɂ͍폜�L�[���ݒ肳��Ă��܂���"); }

	# �폜�L�[���ƍ�
	$check = &decrypt($in{'pwd'}, $PW);
	if ($check != 1) { &error("�폜�L�[���Ⴂ�܂�"); }
	else {
		# �X�V
		unshift(@new,$top);
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

		# ���b�N����
		&unlock if ($lockkey);
	}
}

#-------------------------------------------------
#  �f�R�[�h����
#-------------------------------------------------
sub decode {
	local($buf, $key, $val);

	$post_flag=0;
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		$post_flag=1;
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &error("���e�ʂ��傫�����܂�"); }
		read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
	} else {
		$buf = $ENV{'QUERY_STRING'};
	}

	foreach ( split(/&/, $buf) ) {
		($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

		# S-JIS�R�[�h�ϊ�
		&jcode'convert(*val, "sjis", "", "z");

		# �^�O����
		$val =~ s/&/&amp;/g;
		$val =~ s/"/&quot;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;

		# ���s����
		if ($key eq 'comment') {
			$val =~ s/\r\n/<br>/g;
			$val =~ s/\r/<br>/g;
			$val =~ s/\n/<br>/g;
		} else {
			$val =~ s/\r//g;
			$val =~ s/\n//g;
		}

		# �폜���
		if ($key eq 'del') { push(@DEL,$val); }

		$in{$key} = $val;
	}
	if ($in{'sub'} eq "") { $in{'sub'} = "����"; }
	$mode = $in{'mode'};
	$page = $in{'page'};

	# �����̎擾
	$ENV{'TZ'} = "JST-9";
	$times = time;
	($min,$hour,$mday,$mon,$year,$wday) = (localtime($times))[1..6];

	# �����̃t�H�[�}�b�g
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
	$date = sprintf("%04d\/%02d\/%02d(%s) %02d\:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min);
}

#--------------#
#  HTML�w�b�_  #
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
#  �G���[����
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
<input type=button value="�O��ʂɖ߂�" onClick="history.back()">
</form>
</div>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  �N�b�L�[���s
#-------------------------------------------------
sub set_cookie {
	local(@cook) = @_;
	local($gmt, $cook, @t, @m, @w);

	@t = gmtime(time + 60*24*60*60);
	@m = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	@w = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# ���ەW�������`
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$w[$t[6]], $t[3], $m[$t[4]], $t[5]+1900, $t[2], $t[1], $t[0]);

	# �ۑ��f�[�^��URL�G���R�[�h
	foreach (@cook) {
		s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		$cook .= "$_<>";
	}

	# �i�[
	print "Set-Cookie: HoneyBoard=$cook; expires=$gmt\n";
}

#-------------------------------------------------
#  �N�b�L�[�擾
#-------------------------------------------------
sub get_cookie {
	local($key, $val, *cook);

	# �N�b�L�[���擾
	$cook = $ENV{'HTTP_COOKIE'};

	# �Y��ID�����o��
	foreach ( split(/;/, $cook) ) {
		($key, $val) = split(/=/);
		$key =~ s/\s//g;
		$cook{$key} = $val;
	}

	# �f�[�^��URL�f�R�[�h���ĕ���
	foreach ( split(/<>/, $cook{'HoneyBoard'}) ) {
		s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("H2", $1)/eg;

		push(@cook,$_);
	}
	return (@cook);
}

#-------------------------------------------------
#  �p�X���[�h�Í�����
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
#  �p�X���[�h�ƍ�����
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
#  ���b�N����
#-------------------------------------------------
sub lock {
	local($retry)=5;

	# �Â����b�N�͍폜
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	# symlink�֐������b�N
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}

	# mkdir�֐������b�N
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag=1;
}

#-------------------------------------------------
#  ���b�N����
#-------------------------------------------------
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }

	$lockflag=0;
}

#-------------------------------------------------
#  ���[�����M
#-------------------------------------------------
sub mail_to {
	local($com, $msub, $mbody);

	# ���[���^�C�g�����`
	$msub = &base64("[$title : $no] $in{'sub'}");

	# �L������
	$com  = $in{'comment'};
	$com =~ s/<br>/\n/g;
	$com =~ s/&lt;/</g;
	$com =~ s/&gt;/>/g;
	$com =~ s/&quot;/"/g;
	$com =~ s/&amp;/&/g;

	# ���[���{�����`
	$mbody = <<"EOM";
���e�����F$date
�z�X�g���F$host
�u���E�U�F$ENV{'HTTP_USER_AGENT'}

���e�Җ��F$in{'name'}
�d���[���F$in{'email'}
�t�q�k  �F$in{'url'}
�^�C�g���F$in{'sub'}

$com
EOM

	# sendmail�N��
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
#  BASE64�ϊ�
#-------------------------------------------------
#	�Ƃقق�WWW����Ō��J����Ă��郋�[�`����
#	�Q�l�ɂ��܂����B( http://tohoho.wakusei.ne.jp/ )
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
#  �C���[�W�\��
#-------------------------------------------------
sub image {
	local($i,$j,$stop);

	&header;
	print "<center><hr width=\"75%\">\n";
	print "<b>�摜�C���[�W</b>\n";
	print "<p>- ���ݓo�^����Ă���摜�C���[�W�͈ȉ��̂Ƃ���ł� -\n";
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
#  ���������N
#-------------------------------------------------
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\=\@\;\#\:\%]+)/$1<a href=\"$2\" target='_top'>$2<\/a>/g;
}

#-------------------------------------------------
#  ���e�t�H�[��
#-------------------------------------------------
sub form_view {
	# �N�b�L�[�����擾
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
  <td><b>���Ȃ܂�</b></td>
  <td><input type=text name=name size=28 value="$cnam"></td>
</tr>
<tr>
  <td><b>�d���[��</b></td>
  <td><input type=text name=email size=28 value="$ceml"></td>
</tr>
<tr>
  <td><b>�^�C�g��</b></td>
  <td>
    <input type=text name=sub size=34 value="$res_sub">
    &nbsp;
    <input type=submit value="���M����"><input type=reset value="���Z�b�g">
  </td>
</tr>
<tr>
  <td colspan=2>
    <b>���b�Z�[�W</b><br>
    <textarea name=comment cols=55 rows=7 wrap=soft></textarea>
  </td>
</tr>
<tr>
<tr>
  <td><b>�Q�Ɛ�</b></td>
  <td><input type=text name=url size=50 value="$curl"></td>
</tr>
<tr>
  <td><b>�C���[�W</b></td>
  <td><select name=icon>
EOM
	# �C���[�W�̑I���t�H�[����\��
	push(@icon1,"$mgr_icon");
	push(@icon2,"�Ǘ��җp");
	foreach (0 .. $#icon1) {
		if ($icon1[$_] eq $cico) {
			print "<option value=\"$icon1[$_]\" selected>$icon2[$_]\n";
		} else {
			print "<option value=\"$icon1[$_]\">$icon2[$_]\n";
		}
	}

	print <<"EOM";
    </select> [<a href="$script?mode=image" target="_blank">�A�C�R���Q��</a>]
  </td>
</tr>
<tr>
  <td><b>�폜�L�[</b></td>
  <td><input type=password name=pwd size=6 maxlength=8 value="$cpwd">
    <small>(�L���̍폜���Ɏg�p)</small>
  </td>
</tr>
<tr>
  <td><b>�����F</b></td>
  <td>
EOM

	if ($ccol eq "") { $ccol = $colors[0]; }
	foreach (0 .. $#colors) {
		if ($ccol eq "$colors[$_]") {
			print "<input type=radio name=color value=\"$colors[$_]\" checked>";
			print "<font color=\"$colors[$_]\">��</font> \n";
		} else {
			print "<input type=radio name=color value=\"$colors[$_]\">";
			print "<font color=\"$colors[$_]\">��</font> \n";
		}
	}

	if ($_[0]) {
		print "<input type=hidden name=no value=\"$_[0]\">\n";
	}

	print "</td></tr><tr><td></td><td>\n";
	print "<input type=checkbox name=cook value=\"on\" checked> ";
	print "�N�b�L�[��ۑ�\n";
	print "</td></tr></table>\n</form>\n";
}

#-------------------------------------------------
#  REF�`�F�b�N
#-------------------------------------------------
sub refCheck {
	local($ref) = $ENV{'HTTP_REFERER'};
	$ref =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

	$baseUrl =~ s/(\W)/\\$1/g;
	if ($ref && $ref !~ /$baseUrl/i) { &error("�s���ȃA�N�Z�X�ł�"); }
}

#-------------------------------------------------
#  �`�F�b�N���[�h
#-------------------------------------------------
sub check {
	&header;
	print "<h2>Check Mode</h2>\n";
	print "<ul>\n";

	# ���O�p�X
	if (-e $logfile) {
		print "<li>���O�t�@�C���̃p�X�FOK\n";
		# ���O�p�[�~�b�V����
		if (-r $logfile && -w $logfile) {
			print "<li>���O�t�@�C���̃p�[�~�b�V�����FOK\n";
		} else { print "<li>���O�t�@�C���̃p�[�~�b�V�����FNG\n"; }
	} else { print "<li>���O�t�@�C���̃p�X�FNG �� $logfile\n"; }

	# ���b�N�f�B���N�g��
	print "<li>���b�N�`���F";
	if ($lockkey == 0) { print "���b�N�ݒ�Ȃ�\n"; }
	else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }
		($lockdir) = $lockfile =~ /(.*)[\\\/].*$/;
		print "<li>���b�N�f�B���N�g���F$lockdir\n";

		if (-d $lockdir) {
			print "<li>���b�N�f�B���N�g���̃p�X�FOK\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<li>���b�N�f�B���N�g���̃p�[�~�b�V�����FOK\n";
			} else {
				print "<li>���b�N�f�B���N�g���̃p�[�~�b�V�����FNG �� $lockdir\n";
			}
		} else { print "<li>���b�N�f�B���N�g���̃p�X�FNG �� $lockdir\n"; }
	}
	print "</ul>\n</body>\n</html>\n";
	exit;
}


__END__

