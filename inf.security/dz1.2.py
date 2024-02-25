import gzip

def decompress_file(input_filename, output_filename):
    with gzip.open(input_filename, 'rb') as f_in, open(output_filename, 'wb') as f_out:
        f_out.writelines(f_in)

input_filename = 'compressed_output.txt.gz'
output_filename = 'decompressed_output.txt'

decompress_file(input_filename, output_filename)

print(f'{input_filename} успешно распакован в {output_filename}')