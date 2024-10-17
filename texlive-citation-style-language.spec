Name:		texlive-citation-style-language
Version:	72292
Release:	1
Summary:	Bibliography formatting with Citation Style Language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/citation-style-language
License:	mit cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citation-style-language.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citation-style-language.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Citation Style Language (CSL) is an XML-based language that
defines the formats of citations and bibliography. There are
currently thousands of styles in CSL including the most widely
used APA, Chicago, Vancouver, etc. The citation-style-language
package is aimed to provide another reference formatting method
for LaTeX that utilizes the CSL styles. It contains a citation
processor implemented in pure Lua (citeproc-lua) which reads
bibliographic metadata and performs sorting and formatting on
both citations and bibliography according to the selected CSL
style. A LaTeX package (citation-style-language.sty) is
provided to communicate with the processor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/tex/latex/citation-style-language
%{_texmfdistdir}/scripts/citation-style-language
%doc %{_texmfdistdir}/doc/latex/citation-style-language
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
