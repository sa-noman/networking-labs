# DHCP

## Objective

Configure a router as a DHCP server for a client LAN.

## Topology

```text
R0 --- Switch --- PC1 / PC2
```

## Addressing / Planning

| Device | Interface | IP Address | Mask |
|---|---|---|---|
| R0 | G0/0 | 192.168.30.1 | 255.255.255.0 |
| PC1 | NIC | DHCP | DHCP |
| PC2 | NIC | DHCP | DHCP |

## Configuration

Configuration files: `configs/R0.txt`

## Verification

- `show ip dhcp binding`
- `show ip dhcp pool`
- `ipconfig on PCs`
- `ping 192.168.30.1`

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

DHCP automates host addressing while exclusions protect infrastructure addresses.
