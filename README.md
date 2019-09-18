# scam-database-attack

A set of python scripts to attack specific websites known to scam people

## What does this do

The sites are using jQuery for their website to take in information, however with the implementation of verifying information, there is a little catch.

For `skinamerica.fun` it would verify it against Steam itself, but this script rips out the verification and just spams data anyway, but does this rapidly in a DDoS fashion.

For `bsctmw.com` this just send random login information in a basic DDoS fashion.

## How to run

***Recommended to run with a VPN Active***

### Method 1: Run script standalone

*Perfect for machines with `python3` already installed*

1. Clone repo
2. Install dependencies
3. Run `.py` script for offending website

### Method 2: Prebuilt executable

*No fuss and works immediately with no `python3` installation*

## FAQ

Q: Is this illegal?

A: Yes.

Q: Why?

A: Why not.
