Summary:	Vomit - voice over misconfigured internet telephones
Name:		vomit
Version:	0.2c
Release:	%mkrel 7
License:	BSD
Group:		Networking/Other
URL:		http://vomit.xtdnet.nl/
Source:		http://vomit.xtdnet.nl/%{name}-%{version}.tar.bz2
Patch0:		vomit-remove-old-libevent-code.patch
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The vomit utility converts a Cisco IP phone conversation into a wave file
that can be played with ordinary sound players. Vomit requires a tcpdump
output file. Vomit is not a VoIP sniffer also it could be but the naming
is probably related to H.323.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/vomit
%{_mandir}/*/vomit.*


%changelog
* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 0.2c-7mdv2011.0
+ Revision: 647011
- add gentoo patch to build with latest libevent

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libevent 2.x

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2c-6mdv2010.0
+ Revision: 445707
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2c-5mdv2009.1
+ Revision: 298449
- rebuilt against libpcap-1.0.0

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.2c-4mdv2009.0
+ Revision: 269668
- rebuild early 2009.0 package (before pixel changes)

* Wed May 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2c-3mdv2009.0
+ Revision: 207056
- rebuilt against libevent-1.4.4

* Sun Dec 30 2007 Funda Wang <fwang@mandriva.org> 0.2c-2mdv2008.1
+ Revision: 139487
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.2c-1mdv2007.0
+ Revision: 103804
- Import vomit

* Tue Apr 11 2006 Stefan van der Eijk <stefan@mandrake.org> 0.2c-1mdk
- initial package

