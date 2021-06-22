all: srpm build

srpm:
	mock -r epel-8-x86_64 --resultdir=srpm/ --buildsrpm --spec SPECS/hbjy-release.spec --sources=SOURCES/

build:
	mock -r epel-8-x86_64 --resultdir=dist/ --rebuild srpm/hbjy-release-*.src.rpm

