Summary:	NextStep+Amiga+Win95 Theme
Summary(pl):	Motyw ³±cz±cy wygl±d NextStep+Amiga+Win95
Name:		gtk-theme-engine-Xenophilia
Version:	0.7
Release:	1
License:	LGPL
Group:		Themes/Gtk
Source0:	Xenophilia-1.2.x.tar.gz
URL:		http://gtk.classic.themes.org/php/download.phtml?object=gtk.theme.935252517&rev=1.2.x
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Theme Engine with a plain look which is somewhere in between NextStep,
Amiga and Windows 95.

%description -l pl
Motyw ³±cz±cy wygl±d NextStepa, Amigi oraz Windows 95.

%prep
%setup  -q -n Xenophilia-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	LIB_PATH="%{_libdir}/gtk/themes/engines" \
	DATA_PATH="%{_datadir}/themes"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines
install -d $RPM_BUILD_ROOT%{_datadir}/themes

%{__make} install \
	LIB_PATH=$RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines \
	DATA_PATH=$RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CONFIGURATION ChangeLog README TODO
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*
%{_datadir}/themes/*
