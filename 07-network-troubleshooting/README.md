# Network Troubleshooting

## Objective

Use a repeatable workflow to diagnose common Packet Tracer connectivity failures.

## Topology

```text
PC --- Switch --- R0 --- R1 --- Server
```

## Addressing / Planning

| Check | Typical symptom |
|---|---|
| Physical/link | Interface down/down |
| IP addressing | Wrong subnet or duplicate address |
| Gateway | Local access works, remote fails |
| Routing | Router has no path to destination |
| ACL | Route exists but selected traffic fails |

## Configuration

Configuration files: `configs/R0.txt`

## Verification

- `ping loopback/local gateway`
- `ping next hop`
- `ping remote gateway`
- `traceroute destination`
- `compare routing table and ACLs`

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

Troubleshooting is faster when moving layer-by-layer instead of changing multiple settings at once.
