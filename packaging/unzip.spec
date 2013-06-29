Name:           unzip
Version:        6.0
Release:        9
License:        BSD
Summary:        A utility for unpacking zip files
Url:            http://www.info-zip.org/pub/infozip/UnZip.html
Group:          Applications/Archiving
Source:         ftp://ftp.info-zip.org/pub/infozip/src/unzip60.tar.gz
Source1001: 	unzip.manifest

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q -n %{name}60
cp %{SOURCE1001} .



ln -s unix/Makefile Makefile
%build
make CFLAGS="-D_LARGEFILE64_SOURCE" linux_noasm LF2="" %{?_smp_mflags}

%install

make prefix=%{buildroot}%{_prefix} MANDIR=%{buildroot}/%{_mandir}/man1 INSTALL="cp -p" install LF2=""

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/*
%doc %{_mandir}/*/*

