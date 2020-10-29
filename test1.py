import cyvcf2
import numpy as np
vcf = cyvcf2.VCF("sample.vcf")
# sample_counts = np.zeros(len(vcf.samples), dtype=float)
# for variant in vcf("chr1:0-100"):
#     if variant.is_indel: continue
#     if variant.QUAL < 10: continue
#     depths = variant.format("AD")
#     sample_counts[(depths[:, 1] > 10) & (variant.gt_types == vcf.HET)]+=1
#     print(vcf.samples, sample_counts)

count = 0
for variant in vcf:
    print("This is variant")
    print(variant)
    print("-----")
    print("This is variant.CHROM")
    print(variant.CHROM)
    print("-----")
    print("This is variant.POS")
    print(variant.POS)
    print("-----")
    print("This is variant.ID")
    print(variant.ID)
    print("-----")
    print("This is variant.REF")
    print(variant.REF)
    print("-----")
    print("This is variant.ALT")
    print(variant.ALT)
    print("-----")
    print("This is variant.QUAL")
    print(variant.QUAL)
    print("-----")
    print("This is variant.FILTER")
    print(variant.FILTER)
    print("-----")
    print("This is variant.INFO -> CSQT")
    print(variant.INFO.get("CSQT").split('|'))
    print("-----")
    print("This is variant.INFO -> CSQR")
    print(variant.INFO.get("CSQR").split('|'))
    print("-----")
    print("This is variant.FORMAT")
    print(variant.FORMAT)
    print(variant.format("GT"))
    print(variant.format("GQX"))
    print(variant.format("DP"))
    print(variant.format("DPF"))
    print(variant.format("AD"))
    print(type(variant.format("PL")))
    print(variant.format("PL"))
    break
    

# n = vcf.raw_header.rfind("#")
# print(n)
# print(vcf.raw_header[n+1:].split())
# print(vcf.seqnames)