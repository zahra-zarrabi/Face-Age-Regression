# Face Age Regression
We proposed a CNN network for Mnist Persian classification. We used framework pytorch==1.8.2.



## Train
To train the model please run the file `train.ipy`

## Pretrained model
Please download the weights from [here](https://drive.google.com/file/d/1CbouHYVoRUF8d_wC8i0D7SysXoA_DYpD/view?usp=sharing)  

## Inference
to test the trained model, please run the following file:

`python inference.py --img_path data/2.jpeg --model_path model_mnist.pth --device GPU`
