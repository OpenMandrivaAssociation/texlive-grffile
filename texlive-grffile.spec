%global tl_name grffile
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Extended file name support for graphics (legacy package)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grffile
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grffile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The original package extended the file name processing of package
graphics to support a larger range of file names. The base LaTeX code
now supports multiple dots and spaces, and this package by default is a
stub that just loads graphicx. However, \usepackage{grffile}[=v1] may be
used to access version 1(.18) of the package if that is needed.

