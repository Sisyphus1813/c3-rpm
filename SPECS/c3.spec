Name:           c3
Version:        0.7.10
Release:        3%{?dist}
Summary:        C3 programming langauge compiler and standard library

License:        MIT AND LGPL-3.0-or-later
URL:            https://c3-lang.org/

Source0:        https://github.com/c3lang/c3c/archive/refs/tags/v%{version}.tar.gz
Patch0:         c3c-linkdir.patch

ExclusiveArch:  x86_64 aarch64

%if 0%{?fedora} >= 44
BuildRequires:  clang21
BuildRequires:  llvm21-devel
%else
BuildRequires:  clang
BuildRequires:  llvm-devel
%endif
BuildRequires:  cmake
BuildRequires:  lld-devel
BuildRequires:  ncurses-devel
BuildRequires:  libcurl-devel
BuildRequires:  zlib-devel
BuildRequires:  libzstd-devel
BuildRequires:  libxml2-devel
BuildRequires:  libffi-devel

%description
C3 is a programming language that builds on the syntax and semantics of the C language, with the goal of evolving it while still retaining familiarity for C programmers.
This package builds C3 from source and installs the compiler along with the standard library.
This is an unofficial COPR packaging of C3 and is maintained independently.
Upstream project: https://github.com/c3lang/c3c

%prep
%if 0%{?fedora} >= 44
%autosetup -n c3c-%{version} -p1
%else
%autosetup -n c3c-%{version}
%endif

%build
%if 0%{?fedora} >= 44
cmake -B build -S . -DC3_LINK_DYNAMIC=1 -DLLVM_DIR=/usr/lib64/llvm21/lib64/cmake/llvm
%else
cmake -B build -S . -DC3_LINK_DYNAMIC=1
%endif
cmake --build build

%check
./build/c3c --version

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 build/c3c %{buildroot}%{_bindir}/c3c
install -d -m 0755 %{buildroot}%{_prefix}/lib/c3
cp -r build/lib/* %{buildroot}%{_prefix}/lib/c3

%files
%license LICENSE
%doc README.md
%{_bindir}/c3c
%{_prefix}/lib/c3

%changelog
* Sun Mar 22 2026 Fedora COPR <sisyphus1813@protonmail.com> 0.7.10-3
- Patch only applies to F44 now.
