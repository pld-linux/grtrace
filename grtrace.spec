Summary:	Tool to automatically generate grsecurity ACLs
Summary(pl):	Narzêdzie to automatycznego generowania ACL-i grsecurity
Name:		grtrace
Version:	1.0.1
Release:	1
License:	unknown, (c) 2001 Brad Spengler
Group:		Applications/System
Source0:	http://grsecurity.net/%{name}.tar.gz
# Source0-md5:	c93cb81c07b66e31ff208eef68989987
Patch0:		%{name}-fix.patch
URL:		http://grsecurity.net/
Requires:	strace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
grtrace is to be used to automatically generate grsecurity ACLs for
any binary or running process on your system. It detects needed
capabilities and required file permissions.

%description -l pl
grtrace s³u¿y do automatycznego generowania ACL-i grsecurity dla
dowolnej binarki lub dzia³aj±cego procesu w systemie. Wykrywa
potrzebne capabilities oraz uprawnienia do plików.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o grtrace grtrace.c tracesort.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install grtrace $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/grtrace
