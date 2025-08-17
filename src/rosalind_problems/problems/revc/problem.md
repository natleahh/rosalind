
> The Secondary and Tertiary Structures of DNA
> --------------------------------------------
> 
> [![](https://rosalind.info/media/problems/revc/DNA_chemical_structure.thumb.png)](https://rosalind.info/media/problems/revc/DNA_chemical_structure.png)**Figure 1**. Base pairing across the two strands of DNA.[![](https://rosalind.info/media/problems/revc/DNA.thumb.png)](https://rosalind.info/media/problems/revc/DNA.png)**Figure 2**. The double helix of DNA on the molecular scale.In [“Counting DNA Nucleotides”](/problems/dna/ "“Counting DNA Nucleotides”"), we introduced [nucleic acids](/glossary/nucleic-acid/ "
> A polymer of nucleotides, constituting either RNA or DNA."), and we saw that the [primary structure](/glossary/nucleic-acid-primary-structure/ "
> The order of bases on a strand of nucleic acid.")of a nucleic acid is determined by the ordering of its [nucleobases](/glossary/nucleobase/ "
> The differentiating component of nucleotides.") along the [sugar\-phosphate backbone](/glossary/sugar-phosphate-backbone/ "
> The alternating chain of sugar and phosphate molecules in a nucleic acid.")that constitutes the bonds of the nucleic acid [polymer](/glossary/polymer/ "
> A molecule formed by a repeating chain of subunits.").
> Yet primary structure tells us nothing about the larger, 3\-dimensional shape of the molecule, which
> is vital for a complete understanding of nucleic acids.
> 
> The search for a complete chemical structure of nucleic acids was central to molecular biology research in the mid\-20th
> Century, culminating in 1953 with a publication in *Nature* of fewer than 800 words by James Watson and
> Francis Crick. Consolidating a high resolution X\-ray image created by Rosalind
> Franklin and Raymond Gosling with a number of established chemical results,
> Watson and Crick proposed the following structure for [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms."):
> 
> 1. The DNA molecule is made up of two [strands](/glossary/strand/ "
> A nucleic acid polymer."), running in opposite directions.
> 2. Each base bonds to a base in the opposite strand.[Adenine](/glossary/adenine/ "
> One of the nucleobases of both RNA and DNA; complementary to thymine in DNA.") always bonds with [thymine](/glossary/thymine/ "
> One of the four bases of DNA; complementary to adenine."), and [cytosine](/glossary/cytosine/ "
> One of the nucleobases of both RNA and DNA; complementary to guanine.") always bonds with [guanine](/glossary/guanine/ "
> One of the nucleobases of both RNA and DNA; complementary to cytosine in DNA.");
> the [complement](/glossary/complementary-base/ "New term: 
> The base to which a given base bonds in DNA.") of a base is the base to which it always bonds;
> see [Figure 1](/media/problems/revc/DNA_chemical_structure.png "Click to view").
> 3. The two strands are twisted together into a long spiral staircase structure called
> a [double helix](/glossary/double-helix/ "New term: 
> A shape composed of two twisted chains, which serves as a model for the structure of DNA."); see [Figure 2](/media/problems/revc/DNA.png "Click to view").
> 
> Because they dictate how bases from different strands interact with each other,
> (1\) and (2\) above compose the [secondary structure](/glossary/nucleic-acid-secondary-structure/ "New term: 
> The base pairing interactions of nucleic acid bases.") of DNA.
> (3\) describes the 3\-dimensional shape of the DNA molecule,
> or its [tertiary structure](/glossary/nucleic-acid-tertiary-structure/ "New term: 
> The 3-dimensional shape of a nucleic acid, which in the case of DNA is the double helix.").
> 
> In light of Watson and Crick's model, the bonding of two complementary bases is called a [base pair](/glossary/base-pair/ "New term: 
> The combination of two bonded complementary bases.") (bp).
> Therefore, the length of a DNA molecule will commonly be given in bp instead of [nt](/glossary/nucleotide/ "
> The monomer making up a nucleic acid.").
> By complementarity, once we know the
> order of bases on one strand, we can immediately deduce the sequence of bases in the complementary strand.
> These bases will run in the opposite order to match the fact that the two strands of
> DNA run in opposite directions.

Problem
-------

In [DNA strings](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}."), [symbols](/glossary/symbol/ "
The constituent individual elements of a string, which may constitute numbers and letters.") 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The [reverse complement](/glossary/reverse-complement/ "New term: 
The DNA string formed by reversing and complementing each symbol.") of a [DNA string](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $s$ is the string $s^{\\textrm{c}}$formed by reversing the symbols of $s$, then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string $s$ of length at most 1000 [bp](/glossary/base-pair/ "
The combination of two bonded complementary bases.").

Return: The reverse complement $s^{\\textrm{c}}$ of $s$.

Sample Dataset
--------------

```
AAAACCCGGT

```

Sample Output
-------------

```
ACCGGGTTTT

```
