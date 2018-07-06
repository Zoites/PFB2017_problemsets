#!/usr/bin/env python3
#from Bio.Seq import Seq

DNA_string_test= 'AATTGGCCA'
#DNA_string_test_length = len(DNA_string_test)
#AT=DNA_string_test.count('A') + DNA_string_test.count('T')
#AT_Content= AT / DNA_string_test_length
#print ('Number of As and Ts is' ,AT,)
#print ('AT Content of sequence is' ,AT_Content, '%')

#1 and #2: Find AT and GC content of sequence
DNA_string= 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

DNA_string_length = len(DNA_string)

AT=DNA_string.count('A') + DNA_string.count('T')
AT_Content= AT / DNA_string_length

GC=DNA_string.count('G') + DNA_string.count('C')
GC_Content= GC / DNA_string_length


#print ('Number of nucleotides is' ,DNA_string_length)
#print ('Number of As and Ts is' ,AT,)
#print ('AT Content of sequence is' ,AT_Content,'%')
#print ('GC content of sequence is' ,GC_Content,'%')

#3 Reverse complement of sequence
Test_reverse_complement = DNA_string_test.translate(str.maketrans("ATCG", "TAGC"))
#print (Test_reverse_complement [::-1])

Reverse_complement = DNA_string.translate(str.maketrans("ATCG", "TAGC"))
#print (Reverse_complement [::-1])

#5 find the start position of an EcoRI in the above sequence
#EcoRI_start_site_python = DNA_string_test.find('AATT')
#EcoRI_start_site = EcoRI_start_site_python + 1
#print (EcoRI_start_site)

EcoRI_start_site_python = DNA_string.find('GAATT')
EcoRI_start_site = EcoRI_start_site_python + 1
print (EcoRI_start_site)