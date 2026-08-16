Si tu servidor esta Nuevo lo primero que debes hacer es 
1.	verificar que tenga un IP accesible:
 ```shell
 ip address
 ```
2.	Permitir conexones por SSH para poder administrarlo de manera remota:
```shell
sudo nano /etc/ssh/sshd_config
y habilitar:
ListenAddress 0.0.0.0
ListenAddress ::
PermitRootLogin yes
```
3.	Restaurar el servido de ssh:
```shell
sudo systemctl restart ssh
```
