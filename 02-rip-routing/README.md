# RIP Routing

## Objective

Advertise two LANs dynamically between two routers using RIPv2.

## Topology

```text
PC1 --- R0 === R1 --- PC2
```

## Addressing / Planning

| Device | Interface | IP Address | Mask |
|---|---|---|---|
| R0 | G0/0 | 192.168.10.1 | 255.255.255.0 |
| R0 | G0/1 | 10.0.0.1 | 255.255.255.252 |
| R1 | G0/1 | 10.0.0.2 | 255.255.255.252 |
| R1 | G0/0 | 192.168.20.1 | 255.255.255.0 |

## Configuration

Configuration files: `configs/R0.txt`, `configs/R1.txt`

## Verification

- `show ip protocols`
- `show ip route rip`
- `show ip route`
- ping between LAN hosts

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

RIPv2 exchanges routes automatically and uses hop count as its metric.
