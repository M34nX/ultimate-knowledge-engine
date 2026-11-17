# Build a Local Network Service

**Level:** Intermediate · **Language:** Python or JavaScript · **Status:** Draft

## Outcome
Build a small HTTP service on localhost with routes, input validation, structured responses, tests, and graceful shutdown.

## Prerequisites
Functions, JSON, HTTP basics, and command-line use.

## Lessons
1. **Client and server:** understand requests, responses, methods, paths, headers, and status codes.
2. **Routing:** map a small set of paths to handlers.
3. **Validation:** check request shape and reject invalid data.
4. **Errors and logs:** return consistent errors without exposing secrets or stack traces.
5. **Testing:** write local integration tests.
6. **Reliability:** add timeouts, bounded request sizes, and graceful shutdown.

## Milestones
- M1: return a health response on localhost.
- M2: add two routes and JSON output.
- M3: validate input and return suitable status codes.
- M4: test success and failure cases.
- M5: document configuration and safe shutdown.

## Safety boundary
Bind to localhost by default. Do not scan, probe, or send traffic to systems you do not own or have explicit permission to test. Do not collect credentials or personal data.

## References
- [MDN: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [HTTP Semantics — RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
