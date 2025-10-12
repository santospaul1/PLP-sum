import os

def process_and_count(input_filename="input.txt", output_filename="output.txt"):
    
    print(f"Starting processing: Reading from '{input_filename}'...")

    try:
        # 1. Read the contents of input.txt
        with open(input_filename, 'r') as infile:
            original_content = infile.read()

        if not original_content.strip():
            print(f"Warning: The input file '{input_filename}' is empty.")
            return

        # 2. Convert all text to uppercase
        uppercase_content = original_content.upper()

        # 3. Count the number of words in the file
        
        words = original_content.split()
        word_count = len(words)

        # 4. Prepare the content for the output file
        output_data = (
           f"{uppercase_content}"
        )

        # 5. Write the processed text and word count to output.txt
        with open(output_filename, 'w') as outfile:
            outfile.write(output_data)

        # 6. Print a success message
        print(f"Success! Output written to '{output_filename}'.")
        print(f"Total Words Counted: {word_count}")

    except FileNotFoundError:
        print(f"\nError: Input file '{input_filename}' not found. Please ensure it is in the same directory.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    process_and_count()
