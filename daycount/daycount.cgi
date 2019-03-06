#!/usr/bin/perl

#��������������������������������������������������������������������
#�� DAY COUNTER v2.6 (2002/08/02)
#�� Copyright(C) KENT WEB 1997-2002
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'DAY COUNTER v2.6';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������
#
# [ �f�B���N�g���\���� ]
#
#  public_html / index.html (�z�[���f�B���N�g���j
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
# [ �^�O�̏������̗� ]
#
#  ���J�E���g�� 	<img src="�p�X/daycount.cgi?gif">
#  �{���̃J�E���g�� 	<img src="�p�X/daycount.cgi?today">
#  ����@�@�V		<img src="�p�X/daycount.cgi?yes">
#
#  ������`�F�b�N�̂����� (�u���E�U����Ō�� ?check �����Čďo���j
#    http://�`�`/daycount.cgi?check

#============#
#  �ݒ荀��  #
#============#

# �摜�A�����C�u�����捞��
require './gifcat.pl';

# ���J�E���g���̌���
$digit1 = 5;

# �{/����J�E���g���̌���
$digit2 = 3;

# �L�^�t�@�C��
$logfile = './daycount.dat';

# ���J�E���g�pGIF�摜�̃f�B���N�g��
#  --> �t���p�X���� / ����n��p�X
$gifdir1 = './gif1';

# �{/����J�E���g�pGIF�摜�̃f�B���N�g��
#  --> �t���p�X���� / ����n��p�X
$gifdir2 = './gif2';

# IP�A�h���X�̓�d�J�E���g�`�F�b�N
#   0 : �`�F�b�N���Ȃ�
#   1 : �`�F�b�N����
$ip_check = 1;

# �t�@�C�����b�N�`��
#  �� 0=no 1=symlink�֐� 2=mkdir�֐�
$lockkey = 2;

# ���b�N�t�@�C����
$lockfile = './lock/daycount.lock';

# �J�E���^�̋@�\�^�C�v
#   0 : ���J�E���g���s�v�i����^�{���̂݁j
#   1 : �W���^�C�v
$type = 1;

#============#
#  �ݒ芮��  #
#============#

# ����������
$mode = $ENV{'QUERY_STRING'};
$mode =~ s/\W//g;

# �`�F�b�N���[�h
if (!$mode || $mode eq 'check') { &check; }

# �X�V�n�����łȂ��Ȃ��1�b�҂�����
if ($type == 1 && $mode ne "gif") { sleep(1); }
elsif ($type == 0 && $mode eq "yes") { sleep(1); }

# ���b�N�J�n
$lockflag=0;
if (($type == 1 && $mode eq "gif" && $lockkey) || ($type == 0 && $mode eq "today" && $lockkey)) { &lock; $lockflag=1; }

# �L�^�t�@�C������ǂݍ���
open(IN,"$logfile") || &error("LK");
$data = <IN>;
close(IN);

# �L�^�t�@�C���𕪉�
($key,$yes,$today,$count,$ip) = split(/<>/, $data);

# �������擾
$ENV{'TZ'} = "JST-9";
($mday) = (localtime(time))[3];

# IP�`�F�b�N
$flag=0;
if ($ip_check) {
	$addr = $ENV{'REMOTE_ADDR'};
	if ($addr eq $ip) { $flag=1; }
}

# �{���̃J�E���g�����L�[�ɂ��ăJ�E���g�A�b�v
if ((!$flag && $type && $mode eq "gif") || (!$flag && !$type && $mode eq "today")) {

	if ($key eq "$mday") { $today++; }
	else {
		$yes   = $today;
		$today = 1;
	}

	# �J�E���g�A�b�v����
	$count++;

	# �L�^�t�@�C�����X�V����
	$data = "$mday<>$yes<>$today<>$count<>$addr<>";
	open(OUT,">$logfile") || &error("LK");
	print OUT $data;
	close(OUT);
}

# ���b�N����
if ($lockflag) { &unlock; }

# �摜�\��
&count_view;
exit;

#-------------------#
# �J�E���^�o�͏���  #
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

	# �\���摜��z��
	while (length($count) < $fig) { $count = '0' . $count; }
	$length = length($count);
	@GIF=();
	foreach (0 .. $length-1) {
		$n = substr($count,$_,1);
		push(@GIF, "$gifdir/$n\.gif");
	}

	# �A���摜���o��
	print "Content-type: image/gif\n\n";
	binmode(STDOUT);
	print &gifcat'gifcat(@GIF);
}

#--------------#
#  ���b�N����  #
#--------------#
sub lock {
	local($retry)=5;
	# 1���ȏ�Â����b�N�͍폜����
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime && $mtime < time - 60) { &unlock; }
	}
	# symlink�֐������b�N
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error; }
			sleep(1);
		}
	# mkdir�֐������b�N
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error; }
			sleep(1);
		}
	}
	$lockflag=1;
}

#--------------#
#  ���b�N����  #
#--------------#
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }
	$lockflag=0;
}

#--------------#
#  �G���[����  #
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
#  �`�F�b�N���[�h  #
#------------------#
sub check {
	print "Content-type: text/html\n\n";
	print "<html><head><title>DAY COUNTER</title></head>\n";
	print "<body>\n<h2>Check Mode</h2>\n<UL>\n";

	# ���O�t�@�C���̃p�X�m�F
	if (-e $logfile) {
		print "<LI>���O�t�@�C���̃p�X : OK!\n";
		# ���O�t�@�C���̃p�[�~�b�V����
		if (-r $logfile && -w $logfile) {
			print "<LI>���O�t�@�C���̃p�[�~�b�V���� : OK!\n";
		} else {
			print "<LI>���O�t�@�C���̃p�[�~�b�V���� : NG �� $logfile\n";
		}
	} else { print "<LI>���O�t�@�C���̃p�X : NG �� $logfile\n"; }

	# �摜�f�B���N�g��
	foreach ($gifdir1, $gifdir2) {
		# �f�B���N�g���p�X�m�F
		if (-d $_) { print "<LI>�摜�f�B���N�g���p�X ( $_ ) : OK!\n"; }
		else { print "<LI>�摜�f�B���N�g���̃p�X : NG �� $_\n"; }

		# �摜�`�F�b�N
		foreach $i (0 .. 9) {
			if (-e "$_\/$i\.gif") {
				print "<LI>�摜 : $_\/$i\.gif �� OK!\n";
			} else {
				print "<LI>�摜 : $_\/$i\.gif �� NG!\n";
			}
		}
	}

	# ���b�N�f�B���N�g��
	print "<LI>���b�N�`���F";
	if ($lockkey == 0) { print "���b�N�ݒ�Ȃ�\n"; }
	else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }
		$lockfile =~ s/(.*)[\\\/].*$/$lockdir = $1/e;
		print "<LI>���b�N�f�B���N�g���F$lockdir\n";

		if (-d $lockdir) {
			print "<LI>���b�N�f�B���N�g���̃p�X�FOK\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<LI>���b�N�f�B���N�g���̃p�[�~�b�V�����FOK\n";
			} else {
				print "<LI>���b�N�f�B���N�g���̃p�[�~�b�V�����FNG �� $lockdir\n";
			}
		} else { print "<LI>���b�N�f�B���N�g���̃p�X�FNG �� $lockdir\n"; }
	}

	# ���쌠�\���F�폜�֎~
	print "<P><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/'>Day Counter</a> -\n";
	print "</UL>\n</small>\n</body></html>\n";
	exit;
}

__END__

