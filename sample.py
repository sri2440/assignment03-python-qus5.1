def modify_content(input_file, output_file):
    try:
        # Read content from the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (replace 'old' with 'new' as an example)
        modified_content = content.replace('old', 'new')

        # Write the modified content to a new file using 'w' mode
        with open(output_file, 'w') as file:
            file.write(modified_content)

        # Append some additional content to the new file using 'a' mode
        with open(output_file, 'a') as file:
            file.write('\nAppended content.')

        print(f"File modification successful. Check '{output_file}' for changes.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file_path = 'example.txt'
output_file_path = 'modified_example.txt'

modify_content(input_file_path, output_file_path)
