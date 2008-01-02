Summary: MacPorts allows installing software on Mac OS X (and other platforms)
Name: macports
Version: 1.6.0RC2
Release: %mkrel 1
License: BSD
Group: System/Base
URL: http://www.macports.org
Source: http://svn.macosforge.org/repository/macports/distfiles/MacPorts/MacPorts-%{version}.tar.bz2
Prefix: /opt/local
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: curl tcl rsync coreutils make
BuildRequires: curl-devel tcl-devel sqlite3-devel gcc-objc gnustep-base gnustep-base-devel
BuildRequires: mtree fakeroot gnustep-make libx11-devel
BuildRequires: openssl-devel

%description
MacPorts is a system for compiling, installing, and managing free and
open source software. A MacPorts "port" is a set of specifications
contained in a Portfile that defines an application, its characteristics,
and any files or special instructions required to install it, so MacPorts
may automatically fetch, patch, compile, and install ported software.

MacPorts may also be used to pre-compile ported software into binaries
that may be installed on remote computers. Binaries of ported software
may be installed very quickly since the steps required to install ports
from source code have all been performed in advance.

%prep
%setup -qn MacPorts-%{version}
# avoid the whole upgrade and information procedure
perl -pe 's/^install::/interactive:/' -i Makefile.in

%define _prefix         %{prefix}
%define _bindir         %{prefix}/bin
%define _sysconfdir     %{prefix}/etc
%define _datadir        %{prefix}/share
%define _mandir         %{prefix}/share/man
%define _infodir        %{prefix}/share/info
%define _localstatedir  %{prefix}/var

%build
source /usr/share/GNUstep/Makefiles/GNUstep.sh
%configure \
        --without-included-tclthread --without-included-sqlite3 \
        --with-objc-runtime=GNU --with-objc-foundation=GNUstep
%make

%install
source /usr/share/GNUstep/Makefiles/GNUstep.sh
rm -rf $RPM_BUILD_ROOT
%makeinstall_std \
        DESTDIR="$RPM_BUILD_ROOT" INSTALL="fakeroot install"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE ChangeLog
%{_bindir}/port
%{_bindir}/portf
%{_bindir}/portindex
%{_bindir}/portmirror
%config(noreplace) %{_sysconfdir}/macports
%doc %{_mandir}/man1/port.1*
%doc %{_mandir}/man5/macports.conf.5*
%doc %{_mandir}/man7/portfile.7*
%doc %{_mandir}/man7/portgroup.7*
%doc %{_mandir}/man7/porthier.7*
%doc %{_mandir}/man7/portstyle.7*
%{_datadir}/macports
%{_localstatedir}/macports
/usr/lib/tcl8.5/macports1.0
#### mtree
%dir %{prefix}
%dir %{prefix}/bin
%dir %{prefix}/etc
%dir %{prefix}/include
%dir %{prefix}/lib
%dir %{prefix}/libexec
%dir %{prefix}/man
%dir %{prefix}/sbin
%dir %{prefix}/share
%dir %{prefix}/share/info
%dir %{prefix}/share/man
%dir %{prefix}/share/man/cat?
%dir %{prefix}/share/man/man?
%dir %{prefix}/share/nls
%dir %{prefix}/share/nls/*
%dir %{prefix}/var
