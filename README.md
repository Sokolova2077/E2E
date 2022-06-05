# E2E
A training project for E2E
## Data
You can use any png image your soul want
## Model
This has 2 model: Keras and VGG16.
### VGG Architecture: 
The VGG networks with 16
layers (VGG16) was the basis of the Visual Geometry Group (VGG) submission in the ImageNet Challenge 2014, where the VGG team secured the
first and the second places in the localization and classification tracks respectively.
The VGG architecture is structured starting with five blocks of convolutional layers followed by three fully-connected layers. Convolutional layers use 3 × 3 kernels with a stride of 1 and padding of 1 to ensure that each activation map retains the same spatial dimensions as the previous layer. A rectified linear unit (ReLU) activation is performed right after each convolution and a max pooling operation is used at the end of each block to reduce the spatial dimension. Max pooling layers use 2 × 2 kernels with a stride of 2 and no padding to ensure that each spatial dimension of the activation map from the previous layer is halved. Two fully-connected layers with 4096 ReLU activated units are then used before the final 1000 fully-connected softmax layer.


![image](https://user-images.githubusercontent.com/35465478/172067956-804c9b4a-7468-4d1e-908c-964eb9f7397e.png)

### ResNet Architecture: 
Residual Networks (ResNets) are deep convolutional networks where the basic idea is to skip blocks of convolutional layers by using shortcut connections to form blocks named residual blocks. These stacked residual blocks greatly improve training efficiency and largely resolve the degradation problem present in deep networks. In ResNet-50 architecture, the basic blocks follow two simple design rules: (i) for the same output feature map size, the layers have the same number of filters; and (ii) if the feature map size is halved, the number of filters is doubled. The downsampling is performed directly by convolutional layers that have a stride of 2 and batch normalization is performed right after each convolution and before ReLU activation.

![image](https://user-images.githubusercontent.com/35465478/172068069-a95d3816-26ca-4af3-810e-63e8b03dbcbb.png)

## How to run on VM
To run on your machine user needs to do several steps:

 1. Install	the Python 3 interpreter
 2. Install the needed Python 3 libraries: 
  - Flask
  - NumPy
  - tensorflow
  - io
 3. Create a git folder
 4. Make git pull and download all folders from the github
 5. Make ***python app.py*** 
 6. then launch it: ***flask run --host=0.0.0.0***
