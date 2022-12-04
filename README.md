# HA PostgreSQL Cluster under Patroni control

![CI workflow](https://github.com/randsw/HA-mongodb/actions/workflows/mongo-db-install-ci.yaml/badge.svg)

## Deploy

### Start vagrant VM

`vagrant up`

### Deploy HA mongodb cluster

`ansible-playbook -i inventories/ha-mongodb/hosts.yml mondodb-rs-deploy.yml`
