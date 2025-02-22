Summary:	Voice over misconfigured internet telephones
Name:		vomit
Version:	0.2c
Release:	10
License:	BSD
Group:		Networking/Other
Url:		https://vomit.xtdnet.nl/
Source0:	http://vomit.xtdnet.nl/%{name}-%{version}.tar.gz
Patch0:		vomit-remove-old-libevent-code.patch
BuildRequires:	dnet-devel
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(libevent)

%description
The vomit utility converts a Cisco IP phone conversation into a wave file
that can be played with ordinary sound players. Vomit requires a tcpdump
output file. Vomit is not a VoIP sniffer also it could be but the naming
is probably related to H.323.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{_bindir}/vomit
%{_mandir}/*/vomit.*

