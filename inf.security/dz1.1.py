import gzip

def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f_in, gzip.open(output_filename, 'wb') as f_out:
        f_out.writelines(f_in)

input_filename = 'input.txt'
output_filename = 'compressed_output.txt.gz'

compress_file(input_filename, output_filename)

print(f'{input_filename} успешно сжат и сохранен в {output_filename}')