from pyfaidx import Fasta

def extract_seq_genome(genome, chrom, start, end, strand = '+'):
    '''
    ath: tair10
    cel: cel235
    hsa: hg38
    mmu: mm10

    Usage:
        - If strand == '+', return sequence
        - If strand == '-', return sequence revese complementary
        - With hg38.get_seq(chrom, start, end, rc= strand == '-').seq get correct position of miRNA,
        for mapping result, you should modify by yourself.
    '''
    
    PATH = 'C:/03. Work/DUC_research/homo sapiens/hg38/'
    if genome == 'cel':
        genome = 'cel235'
    elif genome == 'hsa':
        genome = 'hg38'
    elif genome == 'mmu':
        genome = 'mm10'
    elif genome == 'ath':
        genome = 'tair10'
    elif genome == 'mml':
        genome = 'Macaca_mulatta.Mmul_10.dna.toplevel'
    elif genome == 'dre':
        genome = 'Danio_rerio.GRCz11.dna.primary_assembly'
    elif genome == 'dme':
        genome = 'Drosophila_melanogaster.BDGP6.32.dna.toplevel'


    gene = Fasta(f"{PATH}/{genome}.fa") 
    
    #hg38.get_seq('chr1', 100009588 + 1, 100009608, rc=False).seq
    return(gene.get_seq(chrom, start+1, end, rc= strand == '-').seq)