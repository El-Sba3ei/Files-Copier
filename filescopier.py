import os
from tkinter import Tk, Button, filedialog, Label

def copy_files_to_single_file(file_paths, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            output_file.write(f"{file_name}:\n")
            output_file.write("```\n")

            with open(file_path, 'r') as input_file:
                output_file.write(input_file.read().rstrip())  # Write content without trailing newline

            output_file.write("\n```")  # Add closing triple backticks after the content
            output_file.write("\n\n")  # Add an extra newline after each file's content

def select_files():
    file_paths = filedialog.askopenfilenames(
        title="Choose files to copy",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_paths:
        files_label.config(text="Files selected: " + ", ".join(file_paths))
        update_window_size(len(file_paths))
    else:
        files_label.config(text="No files selected.")
        update_window_size(0)

def select_output_file():
    output_file_path = filedialog.asksaveasfilename(
        title="Choose output file",
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if output_file_path:
        output_label.config(text="Output file: " + output_file_path)
    else:
        output_label.config(text="No output file selected.")

def copy_files():
    if not files_label.cget("text") or not output_label.cget("text"):
        result_label.config(text="Please select files and an output file.")
        return

    file_paths = files_label.cget("text")[15:].split(", ")
    output_file_path = output_label.cget("text")[13:]

    # Check if the file paths contain spaces, if so, remove the double quotes
    file_paths = [file_path.strip().strip('"') if " " in file_path else file_path for file_path in file_paths]

    copy_files_to_single_file(file_paths, output_file_path)

    result_label.config(text="Files copied successfully!")

def update_window_size(num_files):
    window_height = 300 + num_files * 20
    window.geometry(f"400x{window_height}")

# Create the Tkinter window
window = Tk()
window.title("File Copy Tool")
window.geometry("400x300")

# Select Files button
select_files_button = Button(
    window,
    text="Select Files",
    command=select_files,
    width=20,
    height=2
)
select_files_button.pack(pady=10)

# Selected Files label
files_label = Label(window, text="No files selected.", wraplength=300)
files_label.pack()

# Select Output File button
select_output_button = Button(
    window,
    text="Select Output File",
    command=select_output_file,
    width=20,
    height=2
)
select_output_button.pack(pady=10)

# Output File label
output_label = Label(window, text="No output file selected.", wraplength=300)
output_label.pack()

# Copy Files button
copy_files_button = Button(
    window,
    text="Copy Files",
    command=copy_files,
    width=20,
    height=2
)
copy_files_button.pack(pady=10)

# Result label
result_label = Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
