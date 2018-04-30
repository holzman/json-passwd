test: test-passwd test-group

test-passwd:
	JPCONF=../etc/json-passwd/config.test ../usr/sbin/json-fetchpasswddb --test

test-group:
	JPCONF=../etc/json-passwd/config.test ../usr/sbin/json-fetchgroupdb --test
