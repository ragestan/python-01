from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load a JPEG image and return it as a NumPy array."""
    try:
        # STEP 1: Try to open the image
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{path}' not found")
    except Exception as error:
        raise Exception(f"Error: Cannot open file '{path}': {error}")
    try:
        # STEP 2: Check format is JPG or JPEG
        img_format = img.format
        if img_format not in ["JPEG", "JPG"]:
            raise ValueError(
                "Error: Image format must be JPG or JPEG, "
                f"got {img_format}"
            )
        # STEP 3: Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")

        # STEP 4: Convert to numpy array
        img_array = np.array(img)

        # STEP 5: Print shape and return
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
