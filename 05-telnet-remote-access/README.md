# Telnet Remote Access

## Objective

Configure password-protected Telnet access for a lab router.

## Topology

```text
Admin PC --- Switch --- R0
```

## Addressing / Planning

| Device | Address |
|---|---|
| R0 G0/0 | 192.168.60.1/24 |
| Admin PC | 192.168.60.10/24 |

## Configuration

Configuration files: `configs/R0.txt`

## Verification

- `ping 192.168.60.1`
- `telnet 192.168.60.1`
- `show users`

## Expected Result

The lab should meet the stated objective without introducing unrelated configuration.

## What I Learned

VTY lines control remote terminal access. Telnet is insecure and is used here only for an isolated lab; SSH is preferred in real networks.
