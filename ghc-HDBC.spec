%global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define module HDBC

Summary:	Haskell Database Connectivity
Name:		ghc-%{module}
Version:	2.3.1.1
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(convertible)
BuildRequires:	haskell(mtl)
BuildRequires:	haskell(text)
BuildRequires:	haskell(utf8-string)
Requires(post,preun):	ghc
Requires(pre):	haskell(convertible)
Requires(pre):	haskell(mtl)
Requires(pre):	haskell(text)
Requires(pre):	haskell(utf8-string)
Obsoletes:	haskell-%{module} < 2.3.1.1-2

%description
HDBC provides an abstraction layer between Haskell programs and SQL relational
databases. This lets you write database code once, in Haskell, and have it work
with any number of backend SQL databases (MySQL, Oracle, PostgreSQL,
ODBC-compliant databases, etc.)

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

