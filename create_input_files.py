from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr30k',
                       karpathy_json_path='./data/Flickr30k/dataset_flickr30k.json',
                       image_folder='./data/Flickr30k/flickr30k-images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='./data/Flickr30k/',
                       max_len=50)
