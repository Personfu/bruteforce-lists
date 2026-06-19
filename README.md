# bruteforce-lists

> Authorized password-audit and bug-bounty wordlist reference for scoped testing, CTFs, and defensive credential-hardening exercises.

## Portfolio role

This repository is a dual-use wordlist collection. In the FLLC / PersonFu portfolio it should be treated as a **bug-hunter audit support repo**, not a credential-stuffing kit.

Use it for:

- CTFs and training labs;
- owned systems;
- written authorization scopes;
- password policy audits;
- lockout/rate-limit validation;
- defensive detection engineering;
- bug bounty programs that explicitly permit credential or authentication testing.

Do not use it for:

- unauthorized login attempts;
- credential stuffing;
- third-party services outside scope;
- bypassing lockout controls;
- harvesting or replaying leaked credentials.

## Professional workflow

Before using any list, define the test scope:

```text
Program / customer:
Written authorization:
Allowed domains / hosts:
Allowed account types:
Rate limit:
Lockout rules:
Test window:
Notification contact:
Data handling rules:
```

## Bug-hunter use cases

| Use case | Goal | Evidence to capture |
| --- | --- | --- |
| Password policy audit | Identify weak policy rules in owned apps | Policy config, test account evidence |
| Lockout validation | Confirm lockout and throttling work | Timestamped request counts, lockout proof |
| Rate-limit testing | Validate auth endpoint abuse resistance | Safe request-rate notes, response headers |
| CTF practice | Learn authentication attack patterns legally | Lab notes and solved challenge summary |
| Detection engineering | Generate telemetry for blue-team alerts | Logs, SIEM query, alert screenshot |

## FLLC upgrade path

### 1. Classify lists

Add metadata for every list:

```json
{
  "file": "example.txt",
  "category": "passwords | usernames | devices | ctf | audit",
  "risk": "low | medium | high",
  "recommended_scope": "ctf-only | owned-lab | authorized-audit",
  "notes": "short use guidance"
}
```

### 2. Add audit-safe tooling

Future helper scripts should default to safety:

- dry-run counts;
- duplicate removal;
- entropy scoring;
- policy compliance checks;
- no network requests by default;
- rate-limit reminders;
- report generation.

### 3. Add defensive outputs

The best FLLC use is turning offensive pressure into defensive evidence:

- lockout configuration checklist;
- password policy scorecard;
- authentication telemetry checklist;
- SIEM alert ideas;
- remediation report template.

## Website integration

Feature as:

- `Authentication Audit Wordlists` under Security Arsenal.
- `Password Policy and Lockout Validation` member lab.
- `Bug Bounty Auth Testing Scope Checklist` blog post.

## Credits

This repository may include upstream/community wordlists. Preserve upstream credits and licenses where present.

## Safety notice

Wordlists are not inherently illegal, but misuse can cause harm and violate law, policy, and platform terms. Keep testing scoped, throttled, logged, and authorized.
