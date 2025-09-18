
> Same Data, Different Formats
> ----------------------------
> 
> [![](https://rosalind.info/media/problems/frmt/gbk.thumb.png)](https://rosalind.info/media/problems/frmt/gbk.png)**Figure 1**. An example of a GenBank record header.A number of different data presentation formats have been used to represent [genetic strings](/glossary/genetic-string/ "
> A DNA, RNA, or amino acid string.").
> The history of file formats presents its own kind of evolution: some formats have died out,
> being replaced by more successful ones. Three file formats are currently the most popular:
> 
> * [FASTA](/glossary/fasta-format/ "
> A text format used for naming genetic strings in databases.") (.fas, .fasta): used by practically all modern software and databases, including[ClustalX](http://www.clustal.org/clustal2/), [Paup](http://paup.csit.fsu.edu/),[HyPhy](http://hyphy.org/), [Rdp](http://rdp.cme.msu.edu/), and [Dambe](http://dambe.bio.uottawa.ca/dambe.asp).
> * [NEXUS](/glossary/nexus/ "New term: 
> File format widely used in bioinformatics.") (.nex, .nexus, .nxs): used by Paup, [MrBayes](http://mrbayes.sourceforge.net/),[FigTree](http://tree.bio.ed.ac.uk/software/figtree/), and [SplitsTree](http://www.splitstree.org/).
> * [PHYLIP](/glossary/phylip-format/ "New term: 
> A format used as an input file for programs belonging to the PHYLIP package."), or "**Phyl**ogeny **I**nference **P**ackage" (.phy): used by [Phylip](http://evolution.genetics.washington.edu/phylip.html),[Tree\-Puzzle](http://www.tree-puzzle.de/), [PhyML](http://www.atgc-montpellier.fr/phyml/),
> and a number of databases.
> 
> A simple reference on file formats can be found [here](http://www.molecularevolution.org/resources/fileformats).
> 
> In this problem, we will familarize ourselves with FASTA. We will save the other two formats for later problems.
> 
> In FASTA format, a [string](/glossary/string/ "
> An ordered collection of symbols formed into a word.") is introduced by a line that begins with '\>',
> followed by some information labeling the string. Subsequent lines contain the string itself; the
> next line beginning with '\>' indicates that the current string is complete and begins the label of the next string
> in the file.
> 
> [GenBank](/glossary/genbank/ "
> The world's largest genetic database, hosted by NCBI") hosts its own file format for storing [genome](/glossary/genome/ "
> The collection of all of an organism's DNA taken from all its chromosomes.") data, containing a large
> amount of information about each interval of [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms."). The GenBank file describes
> the interval's source, taxonomic position, authors, and features (see [Figure 1](/media/problems/frmt/gbk.png "Click to view")).
> 
> A sample GenBank entry can be found [here](http://www.ncbi.nlm.nih.gov/nuccore/JH977701.1).
> You may export an entry to a variety of file formats by selecting the appropriate file
> format under the `Send To:` dropdown menu at the top of the page.

Problem
-------

GenBank can be accessed [here](http://www.ncbi.nlm.nih.gov/genbank/). 
A detailed description of the GenBank format can be found [here](http://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html).
A tool, from the [SMS 2](/glossary/sms-2/ "
A software suite for analyzing short genetic strings.") package, for converting GenBank to FASTA can be found [here](http://www.bioinformatics.org/sms2/genbank_fasta.html). 

Given: A collection of $n$ ($n \\leq 10$) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in [FASTA](/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.") format.

Sample Dataset
--------------

```
FJ817486 JX069768 JX469983

```

Sample Output
-------------

```
>JX469983.1 Zea mays subsp. mays clone UT3343 G2-like transcription factor mRNA, partial cds
ATGATGTATCATGCGAAGAATTTTTCTGTGCCCTTTGCTCCGCAGAGGGCACAGGATAATGAGCATGCAA
GTAATATTGGAGGTATTGGTGGACCCAACATAAGCAACCCTGCTAATCCTGTAGGAAGTGGGAAACAACG
GCTACGGTGGACATCGGATCTTCATAATCGCTTTGTGGATGCCATCGCCCAGCTTGGTGGACCAGACAGA
GCTACACCTAAAGGGGTTCTCACTGTGATGGGTGTACCAGGGATCACAATTTATCATGTGAAGAGCCATC
TGCAGAAGTATCGCCTTGCAAAGTATATACCCGACTCTCCTGCTGAAGGTTCCAAGGACGAAAAGAAAGA
TTCGAGTGATTCCCTCTCGAACACGGATTCGGCACCAGGATTGCAAATCAATGAGGCACTAAAGATGCAA
ATGGAGGTTCAGAAGCGACTACATGAGCAACTCGAGGTTCAAAGACAACTGCAACTAAGAATTGAAGCAC
AAGGAAGATACTTGCAGATGATCATTGAGGAGCAACAAAAGCTTGGTGGATCAATTAAGGCTTCTGAGGA
TCAGAAGCTTTCTGATTCACCTCCAAGCTTAGATGACTACCCAGAGAGCATGCAACCTTCTCCCAAGAAA
CCAAGGATAGACGCATTATCACCAGATTCAGAGCGCGATACAACACAACCTGAATTCGAATCCCATTTGA
TCGGTCCGTGGGATCACGGCATTGCATTCCCAGTGGAGGAGTTCAAAGCAGGCCCTGCTATGAGCAAGTC
A

```

> Programming Shortcut
> --------------------
> 
> Here we can again use the `Bio.Entrez` module introduced in [“GenBank Introduction”](/problems/gbk/ "“GenBank Introduction”"). To search for particular access IDs,
> you can use the function `Bio.Entrez.efetch(db, rettype)`, which takes two parameters:
> the `db` parameter takes the database to search,
> and the `rettype` parameter takes the data format to be returned. For example, we use
> "nucleotide" (or "nuccore") as the `db` parameter for Genbank and "fasta" as the `rettype` parameter for FASTA format.
> 
> The following code illustrates `efetch()` in action. It obtains plain text records in FASTA format
> from NCBI's \[Nucleotide] database.
> 
> 
> ```
> >>>from Bio import Entrez
> >>>Entrez.email = "your_name@your_mail_server.com"
> >>>handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
> >>>records = handle.read()
> >>>print records
> 
> ```
> To work with FASTA format, we can use the `Bio.SeqIO` module, which provides an interface to input and output methods for
> different file formats. One of its main functions is`Bio.SeqIO.parse()`, which takes a handle and format name as parameters and returns entries as SeqRecords.
> 
> 
> ```
> >>>from Bio import Entrez
> >>>from Bio import SeqIO
> >>>Entrez.email = "your_name@your_mail_server.com"
> >>>handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
> >>>records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
> >>>print records[0].id  #first record id
> gi|227437129|gb|FJ817486.1|
> >>>print len(records[-1].seq)  #length of the last record
> 771
> 
> ```

