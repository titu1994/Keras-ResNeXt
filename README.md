# Keras ResNeXt

Implementation of ResNeXt models from the paper [Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/pdf/1611.05431.pdf) in Keras 2.0+.

Contains code for building the general ResNeXt model (optimized for datasets similar to CIFAR) and ResNeXtImageNet (optimized for the ImageNet dataset).

# Salient Features
ResNeXt updates the ResNet block with a new expanded block architecture, which depends on the `cardinality` parameter. It can be further visualised in the below diagram from the paper.

![cardinality](https://github.com/titu1994/Keras-ResNeXt/blob/master/images/Cardinality.PNG?raw=true)

---
However, since grouped convolutions are not directly available in Keras, an equivalent variant is used in this repository (see block 2)

![equivalent blocks](https://github.com/titu1994/Keras-ResNeXt/blob/master/images/equivalent_blocks.PNG?raw=true)

# Usage

For the general ResNeXt model (for all datasets other than ImageNet),

```
from resnext import ResNeXt

model = ResNeXt(image_shape, depth, cardinality, width, weight_decay)
```

For the ResNeXt model which has been optimized for ImageNet,

```
from resnext import ResNeXtImageNet

image_shape = (112, 112, 3) if K.image_data_format() == 'channels_last' else (3, 112, 112)
model = ResNeXtImageNet(image_shape)
```

Note, there are other parameters such as depth, cardinality, width and weight_decay just as in the general model, however the defaults are set according to the paper.
