Summary:	NextStep+Amiga+Win95 Theme
Summary(pl):	Motyw ³±cz±cy wygl±d NextStep+Amiga+Win95
Name:		gtk-theme-engine-Xenophilia
Version:	0.8
Release:	3
License:	LGPL
Group:		Themes/GTK+
Source0:	http://download.freshmeat.net/themes/xenophilia/xenophilia-%{version}.tar.gz
# Source0-md5:	620127ce8e668588de2373783254a3e8
Patch0:		%{name}-DESTDIR.patch
URL:		http://gtk.classic.themes.org/php/download.phtml?object=gtk.theme.935252517&rev=1.2.x
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme Engine with a plain look which is somewhere in between NextStep,
Amiga and Windows 95.

%description -l pl
Motyw ³±cz±cy wygl±d NextStepa, Amigi oraz Windows 95.

%prep
%setup  -q -n Xenophilia-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -DG_DISABLE_CHECKS"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C themes install-themes \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CONFIGURATION ChangeLog README TODO themes/docs/*
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*
%dir %{_datadir}/themes/*
%dir %{_datadir}/themes/*/gtk
%{_datadir}/themes/*/gtk/*
