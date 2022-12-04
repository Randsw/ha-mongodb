# -*- mode: ruby -*-
# vi: set ft=ruby :
$mongodb_instance_num = 5
$vm_ip_addr_start = 230
#$bridge = "wlxa0a3f0908fbc" #name of network interface with internet connection 
$bridge = "wlp2s0" #name of network interface with internet connection 
$vm_cidr = "192.168.0" # virtual machines CIDR
Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu2004"
    config.vm.box_check_update = false
    (1..$mongodb_instance_num).each do |i|
        config.vm.define "mongodb-#{i}" do |node|
            node.vm.network "public_network", ip: "#{$vm_cidr}.#{$vm_ip_addr_start+i}", bridge: $bridge
            node.vm.hostname = "mongodb-#{i}"
            node.vm.provider "virtualbox" do |vb|
                vb.gui = false
                vb.memory = "2048"
                vb.cpus=1
            end
        end
    end
end