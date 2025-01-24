from nltk.tokenize import sent_tokenize, word_tokenize
import json
import os

def split_into_chunks(transcript_path, max_tokens=4096):

    """Helper function to split content into chunks using fixed size chunking."""
    with open(transcript_path, 'r') as file:
        content = file.read()
    sentences = sent_tokenize(content)
    chunks = []
    current_chunk = ''
    current_count = 0
    chunk_no = 1
    for sentence in sentences:
        sentence_words = word_tokenize(sentence)
        sentence_length = len(sentence_words)

        if current_count + sentence_length <= max_tokens:
            current_chunk += ' ' + sentence
            current_count += sentence_length
        else:
            chunks.append({'chunk_number': chunk_no, 'text':current_chunk.strip()})
            current_chunk = sentence
            current_count = sentence_length
            chunk_no+=1
   
    if current_chunk:  # Add the last chunk if it's not empty
        chunks.append({'chunk_number': chunk_no, 'text':current_chunk.strip()})
    
    cp = os.path.join(os.getcwd(),'output','chunks.json')
    with open(cp, 'w') as f:
        json.dump(chunks, f, indent=1)
    return "Complete"


def text_to_chunks(texts: list[str], 
                   word_length: int = 1000, 
                   start_page: int = 1) -> list[list[str]]:
    """
    Splits the text into equally distributed chunks.

    Args:
        texts (str): List of texts to be converted into chunks.
        word_length (int): Maximum number of words in each chunk.
        start_page (int): Starting page number for the chunks.
    """
    text_toks = [t.split(' ') for t in texts]
    chunks = []

    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i:i+word_length]
            if (i+word_length) > len(words) and (len(chunk) < word_length) and (
                len(text_toks) != (idx+1)):
                text_toks[idx+1] = chunk + text_toks[idx+1]
                continue
            chunk = ' '.join(chunk).strip() 
            chunk = f'[Page no. {idx+start_page}]' + ' ' + '"' + chunk + '"'
            chunks.append(chunk)
            
    return chunks