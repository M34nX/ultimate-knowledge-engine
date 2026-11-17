---
id: build-from-scratch.search-engine
title: "Build a Small Search Engine"
content_type: project
locale: en
domain: computer-science
level: intermediate
status: draft
learning_objectives:
  - "Normalize documents and tokenize text while retaining source paths."
  - "Build an inverted index for terms, documents, and positions."
  - "Process queries and rank results with a documented score."
  - "Evaluate relevance using a small query set."
  - "Respect document permissions and keep indexing local."
prerequisites:
  - "Strings, maps, and sets"
  - "Sorting"
  - "Basic probability"
milestones:
  - "Index a folder of public sample text."
  - "Implement exact-term search."
  - "Rank documents using a documented score."
  - "Show snippets and source paths."
  - "Evaluate results with a documented query set."
---

# Build a Small Search Engine

**Level:** Intermediate · **Language:** Python · **Status:** Draft

## Outcome
Build a local search tool for a small document collection. Tokenize text, create an inverted index, and rank results transparently.

## Prerequisites
Strings, maps, sets, sorting, and basic probability.

## Lessons
1. **Documents and tokens:** normalize text carefully and preserve each source path.
2. **Inverted index:** map each term to documents and positions.
3. **Query processing:** tokenize a query and combine candidate document sets.
4. **Ranking:** begin with term frequency; extend to TF-IDF or BM25 after explaining assumptions.
5. **Evaluation:** create test queries and relevance judgments; measure precision at k.
6. **Quality:** handle duplicates, stop words, language-specific tokenization, and updates.

## Milestones
- M1: index a folder of public sample text.
- M2: implement exact-term search.
- M3: rank documents by a documented score.
- M4: show snippets and source paths.
- M5: evaluate with a documented query set.

## Privacy
Index only documents you are allowed to process. Keep this exercise local; do not collect private content or credentials.

## References
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/)
- [Elasticsearch documentation](https://www.elastic.co/guide/index.html)
- [Apache Lucene](https://lucene.apache.org/)
