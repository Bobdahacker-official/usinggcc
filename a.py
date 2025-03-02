import argparse
import subprocess
import os

def compile_c_file(source_file, output_file):
    """Compile a C source file using GCC."""
    compile_command = f"gcc {source_file} -o {output_file}"
    try:
        subprocess.check_call(compile_command, shell=True)
        print(f"Compilation successful! Output saved as {output_file}")
    except subprocess.CalledProcessError:
        print(f"Error: Compilation of {source_file} failed!")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="A simple GCC compiler CLI tool.")
    
    # Add arguments to the parser
    parser.add_argument("source", help="The C source file to compile.")
    parser.add_argument("-o", "--output", help="The output file name (without extension).", required=True)
    parser.add_argument("-t", "--type", help="Specify output file type.", choices=["exe", "bin", "out", "elf", "obj", "other"], default="exe")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    source_file = args.source
    output_file = args.output
    output_type = args.type
    
    # Check if the source file exists
    if not os.path.isfile(source_file):
        print(f"Error: The source file {source_file} does not exist.")
        return
    
    # Add extension to output file based on type
    if output_type == "exe":
        if not output_file.endswith(".exe"):
            output_file += ".exe"
    elif output_type == "bin":
        if not output_file.endswith(".bin"):
            output_file += ".bin"
    elif output_type == "out":
        if not output_file.endswith(".out"):
            output_file += ".out"
    elif output_type == "elf":
        if not output_file.endswith(".elf"):
            output_file += ".elf"
    elif output_type == "obj":
        if not output_file.endswith(".obj"):
            output_file += ".obj"
    else:
        if not output_file.endswith(".out"):
            output_file += ".out"
    
    # Compile the source file
    compile_c_file(source_file, output_file)

if __name__ == "__main__":
    main()
