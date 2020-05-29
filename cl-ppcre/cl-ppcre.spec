Name: cl-ppcre
Version: 2.1.1
Release: 1%{?dist}
License: BSD
Summary: Portable Perl-compatible regular expressions for Common Lisp
Source0: https://github.com/edicl/cl-ppcre/archive/v2.1.1.tar.gz
BuildRequires: sbcl
BuildRequires: texinfo
BuildRequires: autoconf
Requires: sbcl

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
