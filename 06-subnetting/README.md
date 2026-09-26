# Subnetting

## Objective

Practice dividing 192.168.100.0/24 into four equal /26 networks.

## Topology

```text
Address-planning exercise
```

## Addressing / Planning

| Subnet | Network | Host Range | Broadcast |
|---|---|---|---|
| A | 192.168.100.0/26 | .1 - .62 | .63 |
| B | 192.168.100.64/26 | .65 - .126 | .127 |
| C | 192.168.100.128/26 | .129 - .190 | .191 |
| D | 192.168.100.192/26 | .193 - .254 | .255 |

## Configuration

Configuration files: No device configuration file is required for this exercise.

## Verification

- `confirm /26 mask = 255.255.255.192`
- `verify block size = 64`
- `verify no overlapping host ranges`

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

Subnetting turns address requirements into predictable network, host, and broadcast ranges.
