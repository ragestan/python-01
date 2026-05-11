from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        # STEP 1: Try to open the image
        img = Image.open(path)

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{path}' not found")
    except Exception as e:
        raise Exception(f"Error: Cannot open file '{path}': {str(e)}")

    try:
        # STEP 2: Check format is JPG or JPEG
        img_format = img.format
        if img_format not in ["JPEG", "JPG"]:
            raise ValueError(f"Error: Image format must be JPG or JPEG, got {img_format}")

        # STEP 3: Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")

        # STEP 4: Convert to numpy array
        img_array = np.array(img)

        # STEP 5: Print shape and return
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except ValueError as e:
        raise ValueError(str(e))
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")