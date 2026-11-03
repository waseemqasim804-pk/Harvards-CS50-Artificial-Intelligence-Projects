# Analysis

## Layer 4, Head 6

In Layer 4, Head 6, tokens appear to strongly attend to the word that immediately precedes them in the sequence (the previous token). Across multiple tested sentences, each word's highest attention weight is consistently assigned to the token at position `i - 1`, creating a distinct diagonal band immediately below the main diagonal in the attention matrix. For example, in the prepositional phrase "through a small [MASK]", the determiner "a" attends to the preposition "through" with an attention weight of 0.921, the adjective "small" attends to "a" with 0.549, and the masked token "[MASK]" attends to "small" with 0.681. Similarly, in the phrase "over the lazy [MASK]", "over" attends to "jumped" (0.934), "the" attends to "over" (0.900), "lazy" attends to "the" (0.521), and "[MASK]" attends to "lazy" (0.883).

This attention pattern serves as an immediate backward-looking sequence mechanism. While recurrent neural networks process sequences sequentially from left to right by design, Transformer architectures process all tokens simultaneously without inherent recurrence. Having dedicated attention heads that attend to the immediately preceding token allows the model to reconstruct local sequential order and track immediate antecedent context, such as recognizing bigram collocations, verb-particle combinations (e.g., "turned down", "picked up"), and modifier-noun adjacencies. Like many attention heads, it exhibits some noise: the first word in a sentence or major clause boundaries sometimes direct residual attention to the `[CLS]` token rather than the preceding word, but the dominant backward sequential pattern remains consistent across sentences.

Example Sentences:
- We turned down a narrow lane and passed through a small [MASK].
- The brown dog jumped over the lazy [MASK].
- Then I picked up a [MASK] from the table.

## Layer 8, Head 11

In Layer 8, Head 11, determiners (such as "a" and "the") appear to attend directly to the head nouns they modify, even when descriptive adjectives intervene between the determiner and the noun. In the noun phrase "a narrow lane", the determiner "a" concentrates an attention weight of 0.928 directly on the noun "lane", assigning only 0.013 to the intervening adjective "narrow". Likewise, in "the brown dog", the initial determiner "the" attends strongly to "dog" with a weight of 0.707 while largely bypassing "brown" (0.033). In "from the table", "the" attends to "table" with a weight of 0.857. When the head noun is replaced by a mask token, as in "a small [MASK]" or "the lazy [MASK]", the determiner still routes the majority of its attention to the masked position (0.818 and 0.640, respectively).

This attention head appears to capture syntactic noun-phrase dependency structures. In natural language, determiners specify reference, definiteness, and countability for the head noun of a phrase rather than for the intervening adjectives. Because phrases can contain varying numbers of descriptive adjectives (or none at all), an attention head that directly links determiners to their governing head nouns enables the model to resolve the core arguments of noun phrases without being distracted by modifiers. While determiners also allocate a small fraction of their attention to sentence boundary tokens like `[SEP]` in certain contexts, the primary concentration remains on the corresponding head noun.

Example Sentences:
- We turned down a narrow lane and passed through a small [MASK].
- The brown dog jumped over the lazy [MASK].
- Then I picked up a [MASK] from the table.
