from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Load, crop, grayscale, and display a zoomed image."""
    try:
        # STEP 1: Load the image
        img_path = "animal.jpeg"
        img = Image.open(img_path)
        # STEP 2: Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")
        # STEP 3: Convert to numpy array
        img_array = np.array(img)
        # STEP 4: Print original image info
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
        # STEP 5: Crop a 400x400 region from center
        # Get image dimensions
        height, width, _ = img_array.shape
        # Calculate center crop (400x400 from middle)
        start_x = (width - 400) // 2
        start_y = (height - 400) // 2
        end_x = start_x + 400
        end_y = start_y + 400
        # Crop the region
        cropped = img_array[start_y:end_y, start_x:end_x]
        # STEP 6: Convert cropped region to grayscale
        # Convert uint8 RGB to float for calculation
        cropped_float = cropped.astype(float)
        # Grayscale formula: 0.299*R + 0.587*G + 0.114*B
        grayscale = (0.299 * cropped_float[:, :, 0] +
                     0.587 * cropped_float[:, :, 1] +
                     0.114 * cropped_float[:, :, 2]).astype(np.uint8)
        # Reshape to (400, 400, 1) to match expected format
        grayscale_3d = grayscale[:, :, np.newaxis]
        # STEP 7: Print cropped/zoomed image info
        print(f"New shape after slicing: {grayscale_3d.shape}")
        print(grayscale_3d)
        # STEP 8: Display images with matplotlib
        _, axes = plt.subplots(1, 1, figsize=(15, 6))
        # Display zoomed/cropped grayscale
        axes.imshow(grayscale, cmap='gray')
        axes.set_title("Zoomed (400x400) - Grayscale")
        axes.set_xlabel("X axis")
        axes.set_ylabel("Y axis")
        plt.show()
    except FileNotFoundError:
        print("Error: File 'animal.jpeg' not found")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
