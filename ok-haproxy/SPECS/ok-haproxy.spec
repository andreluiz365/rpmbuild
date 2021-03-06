%define haproxy_home /opt/haproxy

%define haproxy_version 1.5.14
%define haproxy_revision 01

#---------------------------------------------------------------------------------
Name:           ok-haproxy
License:        GPL v2
Group:          Development
Summary:        The Reliable, High Performance TCP/HTTP Load Balancer
Version:        %{haproxy_version}
Release:        %{haproxy_revision}
URL:            http://haproxy.1wt.eu/
Source0:        haproxy-%{version}.tar.gz
Source1:        haproxy.init
Source2:        generate-haproxy-config

BuildRequires:  gcc >= 3.4.6
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel
BuildRequires:  openssl-devel

Requires: 	zlib
Requires: 	pcre
Requires: 	openssl

%description
The Reliable, High Performance TCP/HTTP Load Balancer

#---------------------------------------------------------------------------------
%files
%defattr(-,root,root)
%{haproxy_home}
/etc/rc.d/init.d/haproxy

#---------------------------------------------------------------------------------
%prep
%setup -n haproxy-%{version}

#---------------------------------------------------------------------------------
%build
make TARGET=linux26 PREFIX=%{haproxy_home} USE_PCRE=1 USE_REGPARM=1

%install
rm -rf %{buildroot}

install -D -m 755 ./haproxy %{buildroot}%{haproxy_home}/bin/haproxy-%{haproxy_version}
install -D -m 755 $RPM_SOURCE_DIR/haproxy.init %{buildroot}/etc/rc.d/init.d/haproxy
install -D -m 755 $RPM_SOURCE_DIR/generate-haproxy-config %{buildroot}%{haproxy_home}/conf/generate-haproxy-config

#---------------------------------------------------------------------------------
%post
ln -sf %{haproxy_home}/bin/haproxy-%{haproxy_version} %{haproxy_home}/bin/haproxy

#---------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}

%changelog
* Thu Jul 9 2015 Vadzim Tonka <vtonko@swiftype.net> - 1.5.14-01
- Bump up haproxy version

* Sat Feb 22 2014 Oleksiy Kovyrin <alexey@kovyrin.net> - 1.4.24-02
- Fixed startup script to perform graceful restarts.

* Thu Aug 22 2013 Oleksiy Kovyrin <alexey@kovyrin.net> - 1.4.24-01
- Upgraded haproxy to 1.4.24.
