import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter to the image."""
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    Image.fromarray(result).show()
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter to the image."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    Image.fromarray(result).show()
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter to the image."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    Image.fromarray(result).show()
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    result = array.copy()
    grey_values = array.mean(axis=2).astype(np.uint8)
    result[:, :, 0] = grey_values
    result[:, :, 1] = grey_values
    result[:, :, 2] = grey_values
    Image.fromarray(result).show()
    return result


def main():
    """Load an image and apply basic color filters with error handling."""


if __name__ == "__main__":
    main()
