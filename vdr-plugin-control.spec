%define plugin	control

Summary:	VDR plugin: Control VDR over terminal or telnet
Name:		vdr-plugin-%plugin
Version:	0.0.2a
Release:	20
Group:		Video
License:	GPL
URL:		https://ricomp.de/vdr/
Source:		http://ricomp.de/vdr/vdr-%plugin-%{version}.tgz
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-control/control-0.0.2a.patch
Patch2:		02_gateway.dpatch
Patch3:		93_control-0.0.2a-1.5.0.dpatch
Patch4:		control-const-char-gcc4.4.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The 'control' plugin brings the ability to VDR to control
the whole OSD over a telnet client.

%prep
%setup -q -n %plugin-%{version}
%patch1 -p1 -b .1318
%patch2 -p1
%patch3 -p1
%patch4 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# tty to control vdr per virtual terminal
# default: none
var=TERMINAL
param=--terminal=TERMINAL
# port to receive remote connections
# default: 2002
var=PORT
param=--port=PORT
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY TODO




