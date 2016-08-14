# MR. Robot 1

----
## Gathering information

- Get the target's IP Address first: 
`$ netdiscover`
- Need to find the open ports:
`$ nmap -p1-65535 -A -T4 -sS -sU target_ip`
- Nothing much, so i needed to dig even more:
`$ nikto -output MrRobot.xml -host target_ip`

- There are some text files, now we are talking:
`$ wget http://target_ip/license.txt`
`$ wget http://target_ip/robots.txt`

- Did another wpscan to make sure:
`wpscan --url target_ip`

## What are those text files?

- `license.txt` has a base64 decoded string, so we need to decode it:
`$ echo "ZWxsaW90OkVSMjgtMDY1Mgo=" | base64 --decode
`
- Now we got `elliot:ER28-0652`
- `robots.txt` shows a key (what we need) and a dic. Lets save it:
`$ wget http://target_ip/fsociety.dic`
`$ wget http://target_ip/key-1-of-3.txt`

## Signin and Uploading shell
- Use the credential above I could be able to sign in to wordpress
- First thing first, I need to upload a shell, by using the plugin for wordpress I could be able to do so.
- With the shell, I found `key-2-of-3.txt` but I couldn't open it. There is also a `password.raw-md5` so lets play with it.

## Cracking password.raw-md5
- Used rainbow table I could be able to find that decrypted string. But I couldn't sign in with the second password.
- I'm stuck couldn't go any further