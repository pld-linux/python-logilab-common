
# TODO:
#	- check if %%{py_sitescriptdir} used here doesn't break other
#	  python-logilab packages
#	  (I changed sth. is this what author meant?)

%define	module	common
Summary:	Logilab common modules
Summary(pl):	Wspólne moduły Logilab
Name:		python-logilab-common
Version:	0.5.2
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/common/%{module}-%{version}.tar.gz
# Source0-md5:	f373d4e38e101e593449d972f3e70200
URL:		http://www.logilab.org/projects/common/view
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package logilab.common contains several modules providing low
level functionalities shared among several Python projects developed
by Logilab.

%description -l pl
Pakiet logilab.common zawiera różne moduły dostarczające
niskopoziomową funkcjonalność wykorzystywaną przez różne pythonowe
projekty tworzone przez Logilab.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/logilab

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

# because some logilab's software depend on this package
# and some not, so they all provide the __init__.py and we
# have to remove it in dependent software and create it
# here
for DIR in $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py_sitedir}}; do
touch $DIR/logilab/__init__.py
%py_comp $DIR/logilab/
%py_ocomp $DIR/logilab/

find $DIR -name \*.py -exec rm -f {} \;
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/*
%{py_sitedir}/*
