Name:		texlive-grffile
Version:	52756
Release:	2
Summary:	Extended file name support for graphics (legacy package)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grffile
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The original package extended the file name processing of
package graphics to support a larger range of file names. The
base LaTeX code now supports multiple dots and spaces, and this
package by default is a stub that just loads graphicx. However,
\usepackage{grffile}[=v1] may be used to access version 1(.18)
of the package if that is needed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/grffile
%{_texmfdistdir}/tex/latex/grffile
%doc %{_texmfdistdir}/doc/latex/grffile

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
