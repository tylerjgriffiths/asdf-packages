Name: cl-ppcre
Version: 2.1.1
Release: 1%{?dist}
License: BSD
Summary: Portable Perl-compatible regular expressions for Common Lisp
Source0: https://github.com/edicl/%{name}/archive/v%{version}.tar.gz

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
