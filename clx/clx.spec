Name: clx
Version: 0.7.5
Release: 1%{?dist}
License: MIT
Summary: An X11 client library for Common Lisp
Source0: https://github.com/sharplispers/%{name}/archive/%{version}.tar.gz

%define _asdfdir %{_datadir}/asdf-packages/

%description
A tiling window manager written in Common Lisp

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p 1

%build

%install
mkdir -p %{buildroot}%{_asdfdir}/%{name}
mv * %{buildroot}%{_asdfdir}/%{name}/

%files
%{_asdfdir}/%{name}
