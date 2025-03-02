import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Function to create a C file from user input
def create_c_file(file_name, code):
    try:
        with open(file_name, 'w') as f:
            f.write(code)
        messagebox.showinfo("Success", f"C source file '{file_name}' created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create C file: {e}")

# Function to handle parallel compilation
def compile_code_parallel(compile_command, num_jobs):
    try:
        subprocess.check_call(f"{compile_command} -j {num_jobs}", shell=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Compilation failed: {e}")

# Function to compile code
def compile_code():
    source_code = source_code_text.get("1.0", tk.END).strip()
    output_file = output_file_var.get()
    output_type = output_type_var.get()

    if not source_code:
        messagebox.showerror("Error", "Please enter C code in the text area.")
        return

    if not output_file:
        output_file = "output"  # Default output file name

    # Adjust output format based on user selection
    if output_type == "exe":
        output_file += ".exe"
    elif output_type == "bin":
        output_file += ".bin"
    elif output_type == "tar":
        output_file += ".tar"
    elif output_type == "tar.gz":
        output_file += ".tar.gz"
    elif output_type == "tar.bz2":
        output_file += ".tar.bz2"
    elif output_type == "img":
        output_file += ".img"
    elif output_type == "ko":
        output_file += ".ko"
    elif output_type == "so":
        output_file += ".so"
    elif output_type == "json":
        output_file += ".json"
    else:
        output_file += f".{output_type}"

    # Step 1: Create the C source file
    source_file = "user_program.c"
    create_c_file(source_file, source_code)

    # Step 2: Compile the source code into a binary
    compile_command = f"gcc {source_file} -o {output_file}"

    if output_type == "exe.debug":
        compile_command += " -g3"
    elif output_type == "exe.stripped":
        compile_command += " -s"

    # Parallel compilation
    num_jobs = os.cpu_count()  # Use all available CPU cores
    compile_code_parallel(compile_command, num_jobs)

    # Step 3: Handle different output types
    try:
        if output_type == "tar" or output_type == "tar.gz" or output_type == "tar.bz2":
            subprocess.check_call(f"tar -cvf {output_file} {output_file[:-4]}", shell=True)
            subprocess.check_call(f"gzip {output_file}", shell=True) if "gz" in output_type else subprocess.check_call(f"bzip2 {output_file}", shell=True)

        elif output_type == "img":
            subprocess.check_call(f"dd if={output_file[:-4]} of={output_file} bs=4M", shell=True)

        elif output_type == "so":
            subprocess.check_call(f"gcc -shared -o {output_file} {source_file}", shell=True)

        elif output_type == "ko":
            subprocess.check_call(f"make {source_file}", shell=True)

        messagebox.showinfo("Success", f"Compilation successful! Output saved as {output_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Compilation failed: {e}")

# Set up the main window
root = tk.Tk()
root.title("USINGGCC - Enhanced C Compiler GUI")

# Create variables for the output file name and output type
output_file_var = tk.StringVar()
output_type_var = tk.StringVar(value="exe")  # Default to exe

# Layout configuration
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Source Code Text Area
source_code_label = tk.Label(frame, text="Enter your C code:")
source_code_label.grid(row=0, column=0, sticky="w")
source_code_text = tk.Text(frame, width=50, height=10)
source_code_text.grid(row=1, column=0, columnspan=3)

# Output File Name
output_label = tk.Label(frame, text="Output File Name:")
output_label.grid(row=2, column=0, sticky="w")
output_entry = tk.Entry(frame, textvariable=output_file_var, width=40)
output_entry.grid(row=2, column=1)

# Output Type Selection (exe, bin, or custom)
output_type_label = tk.Label(frame, text="Output Type:")
output_type_label.grid(row=3, column=0, sticky="w")
output_type_menu = tk.OptionMenu(frame, output_type_var, "exe", "bin", "out", "exe.debug", "exe.stripped", "tar", "tar.gz", "tar.bz2", "img", "ko", "so", "json")
output_type_menu.grid(row=3, column=1)

# Compile Button
compile_button = tk.Button(frame, text="Compile and Run", command=compile_code)
compile_button.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
