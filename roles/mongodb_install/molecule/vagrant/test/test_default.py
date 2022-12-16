import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_listening_mongodb(host):
    assert host.socket("tcp://0.0.0.0:27017").is_listening

def test_mongodb_is_running(host):
    assert host.service('mongod').is_running

def test_mongodb_config_exist(host):
    mongodb_conf = host.file('/etc/mongod.conf')
    assert mongodb_conf.exists
    assert mongodb_conf.contains('bindIp: 0.0.0.0')
    assert mongodb_conf.contains('replSetName: rs0')
