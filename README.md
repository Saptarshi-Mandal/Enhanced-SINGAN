# Enhanced SinGAN
This is an improvement on an unofficial implementation of SinGAN


<p align="center">
  <img width="992" height="372" src="/figures/sampled.png">
</p>


Please refer the project's [page](https://github.com/kligvasser/SinGAN) for the unofficial implementation.


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
