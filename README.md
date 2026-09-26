# Networking Labs

![Cisco](https://img.shields.io/badge/Cisco-Networking-1BA0D7?logo=cisco&logoColor=white)
![Packet Tracer](https://img.shields.io/badge/Packet%20Tracer-Labs-2563EB)
![Focus](https://img.shields.io/badge/Focus-Routing%20%26%20Troubleshooting-6C63FF)

A practical collection of computer networking labs covering routing, addressing, DHCP, ACLs, remote access, subnetting, and troubleshooting. The configurations are written for Cisco IOS-style lab environments such as Cisco Packet Tracer.

## Labs

| # | Lab | Focus |
|---|---|---|
| 01 | Static Routing | Manual route configuration between LANs |
| 02 | RIP Routing | RIPv2 dynamic routing |
| 03 | DHCP | Automatic IPv4 host configuration |
| 04 | Access Control List | Basic traffic filtering |
| 05 | Telnet Remote Access | VTY and local authentication in an isolated lab |
| 06 | Subnetting | IPv4 subnet planning |
| 07 | Network Troubleshooting | Structured connectivity diagnosis |

## Repository Structure

```text
networking-labs/
├── 01-static-routing/
├── 02-rip-routing/
├── 03-dhcp/
├── 04-access-control-list/
├── 05-telnet-remote-access/
├── 06-subnetting/
├── 07-network-troubleshooting/
├── docs/
├── .github/workflows/validate.yml
├── scripts/validate_repo.py
└── README.md
```

## How to Use

1. Open the README for a lab.
2. Recreate the topology in Cisco Packet Tracer or a compatible Cisco IOS lab.
3. Apply the configurations from the `configs/` directory.
4. Run the verification commands listed in the lab.
5. Record screenshots or `.pkt` files locally if you want to extend the lab.

> Interface names may differ by router model. Adjust `g0/0`, `g0/1`, or other interfaces to match your Packet Tracer device.

## Security Note

The Telnet lab is intentionally included as a learning exercise. Telnet sends traffic without encryption and should not be used for real production administration. Prefer SSH in real environments.

## Validation

This repository includes a small validation script that checks the documentation structure and required configuration files.

```bash
python scripts/validate_repo.py
```

GitHub Actions runs the same validation automatically on pushes and pull requests.

## Future Labs

- VLANs and trunking
- Inter-VLAN routing
- OSPF
- NAT/PAT
- SSH remote access
- IPv6 addressing
- Multi-router troubleshooting
