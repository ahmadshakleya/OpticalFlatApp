from numpy.fft import fft2, ifft2, fftshift, ifftshift
from imageio.v2 import imread
import logging
import numpy as np

def load_image(image_path):
    """Load an image from the disk as 8-bit grayscale."""
    image = imread(image_path, mode='L')
    logging.info(f"Image loaded from {image_path}.")
    return image

def perform_fft(image):
    """Perform a 2D Fast Fourier Transform."""
    fft_result = fftshift(fft2(image))
    logging.info("FFT performed on image.")
    return fft_result

def filter_frequencies(fft_image, threshold=10):
    """Isolate the central frequency peak."""
    magnitude = np.abs(fft_image)
    max_val = np.max(magnitude)
    mask = magnitude > (max_val / threshold)
    logging.info("Frequencies filtered.")
    return fft_image * mask

def perform_ifft(fft_image):
    """Perform an inverse FFT to get the filtered image back in spatial domain."""
    ifft_result = ifft2(ifftshift(fft_image))
    logging.info("Inverse FFT performed.")
    return ifft_result

def extract_phase(image):
    """Extract the phase of the complex image."""
    phase = np.angle(image)
    logging.info("Phase extracted from image.")
    return phase

def calculate_height_map(phase, wavelength=632.8e-9, refractive_index=1.5):
    """Calculate the height map from the unwrapped phase map."""
    calibration_factor = 10e16
    height_map = (wavelength * calibration_factor * phase) / (2 * np.pi * refractive_index)
    logging.info("Height map calculated.")
    return height_map