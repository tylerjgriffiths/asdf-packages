Name: cl-split-sequence
Version: 2.0.0
Release: 1%{?dist}
License: MIT
Summary: A sequence splitting library for Common Lisp
Source0: https://github.com/sharplispers/%{name}/archive/v%{version}.tar.gz

%define _asdfdir %{_datadir}/asdf-packages/

%description
A sequence splitting library for Common Lisp

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p 1

%build

%install
mkdir -p %{buildroot}%{_asdfdir}/%{name}
mv * %{buildroot}%{_asdfdir}/%{name}/

%files
%{_asdfdir}/%{name}
