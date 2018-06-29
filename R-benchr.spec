#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-benchr
Version  : 0.2.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/benchr_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/benchr_0.2.0.tar.gz
Summary  : High Precise Measurement of R Expressions Execution Time
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-benchr-lib
Requires: R-Rcpp
Requires: R-RcppProgress
Requires: R-ggplot2
BuildRequires : R-Rcpp
BuildRequires : R-RcppProgress
BuildRequires : R-ggplot2
BuildRequires : clr-R-helpers

%description
the execution time of R expressions.

%package lib
Summary: lib components for the R-benchr package.
Group: Libraries

%description lib
lib components for the R-benchr package.


%prep
%setup -q -c -n benchr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530311157

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530311157
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library benchr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library benchr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/benchr/DESCRIPTION
/usr/lib64/R/library/benchr/INDEX
/usr/lib64/R/library/benchr/Meta/Rd.rds
/usr/lib64/R/library/benchr/Meta/features.rds
/usr/lib64/R/library/benchr/Meta/hsearch.rds
/usr/lib64/R/library/benchr/Meta/links.rds
/usr/lib64/R/library/benchr/Meta/nsInfo.rds
/usr/lib64/R/library/benchr/Meta/package.rds
/usr/lib64/R/library/benchr/NAMESPACE
/usr/lib64/R/library/benchr/NEWS.md
/usr/lib64/R/library/benchr/R/benchr
/usr/lib64/R/library/benchr/R/benchr.rdb
/usr/lib64/R/library/benchr/R/benchr.rdx
/usr/lib64/R/library/benchr/help/AnIndex
/usr/lib64/R/library/benchr/help/aliases.rds
/usr/lib64/R/library/benchr/help/benchr.rdb
/usr/lib64/R/library/benchr/help/benchr.rdx
/usr/lib64/R/library/benchr/help/paths.rds
/usr/lib64/R/library/benchr/html/00Index.html
/usr/lib64/R/library/benchr/html/R.css
/usr/lib64/R/library/benchr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/benchr/libs/benchr.so
/usr/lib64/R/library/benchr/libs/benchr.so.avx2
/usr/lib64/R/library/benchr/libs/benchr.so.avx512
