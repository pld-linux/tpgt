Summary:	Ncurses based typing trainer program
Summary(hu.UTF-8):	Ncurses alapú gépelést oktató program
Name:		tpgt
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://szit.hu/tpgt/%{name}-%{version}-src.tar.gz
# Source0-md5:	03d351f9b3081fee7b8bd850596c2de4
Patch0:		%{name}-0.6.0-lesson-fix-dir.patch
URL:		http://szit.hu/tpgt/
BuildRequires:	ncurses-ext-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncurses based typing trainer program.

%description -l hu.UTF-8
Ncurses alapú gépelést oktató program.

%prep
%setup -q
%patch0 -p1
%{__sed} -i "s@^CFLAGS.*@CFLAGS=%{rpmcflags}@" src/Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/tpgt $RPM_BUILD_ROOT%{_bindir}
for lang in hu en; do
	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/lessons/${lang}
	install lessons/${lang}/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lessons/${lang}
done
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install README{,.hu} TODO{,.hu} ChangeLog BUGS doc/lesson_format.txt doc/hu/lecke_formatum.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_datadir}/locale/hu/LC_MESSAGES/
install po/hu/LC_MESSAGES/tpgt.mo $RPM_BUILD_ROOT%{_datadir}/locale/hu/LC_MESSAGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tpgt
%dir %{_datadir}/tpgt
%dir %{_datadir}/tpgt/lessons
%{_docdir}/%{name}-%{version}
%{_datadir}/%{name}/lessons/hu
%{_datadir}/%{name}/lessons/en
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES
