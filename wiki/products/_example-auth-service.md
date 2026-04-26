---
product: auth-service
status: Production
adoption: 12
last_updated: 2026-04-25
sources:
  - raw/roadmaps/2026-q2-platform-roadmap.md
  - raw/engineering/auth-service-arch.md
---

# Auth Service

<!-- This is an EXAMPLE. The leading `_` in the filename keeps it out of validator/index expectations.
     Use this as a worked reference; copy `_template.md` (not this file) when creating real product pages. -->

## Summary

Centralized authentication and authorization service for all internal products. Replaces five legacy auth implementations with a single OAuth2/OIDC layer plus role-based access control.

## Status & Maturity

Production. Used by 12 internal teams. Known gap: SAML support deferred from Q1 2026 to Q2 2026 (see `raw/roadmaps/2026-q2-platform-roadmap.md`).

## Key Capabilities

- OAuth2 / OIDC for human users
- Service-to-service tokens (mTLS + short-lived JWTs)
- RBAC with team-scoped roles
- Audit log integration with the central SIEM

## Adoption

12 internal teams, 3.4M monthly active end users. Top consumers: web-app (1.8M MAU), mobile-app (1.1M MAU), partner-portal (0.5M MAU).

## Dependencies

- **Depends on**: identity-provider, secrets-manager, audit-log
- **Depended on by**: web-app, mobile-app, partner-portal, internal-admin, billing-service

## Roadmap

| Quarter | Item | Status |
|---------|------|--------|
| Q1 2026 | Core OAuth2 flows | ✅ Shipped |
| Q1 2026 | RBAC v1 | ✅ Shipped |
| Q2 2026 | SAML federation | 🔜 In progress (slipped from Q1) |
| Q2 2026 | Just-in-time provisioning | Planned |

## Open Questions

- Does the SAML slip block the partner-portal Q2 launch?
- Do we need to support FIDO2 in 2026 or defer to 2027?

## Sources

- `raw/roadmaps/2026-q2-platform-roadmap.md`
- `raw/engineering/auth-service-arch.md`
