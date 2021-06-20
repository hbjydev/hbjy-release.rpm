# hbjy-release.rpm

An RPM spec to install the repository and GPG keys for my personal RPM
repository, at https://rpm.hbjy.io

## Building

To build, you will need two packages on a Fedora or Rocky Linux machine:

- `mock`
- `rpmdevtools`

Once you have cloned the repository into your rpmbuild/ directory, you can
perform the steps required to build the package.

```shell
# build srpm
$ rpmbuild -bs SPECS/hbjy-release.spec

# build rpm with mock
$ mock -r epel-8-x86_64 --rebuild SRPMS/hbjy-release-*.src.rpm
```

With this command, your output should be in
`/var/lib/mock/epel-8-x86_64/result/`. This should include a `build.log` and
`hbjy-release-*.rpm` file. You can install said `.rpm` file with `rpm`.

