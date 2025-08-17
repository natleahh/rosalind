
> The Second Nucleic Acid
> -----------------------
> 
> [![](/media/problems/rna/RNA-DNA.thumb.png)](/media/problems/rna/RNA-DNA.png)**Figure 1**. Structural differences between RNA and DNAIn [“Counting DNA Nucleotides”](/problems/dna/ "“Counting DNA Nucleotides”"), we described the [primary structure](/glossary/nucleic-acid-primary-structure/ "
> The order of bases on a strand of nucleic acid.")of a [nucleic acid](/glossary/nucleic-acid/ "
> A polymer of nucleotides, constituting either RNA or DNA.") as a [polymer](/glossary/polymer/ "
> A molecule formed by a repeating chain of subunits.") of [nucleotide](/glossary/nucleotide/ "
> The monomer making up a nucleic acid.") units,
> and we mentioned that the omnipresent nucleic acid [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms.") is composed of a varied sequence of four [bases](/glossary/nucleobase/ "
> The differentiating component of nucleotides.").
> 
> Yet a second nucleic acid exists alongside DNA in the [chromatin](/glossary/chromatin/ "
> The dense collection of nucleic acids and proteins found in the nucleus."); this molecule,
> which possesses a different [sugar](/glossary/sugar/ "
> One of the three components of a nucleotide.") called [ribose](/glossary/ribose/ "New term: 
> The sugar component of RNA."), came to be known as [ribose
> nucleic acid](/glossary/rna/ "New term: 
> A nucleic acid transcribed from DNA that serves as the template for protein creation."), or RNA. RNA differs further from DNA in that it contains a base called[uracil](/glossary/uracil/ "New term: 
> One of the four bases of RNA (but not DNA).") in place of [thymine](/glossary/thymine/ "
> One of the four bases of DNA; complementary to adenine."); structural differences between DNA and RNA
> are shown in [Figure 1](/media/problems/rna/RNA-DNA.png "Click to view").
> Biologists initially believed that RNA was only contained in plant [cells](/glossary/cell/ "
> The \"building block of life,\" making up all living things on Earth."), whereas DNA
> was restricted to animal cells. However, this hypothesis dissipated as improved chemical
> methods discovered both nucleic acids in the cells of all life forms on Earth.
> 
> The [primary structure](/glossary/nucleic-acid-primary-structure/ "
> The order of bases on a strand of nucleic acid.") of DNA and RNA is
> so similar because the former serves as a blueprint for the creation of
> a special kind of RNA molecule called [messenger RNA](/glossary/messenger-rna/ "New term: 
> An RNA molecule that serves as the blueprint for translation into protein."), or mRNA.
> mRNA is created during [RNA transcription](/glossary/rna-transcription/ "New term: 
> The process by which DNA is converted into RNA."),
> during which a [strand](/glossary/strand/ "
> A nucleic acid polymer.") of DNA is used as a template for constructing a
> strand of RNA by copying nucleotides one at a time, where
> uracil is used in place of thymine.
> 
> In eukaryotes, DNA remains in the [nucleus](/glossary/nucleus/ "
> The central \"brain\" of a eukaryotic cell, which contains the cell's DNA."), while RNA can enter
> the far reaches of the cell to carry out DNA's instructions.
> In future problems, we will examine the process and ramifications of RNA transcription in more detail.

Problem
-------

An [RNA string](/glossary/rna-string/ "New term: 
A string constructed from the alphabet {A, C, G, U}.") is a [string](/glossary/string/ "
An ordered collection of symbols formed into a word.") formed from the [alphabet](/glossary/alphabet/ "
A collection of symbols from which strings are constructed.") containing 'A', 'C', 'G', and 'U'.

Given a [DNA string](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $t$ corresponding to a coding strand, its transcribed [RNA string](/glossary/rna-string/ "
A string constructed from the alphabet {A, C, G, U}.") $u$is formed by replacing all occurrences of 'T' in $t$ with 'U' in $u$.

Given: A [DNA string](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $t$ having [length](/glossary/string-length/ "
The number of symbols in a string.") at most 1000 [nt](/glossary/nucleotide/ "
The monomer making up a nucleic acid.").

Return: The transcribed RNA string of $t$.

Sample Dataset
--------------

```
GATGGAACTTGACTACGTAAATT

```

Sample Output
-------------

```
GAUGGAACUUGACUACGUAAAUU

```
