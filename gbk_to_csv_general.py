import os
from Bio import SeqIO

infile = 'your_file.gbk'
output_file = 'output.csv'

with open(output_file, 'w') as oh:
    # Write the header to the CSV
    oh.write("record_id,feature_type,locus_tag,category,function,product\n")
    
    # Parse the GenBank file
    for record in SeqIO.parse(infile, 'genbank'):
        for feature in record.features:
            # Initialize default values
            locus_tag = 'Unknown'
            category = 'Unknown'
            function = 'Unknown'
            product = 'Unknown'
            
            # Extract the feature type
            feature_type = feature.type
            
            # Check for 'locus_tag', 'category', 'function', and 'product' qualifiers
            if 'locus_tag' in feature.qualifiers:
                locus_tag = feature.qualifiers['locus_tag'][0]
            if 'category' in feature.qualifiers:
                category = feature.qualifiers['category'][0]
            if 'function' in feature.qualifiers:
                function = feature.qualifiers['function'][0]
            if 'product' in feature.qualifiers:
                product = feature.qualifiers['product'][0]
            
            # Create a CSV line with the updated order
            line = f'{record.id},{feature_type},{locus_tag},{category},{function},{product}\n'
            oh.write(line)
