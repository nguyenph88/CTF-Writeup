# CheatSheet

## NMAP
`nmap -sC -sV -oA file_name ip`

I.e:
`nmap -sC -sV -oA Devel 10.10.10.5`

## WFUZZ 
Remember to use the dictionary in `/usr/share/SecList/` or `/usr/share/wfuzz`

Fuzz with 1 param
`wfuzz -z file,wordlist/others/common_pass.txt --hs error "website/FUZZ"`

Fuzz with ID in range
`wfuzz -z range,1-65600 --hc 500  "http://IP:PORT/dir?parameter=id&port=FUZZ"`

## REVERSING
For simple string, use Immunity Debugger:
`https://cramhack.com/2018/09/11/htbfind-the-easy-pass-using-immunity/`