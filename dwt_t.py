# -*- coding: utf-8 -*-
"""DWT-T

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XYnqoXfsdKj2oKVD8wXdpxvBj-IJayFT

First import the libs
"""

import pywt
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt


def get_dwt(image='work/original/cameraman.tif'):
    """Read the image"""

    original_image = np.float32(cv2.imread(image, cv2.IMREAD_GRAYSCALE))

    if __name__ == "__main__":
        # Check data type of image
        print('Data type: '+str(original_image.dtype))
        print('Pixel intensity range: (%d,%d)' % (original_image.min(), original_image.max()))

        # Print image shape
        print(original_image.shape)

        plt.imshow(original_image, cmap="gray")

    # Get the DWT Co-effitients with running time
    s = time.time()
    coeffs = pywt.dwt2(original_image, 'haar')
    LL, (LH, HL, HH) = coeffs

    # Perform thresholding

    thresh = 0.1
    LL_thresh = LL * (np.absolute(LL) > thresh*np.max(np.absolute(LL)))
    LH_thresh = LH * (np.absolute(LH) > thresh*np.max(np.absolute(LH)))
    HL_thresh = HL * (np.absolute(HL) > thresh*np.max(np.absolute(HL)))
    HH_thresh = HH * (np.absolute(HH) > thresh*np.max(np.absolute(HH)))
    e = time.time()
    compression_time = e - s

    if __name__ == "__main__":
        # Show original coeffs

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 4, 1)
        plt.imshow(LL, cmap='gray')
        plt.subplot(1, 4, 2)
        plt.imshow(LH, cmap='gray')
        plt.subplot(1, 4, 3)
        plt.imshow(HL, cmap='gray')
        plt.subplot(1, 4, 4)
        plt.imshow(HH, cmap='gray')
        plt.show(block=False)

    # Reconstruct image with running time
    s = time.time()
    reconstructed_image = pywt.idwt2((LL_thresh, (LH_thresh, HL_thresh, HH_thresh)), 'haar')
    e = time.time()
    decompression_time = e - s

    if __name__ == "__main__":
        # Plot decompressed (reconstructed image)
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 3, 1)
        plt.imshow(original_image, cmap='gray')
        plt.subplot(1, 3, 2)
        plt.imshow(reconstructed_image, cmap='gray')
        plt.subplot(1, 3, 3)
        plt.imshow(original_image-reconstructed_image, cmap='gray')
        plt.show(block=False)

    # Compute compression ratio
    compression_ratio = original_image.size / np.sum(reconstructed_image != 0.0)
    if __name__ == "__main__":
        print('Compression ratio: %.1f:1' % (compression_ratio))

    # Compute Peak Signal to Noise Ratio (PSNR)
    MSE = np.sum((original_image-reconstructed_image)**2)/original_image.size
    PSNR = 10*np.log10(np.max(original_image)**2/MSE)
    if __name__ == "__main__":
        print('PSNR: %.2f dB' % PSNR)

    return (compression_ratio, compression_time, decompression_time, MSE, PSNR, reconstructed_image)


get_dwt()
