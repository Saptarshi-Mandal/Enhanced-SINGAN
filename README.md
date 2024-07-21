# Enhanced SinGAN
This is an improvement on an unofficial implementation of SinGAN


<p align="center">
  <img width="992" height="372" src="/figures/sampled.png">
</p>

Please refer the project's [page](https://github.com/kligvasser/SinGAN) for the unofficial implementation.

## Problem Statement

### Introduction
This project aims to enhance the SinGAN model [(Shaham et al., ICCV, 2019)](https://openaccess.thecvf.com/content_ICCV_2019/papers/Shaham_SinGAN_Learning_a_Generative_Model_From_a_Single_Natural_Image_ICCV_2019_paper.pdf) and overcome its limitations, particularly its reliance on a single input image and sensitivity to image quality. We propose to develop a more robust and versatile generative model independent of input image quality.

### Objectives
1. **Enhance Robustness:** Reduce SinGAN’s sensitivity to input image quality by developing a model that can effectively generate high-quality outputs even from noisy input images. We plan to implement the following approaches:
    - **Introduction of Losses:**
        - **Perceptual Loss:** Euclidean distance between the feature maps of two images (generated and actual images) extracted from a pretrained image classification network such as VGG or ResNET.
        - **Total Variational Loss:** Measures the total amount of variation in the image, focusing on preserving sharp edges while smoothing out flat areas and reducing noise.
    - **Image Preprocessing:** Implement denoising using the following approaches on the input image before feeding it to the SinGAN network.
        - **Classical Techniques:** Mean and median filter.

### Comparison and Analysis
We will conduct a comparison and extensive analysis of the above modifications on the quality of the generated images.

## Results
<p align="center">
  <img src="/Results/results.png">
</p>

For more details checkout ``` ./Results/IQA - ref and gen images.xlsx ```.

## Code

### Clone repository

Clone this repository into any place you want.

```
git clone https://github.com/saptarshi-mandal/Enhacned-SINGAN
cd ./SinGAN/generation/
```

### Install dependencies

```
python -m pip install -r requirements.txt
```

This code tested in PyTorch 1.8.1.

### Training
To train SinGAN model on your own image:

```
python3 main.py --root <path-to-image>
```

### Evaluating
For evaluating, run the following command:

```
python3 main.py --root <path-to-image> --evaluation --model-to-load <path-to-model-pt> --amps-to-load <path-to-amp-pt> --num-steps <number-of-samples> --batch-size <number-of-images-in-batch>
```
