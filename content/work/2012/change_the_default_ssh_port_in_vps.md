# Change the default ssh port in VPS server

- date: 2012-12-20 15:30
- category: work
- tags: ssh, vps

---------------- 

A friend told me that my VPS is using the default port 22. And that is too dangerous. because there are so many crackers trying to break your server's root password using some kind of sniffing software. 

I have just bought my VPS server just a couple of days. So I didn't make so many changes on the server. Just a new installation of Ubuntu Server 12.04 LTS 64bit version. 

These are some code searching from google to determine how many password failure on ssh connection to the server.

```bash
$ cat /var/log/auth.log* | grep "Failed password" | wc -l
```

it just do a simple `cat` and `grep` then count the lines using `wc -l `

to my surprise, this command shows that there are more than **804 Failed Passwor** logs in `auth.log`. Holy crap, I just started using this server for less than a week.

So, I googled some solution, first change the ssh port switching it to other ports that not used by system. Edit the `/etc/ssh/sshd_config` file with your favourite editor.

```bash
$ sudo vim /etc/ssh/sshd_config
```

find this line and change the Port 22 to other ports you want.

```bash
# What ports, IPs and protocols we listen for
Port 22
```

then restart the ssh process.

```bash
$ sudo service ssh reload
```

ok thing getting done. only change port doesn't really help to prevent all the risks for ssh password cracking. I found a tool called  `fial2ban` <http://en.wikipedia.org/wiki/Fail2ban>. it's easy to use and install to the system.

just type

```bash
$ sudo apt-get install fail2ban
```

and the detail configuration are in `/etc/fail2ban/jail.conf` I didn't running too many services on my vps, so the default settings are good for me. you can set how many times you can try to guess the password. with too much wrong password inputing. the system will ban the ip address of the attacker.

