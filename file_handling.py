import os

def file_transformer_lab():
    
    output_filename = "transformed_output.txt"
    input_filename = ""
    
    while True:
        # Ask the user for the input filename
        input_filename = input("Enter the input filename (or type 'quit' to exit): ").strip()
        
        if input_filename.lower() == 'quit':
            print("Exiting the file transformer lab. Goodbye!")
            return

        print(f"\nAttempting to process '{input_filename}'...")
        
        try:
            #  Attempt to Read the File ---
            
            with open(input_filename, 'r', encoding='utf-8') as infile:
                original_content = infile.read()
            
            # Simple Processing: convert content to uppercase
            processed_content = original_content.upper()
            
            # Attempt to Write the File ---
            # Prepare the final data to be written
            line_count = processed_content.count('\n') + 1
            word_count = len(processed_content.split())
            
            output_data = (
                
                f"Source File: {input_filename}\n"
                f"Lines Processed: {line_count}\n"
                f"Words Processed: {word_count}\n"
                
                f"{processed_content}"
            )
            
            # Using 'w' mode to write (overwrites existing file)
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                outfile.write(output_data)
            
            # Success Message (break the loop)
            print(f"\n SUCCESS: File processed and written to '{output_filename}'.")
            print("You can run the program again to process another file.")
            break # Exit the while loop on success

        # --- Error Handling ---
        
        # Handle case where the file does not exist
        except FileNotFoundError:
            print(f"ERROR: File not found. The file '{input_filename}' does not exist.")
            print("Please check the filename and try again.")
            # Continue the loop to prompt the user again

        # Handle general OS-related IO errors (e.g., permission issues, device full)
        except IOError as e:
            print(f"ERROR: An input/output error occurred while reading or writing.")
            print(f"Details: {e}")
            # Continue the loop to prompt the user again
            
        # Handle any other unexpected errors
        except Exception as e:
            print(f" CRITICAL ERROR: An unexpected error occurred.")
            print(f"Details: {e}")
            # Continue the loop to prompt the user again


if __name__ == "__main__":
    file_transformer_lab()
