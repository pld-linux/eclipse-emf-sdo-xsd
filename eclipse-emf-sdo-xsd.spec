%define		module		emf-sdo
%define		_buildid	R200609210005
Summary:	Eclipse Modeling Framework
Name:		eclipse-%{module}
Version:	2.2.1
Release:	0.1
License:	CPL
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/emf/downloads/drops/%{version}/%{_buildid}/%{module}-SDK-%{version}.zip
# Source0-md5:	8dcd27a7dca1648c0da0c056c551f472
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_datadir}/eclipse

%description
Eclipse Modeling Framework (EMF).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/org.eclipse.emf*
%{_eclipsedir}/plugins/org.eclipse.emf*
