
> Evolution as a Sequence of Mistakes
> -----------------------------------
> 
> [![](https://rosalind.info/media/problems/hamm/point_mutation.thumb.png)](https://rosalind.info/media/problems/hamm/point_mutation.png)**Figure 1**. A point mutation in DNA changing a C\-G pair to an A\-T pair.A [mutation](/glossary/mutation/ "New term: 
> A mistake that occurs during the creation or copying of a nucleic acid.") is simply a mistake that occurs during the creation or copying of a[nucleic acid](/glossary/nucleic-acid/ "
> A polymer of nucleotides, constituting either RNA or DNA."), in particular [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms."). Because nucleic acids are vital to [cellular](/glossary/cell/ "
> The \"building block of life,\" making up all living things on Earth.") functions, mutations tend
> to cause a ripple effect throughout the cell.
> Although mutations are technically mistakes, a very rare mutation may equip the cell with a beneficial attribute.
> In fact, the macro effects of evolution are attributable by the accumulated result of beneficial
> microscopic mutations over many generations.
> 
> The simplest and most common type of nucleic acid mutation is a [point mutation](/glossary/point-mutation/ "New term: 
> A mutation that only affects a single nucleotide of nucleic acid."), which
> replaces one [base](/glossary/nucleobase/ "
> The differentiating component of nucleotides.") with another at a single [nucleotide](/glossary/nucleotide/ "
> The monomer making up a nucleic acid."). In the case of DNA,
> a point mutation must change the [complementary base](/glossary/complementary-base/ "
> The base to which a given base bonds in DNA.") accordingly;
> see [Figure 1](/media/problems/hamm/point_mutation.png "Click to view").
> 
> Two DNA strands taken from different organism or species genomes are [homologous](/glossary/homologous/ "New term: 
> Descending from the same ancestor.") if they share a recent
> ancestor; thus, counting the number of bases at which homologous strands differ provides
> us with the minimum number of point mutations that could have occurred
> on the evolutionary path between the two strands.
> 
> We are interested in minimizing the number of (point) mutations separating two species because of the
> biological principle of [parsimony](/glossary/parsimony/ "New term: 
> The biological principle that nature tends to take the shortest path in evolution."), which demands that evolutionary histories should be as simply explained as possible.

Problem
-------

[![](https://rosalind.info/media/problems/hamm/Hamming_distance.png)](https://rosalind.info/media/problems/hamm/Hamming_distance.png)**Figure 2**. The Hamming distance between these two strings is 7\. Mismatched symbols are colored red.Given two [strings](/glossary/string/ "
An ordered collection of symbols formed into a word.") $s$ and $t$ of equal length, the [Hamming distance](/glossary/hamming-distance/ "New term: 
The minimum number of symbol substitutions required to change one string into another of equal length.")between $s$ and $t$, denoted $d\_{\\mathrm{H}}(s, t)$, is the number of corresponding symbols
that differ in $s$ and $t$. See [Figure 2](/media/problems/hamm/Hamming_distance.png "Click to view").

Given: Two [DNA strings](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $s$ and $t$ of equal length (not exceeding 1 [kbp](/glossary/kbp/ "
1 kbp = 1000 base pairs")).

Return: The Hamming distance $d\_{\\mathrm{H}}(s, t)$.

Sample Dataset
--------------

```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

```

Sample Output
-------------

```
7

```
