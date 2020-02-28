import torch
import numpy as np 
import pickle 
import os
from PIL import Image
import json
import sys
sys.path.append('../')

from caption import caption_image_beam_search


# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

default_args = {
    'model':'../models/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar',
    'word_map':'../models/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'
}

def caption(image_path, args=None):    
    if args is None:
        args = default_args
    
    if not os.path.exists(args['model']) or not os.path.exists(args['word_map']):
        print('Pretrained model files not found.\n', args)
        return None

    # Load model
    checkpoint = torch.load(args['model'], map_location=torch.device('cpu'))
    decoder = checkpoint['decoder']
    decoder = decoder.to(device)
    decoder.eval()
    encoder = checkpoint['encoder']
    encoder = encoder.to(device)
    encoder.eval()
    
    # Load word map (word2idx)
    with open(args['word_map'], 'r') as j:
        word_map = json.load(j)
        
    # idx2word
    rev_word_map = {v: k for k, v in word_map.items()}  
    

    seq, alphas = caption_image_beam_search(encoder, decoder, image_path, word_map, 4)
    
    sampled_caption = [rev_word_map[ind] for ind in seq]
    sampled_caption = []
    for ind in seq[1:]:
        word = rev_word_map[ind]
        if word == '<end>':
            break
        sampled_caption.append(word)
        
    sentence = ' '.join(sampled_caption)

    return sentence