# Attention-Beam-Image-Captioning

We present a heuristic of beam search on top of the encoder-decoder based architecture that gives better quality captions on three benchmark datasets: Flickr8k, Flickr30k and MS COCO.

## Dependencies

For dependencies related to this project, `environment.yml` and `requirements.txt` files have been provided.

To install the dependencies using conda: 

```bash
conda env create -f environment.yml
conda env list
```

## Training

Reference data folder and annotations json file for the downloaded dataset (MSCOCO, Flickr8k, Flickr30k) in `create_input_files.py` and run the python script to create the required dataset.

To train a model run `python train.py`.
All training hyper-parameters are mentioned in `train.py`.

**Note: Pretrained models for MSCOCO, Flickr8k, Flickr30k can be downloaded from [here](https://drive.google.com/file/d/1kPeKtfuBNjFslJ33ftbNtygtE1NM0n7L/view?usp=sharing).**

## Testing / Inference

* You may use `caption.py` to generate image captions and attention map over an image.

  ```
  python caption.py --img='path/to/image.jpeg' --model='path/to/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar' --word_map='path/to/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json' --beam_size=5
  ```

* The Jupyter Notebook `Caption-Sample-Images.ipynb` can be used to caption specified images using the trained model.
* `Generate-Testset-Predictions.ipynb` is used for generating predictions in the required format for the testing dataset.

## Results

![results table](./img/results.png)

![comparing captions](./img/compare_captions.png)

<div style='text-align: center;'>
  <img src="./img/1.png" alt="image1">
  <img src="./img/1a.png" alt="image1a">
</div>
<div style='text-align: center;'>
  <img src="./img/2.png" alt="image2">
  <img src="./img/2a.png" alt="image2a">
</div>
<div style='text-align: center;'>
  <img src="./img/3.png" alt="image3">
  <img src="./img/3a.png" alt="image3a">
</div>