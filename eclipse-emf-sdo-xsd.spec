# TODO
# - rename to eclipse-emf-sdo-xsd.spec
# - build noarch

%define		module	emf-sdo-xsd
%define		buildid	200706262000
Summary:	Eclipse Modeling Framework
Summary(pl.UTF-8):	Eclipse Modeling Framework - szkielet do modelowania w Eclipse
Name:		eclipse-%{module}
Version:	2.3.0
Release:	0.1
License:	EPL v1.0
Group:		Development/Tools
URL:		http://www.eclipse.org/emf/
BuildRequires:	unzip
Requires:	eclipse >= 3.2
Source0:	http://archive.eclipse.org/modeling/emf/emf/downloads/drops/%{version}/R%{buildid}/%{module}-SDK-%{version}.zip
# Source0-md5:	95c3eed41fa88e18b998cf14d9a2a985
Obsoletes:	eclipse-emf-sdo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir	%{_libdir}/eclipse

%description
Eclipse Modeling Framework (EMF).

%description -l pl.UTF-8
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
%{_eclipsedir}/features/org.eclipse.xsd*
%{_eclipsedir}/plugins/org.eclipse.emf*
%{_eclipsedir}/plugins/org.eclipse.xsd*
