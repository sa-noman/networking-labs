# Static Routing

## Objective

Connect two LANs through two routers using static routes.

## Topology

```text
PC1 --- R0 --- R1 --- PC2
```

## Addressing / Planning

| Device | Interface | IP Address | Mask | Gateway |
|---|---|---|---|---|
| PC1 | NIC | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| R0 | G0/0 | 192.168.10.1 | 255.255.255.0 | - |
| R0 | G0/1 | 10.0.0.1 | 255.255.255.252 | - |
| R1 | G0/1 | 10.0.0.2 | 255.255.255.252 | - |
| R1 | G0/0 | 192.168.20.1 | 255.255.255.0 | - |
| PC2 | NIC | 192.168.20.10 | 255.255.255.0 | 192.168.20.1 |

## Configuration

Configuration files: `configs/R0.txt`, `configs/R1.txt`

## Verification

- `show ip interface brief`
- `show ip route`
- `ping 192.168.20.10 from PC1`
- `ping 192.168.10.10 from PC2`

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

Static routes explicitly define next hops and are easy to reason about in small networks.
