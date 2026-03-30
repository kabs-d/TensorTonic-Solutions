import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)
    padded =[]
    for seq in seqs:
        new_seq = seq[:max_len]
        while(len(new_seq)<max_len):
            new_seq.append(pad_value)
        padded.append(new_seq)
    return np.array(padded)