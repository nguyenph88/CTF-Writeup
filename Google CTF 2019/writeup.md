## Google CTF 2019

Google CTF 2019: Google runs a CTF competition in two rounds: an online qualification round and an onsite final round. The top 10 teams from the qualification round will be invited to the finals to compete onsite for a prize pool of more than USD $31,337. In addition to the grand prizes, some of the best and creative write-ups that we receive during the qualifying round will be rewarded as well. We want to give you an opportunity to share with the world the clever ways you solve challenges. You can read more about the Google CTF here.

URL: https://capturetheflag.withgoogle.com/

# Beginner's Quests

The challenge is as easy as ... compiling the python code to get the flag:

> python3 -c "for i in [102, 108, 97, 103, 123, 119, 101, 108, 99, 111, 109, 101, 95, 112, 97, 114, 116, 105, 99, 105, 112, 97, 110, 116, 115, 33, 125]: print(chr(i), end='')"

![](img/beginnerquest.png)

# uhhMAZEin

We are provided with a pcap file and a nc: `nc challenges.ctfd.io 30035`

**Recon:** When I see PCAP, I also see package-sniffing and Wireshark is a useful toy for such. By nc-ing to the above, I'm asked to enter the list of sequences (LEFT, RIGHT, STRAIGHT). It may be obtained from the PCAP file.

Upon opening the file using Wireshark, we can see a lot of traffic on TCP. To filter out garbage, I use this filter: `tcp and not tcp.len==0` to remove the package with no data and show only the package with response.

![](img/2-filter.png)

Now we need to show all the package's content in one view. To do that, right click on any package and select `Streaming > TCP Stream`. 

![](img/2-stream.png)

Now we got all the message. You can type them manually but since i'm I save the response to package.txt and pipe the grep to the nc above:
`(grep 'LEFT, RIGHT, or STRAIGHT:' package.txt | sed 's/^.*: //') | nc challenges.ctfd.io 30035`
