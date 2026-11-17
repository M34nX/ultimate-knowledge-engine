---
id: build-from-scratch.database-engine
title: "Build a Tiny Database Engine"
content_type: project
locale: en
domain: databases
level: intermediate
status: draft
learning_objectives:
  - "Represent tables, schemas, rows, and validated values."
  - "Implement insert, select, update, and delete."
  - "Compare linear scans with a simple index."
  - "Model rollback and file persistence."
  - "Test invalid input and document limitations."
prerequisites:
  - "Functions and classes or records"
  - "Maps, lists, and file I/O"
  - "Basic algorithm analysis"
milestones:
  - "Create tables and validate schemas."
  - "Insert rows and reject invalid values."
  - "Select rows with filters."
  - "Update and delete rows."
  - "Build and benchmark an index."
  - "Save, reload, and test rollback."
---

# Build a Tiny Database Engine

**Level:** Intermediate · **Language:** Python · **Status:** Draft

## Outcome
Build an in-memory teaching database with tables, schemas, insert/select/update/delete, a simple index, and file persistence. It is not a production database.

## Prerequisites
Functions, records or classes, maps, lists, file I/O, and basic algorithm analysis.

## Lessons
1. **Data model:** represent a table as a schema plus rows; validate column names and types.
2. **Queries:** implement a small command set before attempting a full SQL parser.
3. **Indexes:** compare linear scan with hash lookup; explain memory and write-cost trade-offs.
4. **Transactions:** model begin, commit, and rollback with snapshots or a change log.
5. **Persistence:** serialize data in a documented format and validate it on load.

## Milestones
- M1: create tables and validate schemas.
- M2: insert rows and reject invalid values.
- M3: select rows with equality filters.
- M4: update and delete rows.
- M5: build and benchmark a simple index.
- M6: save, reload, and test rollback.

## Practice
Explain why an index can speed up reads but increase memory use and write cost. Test duplicate keys, missing columns, malformed files, and empty tables.

## Acceptance
Operations have tests; invalid input is rejected safely; saved data can be reloaded; benchmark size and limitations are documented.

## References
- [SQLite documentation](https://www.sqlite.org/docs.html)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Database System Concepts](https://www.db-book.com/)

Do not claim ACID compliance or production readiness unless implemented and tested.
