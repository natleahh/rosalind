
> A Rapid Introduction to Molecular Biology
> -----------------------------------------
> 
> [![](https://rosalind.info/media/problems/dna/cell.thumb.jpg)](https://rosalind.info/media/problems/dna/cell.jpg)**Figure 1**. A 1900 drawing by Edmund Wilson of onion cells at different stages of mitosis. The sample has been dyed, causing chromatin in the cells (which soaks up the dye) to appear in greater contrast to the rest of the cell.[![](https://rosalind.info/media/problems/dna/DNA_chemical_structure.thumb.png)](https://rosalind.info/media/problems/dna/DNA_chemical_structure.png)**Figure 2**. A sketch of DNA's primary structure.Making up all living material, the [cell](/glossary/cell/ "New term: 
> The \"building block of life,\" making up all living things on Earth.") is considered to be the building block of life.
> The [nucleus](/glossary/nucleus/ "New term: 
> The central \"brain\" of a eukaryotic cell, which contains the cell's DNA."), a component of most [eukaryotic](/glossary/eukaryote/ "New term: 
> Eukaryotes form the most complex domain of life, which includes all multicellular organisms.") cells, was identified as the hub of
> cellular activity 150 years ago. Viewed under a light microscope, the nucleus appears only
> as a darker region of the cell, but as we increase magnification,
> we find that the nucleus is densely filled with a stew of macromolecules called [chromatin](/glossary/chromatin/ "New term: 
> The dense collection of nucleic acids and proteins found in the nucleus.").
> During [mitosis](/glossary/mitosis/ "New term: 
> The process of eukaryotic cell division.") (eukaryotic cell division), most of the chromatin condenses into long, thin strings
> called [chromosomes](/glossary/chromosome/ "New term: 
> A tightly coiled structure of DNA formed in advance of mitosis to facilitate DNA's duplication."). See [Figure 1](/media/problems/dna/cell.jpg "Click to view")for a figure of cells in different stages of mitosis.
> 
> One class of the macromolecules contained in chromatin are called [nucleic acids](/glossary/nucleic-acid/ "New term: 
> A polymer of nucleotides, constituting either RNA or DNA.").
> Early 20th century research into the
> chemical identity of nucleic acids culminated with the conclusion that
> nucleic acids are [polymers](/glossary/polymer/ "New term: 
> A molecule formed by a repeating chain of subunits."), or repeating chains of smaller, similarly structured molecules known as [monomers](/glossary/monomer/ "New term: 
> The structural unit making up a macromolecule (specifically, a polymer).").
> Because of their tendency to be long and thin, nucleic acid polymers are commonly called [strands](/glossary/strand/ "New term: 
> A nucleic acid polymer.").
> 
> The nucleic acid monomer is called a [nucleotide](/glossary/nucleotide/ "New term: 
> The monomer making up a nucleic acid.") and is used as a unit of strand length (abbreviated to nt).
> Each nucleotide is formed of three parts:
> a [sugar](/glossary/sugar/ "New term: 
> One of the three components of a nucleotide.") molecule, a negatively charged [ion](/glossary/ion/ "New term: 
> An electrically charged atom or molecule.") called a [phosphate](/glossary/phosphate/ "New term: 
> An ion that forms one of the three components of a nucleotide."),
> and a compound called a [nucleobase](/glossary/nucleobase/ "New term: 
> The differentiating component of nucleotides.") ("base" for short).
> Polymerization is achieved as the sugar of one nucleotide bonds to the phosphate of the
> next nucleotide in the chain, which forms a [sugar\-phosphate backbone](/glossary/sugar-phosphate-backbone/ "New term: 
> The alternating chain of sugar and phosphate molecules in a nucleic acid.") for the nucleic acid strand.
> A key point is that the nucleotides of a specific type of nucleic acid
> always contain the same sugar and phosphate molecules,
> and they differ only in their choice of base.
> Thus, one strand of a nucleic acid can be differentiated from 
> another based solely on the *order* of its bases; this ordering of bases defines a nucleic
> acid's [primary structure](/glossary/nucleic-acid-primary-structure/ "New term: 
> The order of bases on a strand of nucleic acid.").
> 
> For example, [Figure 2](/media/problems/dna/DNA_chemical_structure.png "Click to view")shows a strand of [deoxyribose nucleic acid](/glossary/dna/ "New term: 
> The molecule encoding heredity and underlying the cellular processes of all life forms.") (DNA),
> in which the sugar is called [deoxyribose](/glossary/deoxyribose/ "New term: 
> The monosaccharide appearing in each nucleotide of DNA."),
> and the only four choices for nucleobases are molecules called[adenine](/glossary/adenine/ "New term: 
> One of the nucleobases of both RNA and DNA; complementary to thymine in DNA.") (A), [cytosine](/glossary/cytosine/ "New term: 
> One of the nucleobases of both RNA and DNA; complementary to guanine.") (C), [guanine](/glossary/guanine/ "New term: 
> One of the nucleobases of both RNA and DNA; complementary to cytosine in DNA.") (G), and [thymine](/glossary/thymine/ "New term: 
> One of the four bases of DNA; complementary to adenine.") (T).
> 
> For reasons we will soon see, DNA is found in all living organisms on Earth, including bacteria;
> it is even found in many viruses (which are often considered to be nonliving).
> Because of its importance, we reserve the term [genome](/glossary/genome/ "New term: 
> The collection of all of an organism's DNA taken from all its chromosomes.")to refer to the sum total of the DNA contained in an organism's chromosomes.

Problem
-------

A [string](/glossary/string/ "New term: 
An ordered collection of symbols formed into a word.") is simply an ordered collection of symbols selected from
some [alphabet](/glossary/alphabet/ "New term: 
A collection of symbols from which strings are constructed.") and formed into a word; the [length](/glossary/string-length/ "New term: 
The number of symbols in a string.") of a string is
the number of symbols that it contains.

An example of a length 21 [DNA string](/glossary/dna-string/ "New term: 
A string constructed from the alphabet {A, C, G, T}.") (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string $s$ of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the
symbols 'A', 'C', 'G', and 'T' occur in $s$.

Sample Dataset
--------------

```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

```

Sample Output
-------------

```
20 12 17 21

```
