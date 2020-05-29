Name: split-sequence
Version: 1.5
Release: 1%{?dist}
License: BSD
Summary: A Common Lisp library for drawing into PNG files with a PDF-like interface
Source0: https://beta.quicklisp.org/archive/%{name}/2017-12-27/%{name}-%{version}.tgz

%define _asdfdir %{_datadir}/asdf-packages/

%description
A Common Lisp library for drawing into PNG files with a PDF-like interface

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p 1

%build

%install
mkdir -p %{buildroot}%{_asdfdir}/%{name}
mv * %{buildroot}%{_asdfdir}/%{name}/

%files
%{_asdfdir}/%{name}
