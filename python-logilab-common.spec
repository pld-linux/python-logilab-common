
# TODO:
#	- check if %%{py_sitescriptdir} used here doesn't break other
#	  python-logilab packages

%define	module	common
%include	/usr/lib/rpm/macros.python
Summary:	Logilab common modules
Summary(pl):	Wspólne modu³y Logilab
Name:		python-logilab-common
Version:	0.4.4
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	4cd3ce38efbd27c6cf4223f0ced2a5b5
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

# because some logilab's software depend on this package
# and some not, so they all provide the __init__.py and we
# have to remove it in dependent software and create it
# here
touch $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/*
