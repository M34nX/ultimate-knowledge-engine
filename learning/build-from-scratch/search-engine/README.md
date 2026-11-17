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
