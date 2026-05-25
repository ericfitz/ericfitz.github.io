+++
title = "IPv6 is mainly just an IoT protocol"
date = 2025-01-04
+++

I've been struggling for a couple of years to try to get IPv6 support for my home.  I use Frontier as my ISP.  Frontier doesn't support residential IPv6 in my area.  I tried tunneling via Hurricane Electric (you should try this) but it was not satisfying and was way too much work.

So I bought Starlink as a "backup" :-) ISP, which natively supports IPv6.

Unfortunately I use Ubiquiti Unifi for my home networking and WiFi, and their support for IPv6 is a barely-implemented afterthought.

I want a simple configuration:
1. All IPv4 routes through Frontier, except if there's a Frontier outage, in which case it routes through Starlink as a backup.
2. All IPv6 routes through Starlink only.

Believe it or not, you cannot accomplish this with Unifi without SSHing into the device and modifying the routing tables, which changes will be lost when you reboot the device.

So I bought a Microtik full-featured router (their Cloud Core router is a steal) and am transitioning.

Back from my aside, thinking long and hard about IPv6, I realize that it's only well supported when it's invisible - either in mDNS or in IoT protocols like Matter.

Why is IPv6 not adopted after decades?  (1) Tech debt - too hard to adapt old devices and no one wants to throw them away, and (2) NAT, especially CGNAT, is too good.

Will IPv6 ever "break through"?   Maybe, if the wireless carriers or ISPs see a use for it, and even then they might make it relatively invisible to users/apps/devices.   The only thing I really see driving IPv6 is if someone invents some killer app or technology that just won't work on IPv4.  If everyone wants it bad enough, then consumer demand will drive adoption.  Otherwise it will be running silently in the background doing IoT-like stuff and reducing setup burden for consumers and support costs for ISPs in home networks, but not much else.
