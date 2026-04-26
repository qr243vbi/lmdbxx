#
# spec file for package lmdbxx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lmdbxx
Version:        1.0.1
Release:        0
Summary:        C++ wrapper for the LMDB embedded B+ tree database library
License:        PDDL-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/qr243vbi/lmdbxx
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  (ninja or ninja-build)

%bcond_without test
%if %{with test}
BuildRequires:  lmdb-devel
%check
declare -a LMDBXX_FLAGS=("-I$PWD/include/lmdbxx")
. debian/tests/compilation-test
. debian/tests/string-view-test
%endif

%description
Header-only %{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lmdb-devel

%description devel
Header-only %{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
ln -sf lmdbxx/lmdb++.h %{buildroot}%{_includedir}/lmdb++.h

%files devel
%doc README.md TODO FUNCTIONS.rst AUTHORS
%license UNLICENSE
%{_includedir}/lmdb++.h
%dir %{_includedir}/lmdbxx
%{_includedir}/lmdbxx/lmdb++.h
%{_datadir}/pkgconfig/lmdbxx.pc

%changelog
