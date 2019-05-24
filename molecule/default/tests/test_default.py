import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_audit_pkg(host):
    pkg = host.package('audit')
    assert pkg.is_installed


def test_audit_service(host):
    vrt = host.ansible("setup")["ansible_facts"]["ansible_virtualization_type"]
    if vrt != 'docker':
        srv = host.service('auditd')
        assert srv.is_running
        assert srv.is_enabled
