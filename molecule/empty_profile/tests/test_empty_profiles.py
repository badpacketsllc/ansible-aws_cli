import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aws_cli_should_be_installed(host):
    assert host.run('aws --v').rc == 0


def test_aws_cli_folder_should_not_exist(host):
    assert not host.file('/root/.aws').is_directory
