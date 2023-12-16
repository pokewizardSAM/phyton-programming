import random

def generate_pan_card_number():
    # Generate the first three characters (letters)
    first_three = ""
    for _ in range(3):
        first_three += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Generate the fourth character based on the status
    status_mapping = {
        'C': 'Company',
        'P': 'Person',
        'H': 'HUF',
        'F': 'Firm',
        'A': 'Association of Persons (AOP)',
        'T': 'AOP (Trust)',
        'B': 'Body of Individuals (BOI)',
        'L': 'Local Authority',
        'J': 'Artificial Juridical Person',
        'G': 'Government'
    }
    status = 'P'  # Default status is 'Person'
    status_char = random.choice('CPHFATBLJG')
    if status_char in status_mapping.keys():
        status = status_char

    # Generate the fifth character (surname or entity name)
    name = ""
    if status == 'P':
        name = 'SAHU'

    # Generate the sixth to ninth characters (sequential numbers)
    seq_numbers = str(random.randint(1, 9999)).zfill(4)

    # Calculate the checksum character
    pan_number_without_checksum = first_three + status + name + seq_numbers
    checksum = calculate_checksum(pan_number_without_checksum)

    # Generate the complete PAN card number
    pan_card_number = pan_number_without_checksum + checksum

    return pan_card_number

def calculate_checksum(pan_number):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    weighted_sum = 0

    for i in range(len(pan_number) - 1):
        if pan_number[i].isdigit():
            weighted_sum += int(pan_number[i]) * weights[i]
        else:
            weighted_sum += (ord(pan_number[i]) - ord('A') + 10) * weights[i]

    remainder = weighted_sum % 11
    checksum = alphabets[remainder]

    return checksum

# Example usage
pan_number = generate_pan_card_number()
print(pan_number)
