import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix, huffman_code):
    if node:
        if node.char is not None:
            huffman_code[node.char] = prefix
        generate_codes(node.left, prefix + "0", huffman_code)
        generate_codes(node.right, prefix + "1", huffman_code)

def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_code = {}
    generate_codes(root, "", huffman_code)
    return huffman_code

if __name__ == "__main__":
    Exit = True
    huffman_code = {}
    while Exit:
      print("1) Build Huffman Tree")
      print("2) Encode given string")
      print("3) Decode given string")
      print("4) Exit")
      choice = int(input("Enter your choice : "))
      if choice == 1:
          huffman_code = {}
          Input_data = str(input("Enter your data for building Huffman Tree : "))
          Huffman_tree = build_huffman_tree(Input_data)
          generate_codes(Huffman_tree, "", huffman_code)
          print(huffman_code)
      if choice == 2:
          encoded_text = ''.join(huffman_code[char] for char in Input_data)
          print("Encoded string is ",encoded_text)
      if choice == 3:
          print("Decoded string is ",Input_data)
      if choice == 4:
          Exit = False

        