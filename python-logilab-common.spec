%define	module	common
%include	/usr/lib/rpm/macros.python
Summary:	Logilab common modules
Summary(pl):	Wsp�lne modu�y Logilab
Name:		python-logilab-common
Version:	0.2.2
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6554f6694167c72aa867364b1bc56e12
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
Pakiet logilab.common zawiera r�ne modu�y dostarczaj�ce
niskopoziomow� funkcjonalno�� wykorzystywan� przez r�ne pythonowe
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
