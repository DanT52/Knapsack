import subprocess
import os

def run_test(input_file, expected_output_file):
    with open(input_file, 'r') as infile:
        input_data = infile.read()
    
    with open(expected_output_file, 'r') as outfile:
        expected_output = outfile.read().strip()
    
    process = subprocess.Popen(['./test'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # test python version
    # process = subprocess.Popen(['python3','main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate(input=input_data.encode())
    
    output = stdout.decode().strip()
    
    if output == expected_output:
        print(f"Test {input_file} passed.")
    else:
        print(f"Test {input_file} failed.")
        print(f"Expected:\n{expected_output}")
        print(f"Got:\n{output}")

if __name__ == "__main__":
    input_dir = 'inputs'
    output_dir = 'outputs'
    
    for i in range(1, 6):
        input_file = os.path.join(input_dir, f'{i}.txt')
        expected_output_file = os.path.join(output_dir, f'{i}out.txt')
        run_test(input_file, expected_output_file)