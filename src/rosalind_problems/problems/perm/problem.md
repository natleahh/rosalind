
> Rearrangements Power Large\-Scale Genomic Changes
> -------------------------------------------------
> 
> [![](https://rosalind.info/media/problems/perm/synteny.thumb.jpg)](https://rosalind.info/media/problems/perm/synteny.jpg)**Figure 1**. Similar regions in mouse and human chromosomes. Image credit: U.S. Department of Energy Human Genome Program[Point mutations](/glossary/point-mutation/ "
> A mutation that only affects a single nucleotide of nucleic acid.") can create changes in populations of organisms from the same species,
> but they lack the power to create and differentiate entire species.
> This more arduous work is left to larger mutations called [genome rearrangements](/glossary/genome-rearrangement/ "New term: 
> A large-scale mutation that affects the makeup of entire intervals of nucleic acid."), which move
> around huge blocks of [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms."). Rearrangements cause major [genomic](/glossary/genome/ "
> The collection of all of an organism's DNA taken from all its chromosomes.") change, and
> most rearrangements are fatal or seriously damaging to the mutated[cell](/glossary/cell/ "
> The \"building block of life,\" making up all living things on Earth.") and its descendants (many cancers derive from rearrangements). For this reason,
> rearrangements that come to influence the genome of an entire species are very rare.
> 
> Because rearrangements that affect species evolution occur infrequently, two closely related species will
> have very similar genomes. Thus, to simplify comparison of two such genomes, researchers
> first identify similar intervals of DNA from the species, called [synteny blocks](/glossary/synteny-block/ "New term: 
> A region of DNA that is condensed into a single unit for genome comparison."); over time, rearrangements
> have created these synteny blocks and heaved them around
> across the two genomes (often separating blocks onto different [chromosomes](/glossary/chromosome/ "
> A tightly coiled structure of DNA formed in advance of mitosis to facilitate DNA's duplication."), see [Figure 1](/media/problems/perm/synteny.jpg "Click to view").).
> 
> A pair of synteny blocks from two different species are not strictly identical
> (they are separated by the action of point mutations or very small rearrangements),
> but for the sake of studying large\-scale rearrangements, we consider them to be equivalent.
> As a result, we can label each synteny block with a positive integer; when comparing
> two species' genomes/chromosomes,
> we then only need to specify the order of its numbered synteny blocks.

Problem
-------

A [permutation](/glossary/permutation/ "New term: 
A permutation of length n is an ordering of the first n positive integers.") of length $n$ is an ordering of the positive integers $\\{1, 2, \\ldots, n\\}$.
For example, $\\pi \= (5, 3, 2, 1, 4\)$ is a permutation of length $5$.

Given: A positive integer $n \\leq 7$.

Return: The total number of permutations of length $n$, followed by a list of all such
permutations (in any order).

Sample Dataset
--------------

```
3

```

Sample Output
-------------

```
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

```
