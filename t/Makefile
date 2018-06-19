test: test-passwd test-group
test-gpgrid: test-passwd-gpgrid test-group-gpgrid
test-nova: test-passwd-nova test-group-nova

test-group:
	JPCONF=./config ../usr/sbin/json-fetchgroupdb --test

test-group-gpgrid:
	JPCONF=./config.gpgrid ../usr/sbin/json-fetchgroupdb --test

test-group-nova:
	JPCONF=./config.nova ../usr/sbin/json-fetchgroupdb --test

test-passwd:
	JPCONF=./config ../usr/sbin/json-fetchpasswddb --test

test-passwd-gpgrid:
	JPCONF=./config.gpgrid ../usr/sbin/json-fetchpasswddb --test

test-passwd-nova:
	JPCONF=./config.nova ../usr/sbin/json-fetchpasswddb --test

