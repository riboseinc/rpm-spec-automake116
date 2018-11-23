#!/bin/bash

ln -sf "$PWD" /usr/local/rpm-specs/automake116
ln -sf "$PWD" /usr/local/rpm-specs/automake116-automake

. /usr/local/rpm-specs/setup_env.sh

yum -y install scl-utils-build

build_package automake116

yum -y localinstall ~/rpmbuild/RPMS/*/{ribose-automake116-build-*.rpm,ribose-automake116-runtime-*.rpm}
build_package automake116-automake

