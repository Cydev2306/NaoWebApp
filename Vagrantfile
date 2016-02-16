Vagrant.configure(2) do |config|
  config.vm.box = "ARTACK/debian-jessie"
  config.vm.provision "shell", path: "provision.sh"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder "./www", "/var/www", owner: "root", group: "root"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
    v.name ="Server Nao"
  end
  config.vm.network "private_network", ip: "172.28.128.3"
  config.vm.network :public_network, bridge: "en4: Ethernet Thunderbolt"

end
