# Kringlecon 2018

I participated in this but haven't done a lot as I i didn't have much time.

----
## List of Challenge
1. Orientation Challenge
2. Directory Browsing
3. de Bruijn Sequences
4. Data Repo Analysis
5. AD Privilege Discovery
6. Badge Manipulation
7. HR Incident Response
8. Network Traffic Forensics
9. Ransomware Recovery
10. Who Is Behind It All?


----
## 1. Orientation Challenge

Escape_Key followed by  ":q"


## 2. Directory Browsing

- Inject the server ip
- Cat and explore the `onboard.db`
- Search for "Chan" last name
```
# !?ScottChan48 Colorado WayLos Angeles900674017533509scottmchan90067@gmail.comS```

- So Scott is the First Name.
- In CVS File, "Data Loss for Rainbow Teams" is  John McClane, that's it


## 3. de Bruijn Sequences

- 2 interesting things .secret folder and .viminfo file. Looking at poem.txt. Looking at the poem.txt it felt like Morcel Naugat had written the letter. However .viminfo  file revealed something interesting.  Seems the name is Elinore. 

- The next, i didn't have any answer


## 4. Data Repo Analysis

 - Using -u param, we got "directreindeerflatterystable". Use this combination: "report-upload"/"directreindeerflatterystable".
- Login and successfully upload the report.txt file.


#5. AD Privilege Discovery

- Run this command:
```curl -v --http2-prior-knowledge localhost:8080 -X POST -d "status=on"```
- No idea how to solve Active Directory


#6. Badge Manipulation

- Explore `event.dump`
- Will see `sparkle.redberry` and `minty.candycane`. minty.candycane is the right answer.
- Scanner has SQLi, this is the breakpoint:
```
1' OR '1'='1' LIMIT 8,1;# 
```
- Here we go:
```
{"data":"User Access Granted - Control number 19880715","request":true,"success":{"hash":"5588574fc6db4b7e6756f76d79da594a7bf569c543b1e9ddfd6275660f676ee4","resourceId":"55e12281-e571-4adf-bf2f-a51d345dcabd"}}
```


#7. HR Incident Response

- Use this with git:
```git log --pretty=oneline ```
- Here is the Pass: twinkletwinkletwinkle

