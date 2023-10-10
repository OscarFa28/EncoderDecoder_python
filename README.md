# EncoderDecoder_python

This Python program allows you to encode and decode text messages using a custom alphabet generated from the frequency of characters in a given text file. It leverages a priority queue (heap) implementation to efficiently process and transform text messages.

## Features

- `CharList` class to represent characters and their frequencies.
- `EncoderDecoder` class for encoding and decoding messages.
- Read text content from a specified .txt file to build a custom alphabet.
- Encode a message into a list of indices based on the custom alphabet.
- Decode a list of indices back into a readable message.
- Handles lowercase letters and spaces.

## Usage

1. Ensure that a text file containing the source text for building the custom alphabet is available in the repository.

2. Create an instance of the `EncoderDecoder` class and load the text from the file using the `get_text` method.

3. Encode a message by calling the `encode_message` method with a lowercase string.

4. Decode a message by calling the `decode_message` method with a list of indices.


