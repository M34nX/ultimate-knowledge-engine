# Security Policy

## Scope

Reports may concern the website, build pipeline, validation tools, dependency configuration, code examples, or handling of user-provided content.

## Reporting a vulnerability

Do not publish exploit details, credentials, personal data, or proof-of-concept payloads in a public issue. Use GitHub private vulnerability reporting when enabled. Otherwise, contact the repository owner through a verified private channel.

Include the affected component and version/commit, impact and preconditions, minimal reproduction details, and a suggested mitigation if known.

## Security principles

- Never run untrusted code in the website process.
- Any future playground must use isolated infrastructure, strict resource limits, timeouts, and network restrictions.
- Do not store secrets in the repository.
- Review dependencies and pin versions where practical.
- Validate content and metadata before publication.
- Treat external links and imported data as untrusted.
- Keep security material defensive, lawful, and educational.

Do not test against systems without explicit permission.
