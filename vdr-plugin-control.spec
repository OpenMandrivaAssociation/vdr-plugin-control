
%define plugin	control
%define name	vdr-plugin-%plugin
%define version	0.0.2a
%define rel	16

Summary:	VDR plugin: Control VDR over terminal or telnet
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://ricomp.de/vdr/
Source:		http://ricomp.de/vdr/vdr-%plugin-%version.tar.bz2
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-control/control-0.0.2a.patch
Patch2:		02_gateway.dpatch
Patch3:		93_control-0.0.2a-1.5.0.dpatch
Patch4:		control-const-char-gcc4.4.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The 'control' plugin brings the ability to VDR to control
the whole OSD over a telnet client.

%prep
%setup -q -n %plugin-%version
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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2a-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- fix build with gcc4.4 (const-char-gcc4.4.patch)

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2a-15mdv2009.1
+ Revision: 359700
- rediff 1.5.0 patch
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-14mdv2009.0
+ Revision: 197915
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-13mdv2009.0
+ Revision: 197647
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix problems with telnet session (P2 from e-tobi)
- adapt for api changes of vdr 1.5.0 (P3 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-12mdv2008.1
+ Revision: 145054
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-11mdv2008.1
+ Revision: 103079
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-10mdv2008.0
+ Revision: 49985
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-9mdv2008.0
+ Revision: 42072
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-8mdv2008.0
+ Revision: 22734
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-7mdv2007.0
+ Revision: 90907
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-6mdv2007.1
+ Revision: 73979
- rebuild for new vdr
- Import vdr-plugin-control

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-1mdv2007.0
- initial Mandriva release

