# Face Age Regression
We proposed a CNN network for Mnist Persian regression. We used framework pytorch==1.8.2.  


  <table>
    <tr>
      <center>     
        <img src="https://user-images.githubusercontent.com/80582110/147503753-4e3cfc86-a4ae-4e76-bb58-514076965d71.png">
      </center>
    </tr>
  </table>


## Train
To train the model, please run the file:

`face_age.ipynb`

## Pretrained model
Please download the weights from [here](https://drive.google.com/file/d/1-aiOwRsQnzMWBHd_FAeXqcuD74ccSuoY/view?usp=sharing)  

## Inference
To test the trained model, please run the following file:

`python inference.py --img_path data/2.jpeg --model_path age_weight.pth --device GPU`
