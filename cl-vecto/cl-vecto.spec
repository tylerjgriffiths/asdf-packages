%define lispname vecto
Name: cl-%{lispname}
Version: 1.5
Release: 1%{?dist}
License: BSD
Summary: A Common Lisp library for drawing into PNG files with a PDF-like interface
Source0: https://beta.quicklisp.org/archive/%{lispname}/2017-12-27/%{lispname}-%{version}.tgz

BuildRequires: common-lisp-controller
Requires: common-lisp-controller
Requires(post): common-lisp-controller
Requires(preun): common-lisp-controller

%description
A Common Lisp library for drawing into PNG files with a PDF-like interface

%global debug_package %{nil}

%prep
#%autosetup -n %{name}-%{version} -p 1
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/%{lispname}
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems

for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/%{lispname};
done;
for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/%{lispname};
done;
cd %{buildroot}%{_datadir}/common-lisp/source/%{lispname};
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/@NAME@/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source %{lispname}

%preun
/usr/sbin/unregister-common-lisp-source %{lispname}

%clean
%{__rm} -rf %{buildroot}

%files
%{_asdfdir}/%{name}
