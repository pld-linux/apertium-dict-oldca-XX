Summary:	Old Catalan morphological dictionary for Apertium
Summary(pl.UTF-8):	Słownik morfologiczny języka starokatalońskiego dla Apertium
%define	lpair	oldca-XX
Name:		apertium-dict-%{lpair}
Version:	0.7
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	1d43b566fa3fb6657f357b176ef92f3a
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-apertium32.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Old Catalan morphological dictionary for
Apertium.

%description -l pl.UTF-8
Ten pakiet zawiera słownik morfologiczny języka starokatalońskiego dla
Apertium.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/oldca-XX-morph.mode
