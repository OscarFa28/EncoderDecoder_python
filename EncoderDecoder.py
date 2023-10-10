from priority_queue import Heap, HeapNode
import math
import os

class CharList:
    def __init__(self, letter, repeats):
        self.letter = letter  # The letter (a-z) without ñ
        self.repeats = repeats  # Number of repetitions

class EncoderDecoder:
    def __init__(self):
        self.text = None
        self.repeats = []
        self.message = None

    def generate_list(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        self.repeats = []
        
        for letter in letters:
            count = self.__char_to_index(letter)
            char_list = CharList(letter, count)
            self.repeats.append(char_list)

    def __char_to_index(self, c):
        count = 0
        for i in range(len(self.text)):
            if self.text[i] == c:
                count += 1
        return count  
    
    def __index_to_char(self, idx):
        return self.repeats[idx].letter
    
    def get_text(self, file):  # Open a .txt file and store its content in program memory
        with open(file, 'r') as archivo:
            txt = archivo.read()
            self.text = txt.lower()
            
    def generate_alphabet(self):  # Generate the new alphabet with the order corresponding to character frequency in the text.
        my_heap = Heap()
        
        elements = [HeapNode(char_list.repeats, char_list) for char_list in self.repeats]

        my_heap.build_heap(elements)

        sorted_result = []

        while my_heap.get_size() > 0:
            max_node = my_heap.heap_extract_max()
            sorted_result.append(max_node.value) 

        self.repeats = sorted_result
    
    def decode_message(self, num_message):  # Receive a list of integers and transform it into a message string based on the indices contained in the list.
        decoded_message = ''
        for index in num_message:
            if index == -1:
                decoded_message += ' '  # Space for index -1
            else:
                char = self.__index_to_char(index)
                decoded_message += char
        return decoded_message
    
    def encode_message(self, message):  # Receive a string and transform it into a list of indices corresponding to the position of each letter in the modified alphabet
        self.generate_list()
        self.generate_alphabet()
        self.message = message
        encoded_message = []
        
        for i in range(len(message)):
            position = -1  # Initialize the position as -1 (space)
            if message[i] != ' ':
                char = message[i]
                for j in range(len(self.repeats)):
                    if message[i] == ' ':
                        position = -1
                        break
                
                    elif self.repeats[j].letter == message[i]:
                        position = j
                        break
                
            encoded_message.append(position)

        return encoded_message
        

# Information    
current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = 'text_to_build_alphabet.txt' #file name
file_name = os.path.join(current_directory, relative_path)

message = "codifica este mensaje"  #message to encode (only lowercase letters)
num_message = [0, 5, -1, 7, 0, 2, 10, 8, 9, 2, 9, -1, 5, 3, -1, 6, 2, 18, 0, 14, 3, 6, -1, 4, 2, 13, 21, 0, 2, 7] #message to decode (only from -1 - 25)

enc = EncoderDecoder()
enc.get_text(file_name) 

print('The encoded message is: '+ str(enc.encode_message(message)))
print('The encoded and then decoded message is: '+ enc.decode_message(num_message))
