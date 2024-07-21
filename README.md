# Enhanced SinGAN
This is an improvement on an unofficial implementation of SinGAN

<p align="center">
  <img width="992" height="372" src="/figures/sampled.png">
</p>

Please refer the project's [page](https://github.com/kligvasser/SinGAN) for the unofficial implementation.

## Introduction
The project implements the **Enhanced SinGAN** model, a robust and versatile version of the original SinGAN model [(Shaham et al., ICCV, 2019)](https://openaccess.thecvf.com/content_ICCV_2019/papers/Shaham_SinGAN_Learning_a_Generative_Model_From_a_Single_Natural_Image_ICCV_2019_paper.pdf). The Enhanced SinGAN is designed to be less sensitive to input image quality, enabling it to generate clean images even from noisy inputs.

## Features
1. **Enhance Robustness:** Improve SinGAN’s ability to handle varying image quality by developing a model that generates high-quality outputs even from noisy input images. This is achieved through the following  approaches:
    - **Introduction of Losses:**
        - **Total Variational Loss:** This loss penalizes differences between neighboring pixels both horizontally and vertically. It is a measure of the variation in an image, focusing on preserving sharp edges  while smoothing out flat areas and reducing noise.
    - **Image Preprocessing:** Denoise and sharpen the noisy input image before feeding it to the SinGAN network.
        - **Classical Denoising Techniques:** Non Local Means, Bilateral Filtering
        - **Classical Sharpening Techniques:** High Boost Filtering, Adaptive Histogram Equalization

## Results
The following are sample images geenrated by the Enhances SinGAN model:


For more details checkout ``` ./Results/IQA - ref and gen images.xlsx ```.

## Comparison and Analysis
The following is a comparison and extensive analysis of the above modifications on the quality of the generated images.

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
