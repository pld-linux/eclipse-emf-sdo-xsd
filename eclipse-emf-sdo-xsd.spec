%define		module		emf-sdo
%define		_buildid	R200609210005
Summary:	Eclipse Modeling Framework
Summary(pl):	Eclipse Modeling Framework - szkielet do modelowania w Eclipse
Name:		eclipse-%{module}
Version:	2.2.1
Release:	0.2
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/emf/downloads/drops/%{version}/%{_buildid}/%{module}-SDK-%{version}.zip
# Source0-md5:	8dcd27a7dca1648c0da0c056c551f472
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_libdir}/eclipse

%description
Eclipse Modeling Framework (EMF).

%description -l pl
Eclipse Modeling Framework (EMF) - szkielet do modelowania w Eclipse.

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
