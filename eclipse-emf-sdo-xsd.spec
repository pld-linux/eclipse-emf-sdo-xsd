%define		module	emf-sdo-xsd
Summary:	Eclipse Modeling Framework
Summary(pl.UTF-8):	Eclipse Modeling Framework - szkielet do modelowania w Eclipse
Name:		eclipse-%{module}
Version:	2.3.2
Release:	2
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/modeling/emf/emf/downloads/drops/%{version}/R200802051830/%{module}-SDK-%{version}.zip
# Source0-md5:	da937bf8e31788d5121176581b286a43
URL:		http://www.eclipse.org/emf/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.2
Obsoletes:	eclipse-emf-sdo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
Eclipse Modeling Framework (EMF).

%description -l pl.UTF-8
Eclipse Modeling Framework (EMF) - szkielet do modelowania w Eclipse.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a eclipse/features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a eclipse/plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.emf*
%{eclipsedir}/features/org.eclipse.xsd*
%{eclipsedir}/plugins/org.eclipse.emf*
%{eclipsedir}/plugins/org.eclipse.xsd*
