from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load a JPEG image and return it as a NumPy array."""
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{path}' not found")
    except Exception as error:
        raise Exception(f"Error: Cannot open file '{path}': {error}")
    try:
        img_format = img.format
        if img_format not in ["JPEG", "JPG"]:
            raise ValueError(
                "Error: Image format must be JPG or JPEG, "
                f"got {img_format}"
            )
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except ValueError as error:
        raise ValueError(str(error))
    except Exception as error:
        raise Exception(f"Error processing image: {error}")


def main():
    """Run a basic image load demonstration with error handling."""


if __name__ == "__main__":
    main()
