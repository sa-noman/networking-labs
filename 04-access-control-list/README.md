# Access Control List

## Objective

Use a standard ACL to block one host while permitting the rest of the LAN.

## Topology

```text
LAN 192.168.40.0/24 --- R0 --- Server LAN
```

## Addressing / Planning

| Device | Address |
|---|---|
| Blocked PC | 192.168.40.50 |
| Allowed PC | 192.168.40.60 |
| R0 LAN GW | 192.168.40.1 |
| Server | 192.168.50.10 |

## Configuration

Configuration files: `configs/R0.txt`

## Verification

- `show access-lists`
- `show ip interface g0/1`
- test blocked host
- test allowed host

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

ACL order matters because IOS evaluates entries top-down and stops at the first match.
