#!/usr/bin/env python3
"""
Brain Tumor Segmentation — Complete Pipeline
=============================================
Dataset    : BraTS 2020 (Kaggle: awsaf49/brats2020-training-data)
Methods    : Otsu, K-Means, Active Contour, U-Net, PyramidUNet
Framework  : TensorFlow 2.19 / Keras
Platform   : Google Colab (GPU)
"""

# ── INSTALL ──────────────────────────────────────────────────
# !pip install -q nibabel scikit-image opencv-python-headless tensorflow kaggle

# ── IMPORTS ──────────────────────────────────────────────────
import os, h5py, cv2, time
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from skimage import filters, morphology
from skimage.segmentation import active_contour
from skimage.draw import polygon
from scipy import ndimage
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

DATA_PATH = '/content/brats2020/BraTS2020_training_data/content/data'

# See full implementation in Brain_Tumor_Segmentation.ipynb
print("Run Brain_Tumor_Segmentation.ipynb for complete pipeline")
