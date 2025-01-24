import re

def remove_text_before_webvtt(text):
    
    """Helper function to remove text before "WEBVTT in transcript file."""
    index_webvtt = text.find("WEBVTT")
    txt1 =  text[index_webvtt + len("WEBVTT"):] if index_webvtt != -1 else text
      
    return txt1


def remove_timestamp_pattern(text):
    
    """Helper function to remove timestamp format in transcript file."""

    pattern = r'\b[a-zA-Z]+\s\d{2}:\d{2}:\d{2}\.\d{3}\s-->\s\d{2}:\d{2}:\d{2}\.\d{3}\b'
    txt1 =  re.sub(pattern, '', text)
    txt1 = re.sub(' +', ' ', txt1)     # remove additional space from string

    return txt1
 

def preprocess_content(text):

    """Helper function to convert transcript in a standarized conversation format."""

    lines = text.split('\n')
    result = ''
    current_speaker = None

    for line in lines:
        if line.strip().isdigit():
            current_speaker = None
        elif line.strip() and current_speaker is None:
            current_speaker = line.strip()
        elif line.strip():
            result += f'{current_speaker} : {line}\n\n'

    res = result.replace(".\n\n", ";\n\n")     # Replace ".\n\n" with ";\n"

    return res.strip()