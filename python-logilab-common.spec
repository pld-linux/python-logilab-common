%define	module	common
%include	/usr/lib/rpm/macros.python
Summary:	Logilab common modules
Summary(pl):	Wspólne modu³y Logilab
Name:		python-logilab-common
Version:	0.3.3
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	bc34d6dd3f79f66256ab639dae1ce1ba
URL:		http://www.logilab.org/projects/%{module}/view
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package logilab.common contains several modules providing low
level functionalities shared among several Python projects developed
by Logilab.

%description -l pl
Pakiet logilab.common zawiera ró¿ne modu³y dostarczaj±ce
niskopoziomow± funkcjonalno¶æ wykorzystywan± przez ró¿ne pythonowe
projekty tworzone przez Logilab.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitedir}/*
