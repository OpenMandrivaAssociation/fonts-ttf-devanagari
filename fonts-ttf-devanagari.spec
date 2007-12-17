Summary: Devanagari TTF font(s)
Name: fonts-ttf-devanagari
Version: 1.0
Release: %mkrel 1
License: Free use and distribution
Group: System/Fonts/True type
# it was previously distributed with XFree86; it's in public domain
Source0: raghu.ttf.bz2
#URL: 
BuildArch:	noarch
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

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
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
  [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
#%doc %{name}-%{version}/README*
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/devanagari
%_datadir/fonts/TTF/devanagari/*.ttf




