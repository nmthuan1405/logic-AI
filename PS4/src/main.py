import os
import logic
import utils

INPUT_FOLDER = "input/"
OUTPUT_FOLDER = "output/"

for filename in os.listdir(INPUT_FOLDER):
    print('--------------------------------------------------------------')
    print (filename)
    
    alpha, KB = utils.read_input(os.path.join(INPUT_FOLDER, filename))
    result = logic.pl_resolution(KB, alpha)
    utils.write_output(os.path.join(OUTPUT_FOLDER, utils.output_filename(filename)), result)