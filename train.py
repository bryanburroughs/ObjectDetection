import numpy as np
import os

from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

from tflite_support import metadata

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)



train_data = object_detector.DataLoader.from_pascal_voc(
    'trainingdata/train',
    'trainingdata/train',
    ['clownfish', 'rubikscube'] #labels should correspond to the image labels created in labelImg
)

val_data = object_detector.DataLoader.from_pascal_voc(
    'trainingdata/validate',
    'trainingdata/validate',
    ['clownfish', 'rubikscube'] #labels should correspond to the image labels created in labelImg
)





#spec = model_spec.get('efficientdet_lite0')
spec = model_spec.get('efficientdet_lite0', model_dir='tbdir')
#model_dir is needed for TensorBoard

#add some notes here on tuning the model


#model = object_detector.create(train_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=20, validation_data=val_data)
model = object_detector.create(train_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=100, validation_data=val_data)



model.evaluate(val_data)


model.export(export_dir='.', tflite_filename='best.tflite')
