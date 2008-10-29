Summary:	Vomit - voice over misconfigured internet telephones
Name:		vomit
Version:	0.2c
Release:	%mkrel 5
License:	BSD
Group:		Networking/Other
URL:		http://vomit.xtdnet.nl/
Source:		http://vomit.xtdnet.nl/%{name}-%{version}.tar.bz2
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

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/vomit
%{_mandir}/*/vomit.*
