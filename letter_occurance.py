class UserMainCode:
    @classmethod
    def distinctCharacters(cls, input1):
        # Create a dictionary to store character counts
        char_count = {}
        
        # Count the frequency of each character in the input string
        for char in input1:
            if char.isalpha():  # Check if the character is a letter
                char = char.lower()  # Convert to lowercase for case insensitivity
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        
        # Sort the dictionary by values in descending order
        sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
        
        # Get the three most common characters and their counts
        most_common = {}
        count = 0
        for char, freq in sorted_char_count.items():
            most_common[char] = freq
            count += 1
            if count >= 3:
                break
        
        # Format the result as a string
        result_str = "{"
        for char, freq in most_common.items():
            result_str += f'"{char}":{freq},'
        result_str = result_str.rstrip(',')  # Remove the trailing comma
        result_str += "}"
        
        return result_str

input1=input("Enter the string: ")
result= UserMainCode.distinctCharacters(input1)
print(result)