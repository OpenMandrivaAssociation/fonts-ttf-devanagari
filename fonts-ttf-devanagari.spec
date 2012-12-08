Summary: Devanagari TTF font(s)
Name: fonts-ttf-devanagari
Version: 1.0
Release: %mkrel 8
License: Free use and distribution
Group: System/Fonts/True type
# it was previously distributed with XFree86; it's in public domain
Source0: raghu.ttf.bz2
#URL: 
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

%description
This package contains fonts for the devanagari script.

%prep
#%setup -c 

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}

%build
cd %{name}-%{version}
bzcat %{SOURCE0} > raghu.ttf

%install
cd %{name}-%{version}
rm -rf %buildroot
install -d %buildroot/%_datadir/fonts/TTF/devanagari

for i in `find . -name "*.ttf"` ; do
install -m 644 $i %buildroot/%_datadir/fonts/TTF/devanagari
done

%post
touch %{_datadir}/fonts/TTF

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
#%doc %{name}-%{version}/README*
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/devanagari
%_datadir/fonts/TTF/devanagari/*.ttf






%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-7mdv2011.0
+ Revision: 675414
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-6
+ Revision: 675178
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-5
+ Revision: 664326
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2011.0
+ Revision: 605193
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-3mdv2010.1
+ Revision: 494135
- fc-cache is now called by an rpm filetrigger

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 220861
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-1mdv2008.1
+ Revision: 125118
- kill re-definition of %%buildroot on Pixel's request


* Wed Jan 17 2007 Pablo Saratxaga <pablo@mandriva.com> 1.0-1mdv2007.0
+ Revision: 109837
- initial rpm package
- Create fonts-ttf-devanagari

