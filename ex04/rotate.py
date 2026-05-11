from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def manual_transpose(array_2d):
    """
    Manually transpose a 2D array without using library transpose functions.
    Converts element at [i][j] to [j][i]
    """
    rows = len(array_2d)
    cols = len(array_2d[0])

    # Create new 2D list for transposed array
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Manually swap indices
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = array_2d[i][j]

    # Convert back to numpy array
    return np.array(transposed)


def main():
    """
    Load animal.jpeg, crop 400x400, convert to grayscale, transpose, and display.
    """
    try:
        # STEP 1: Load the image
        img_path = "animal.jpeg"
        img = Image.open(img_path)

        # STEP 2: Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")

        # STEP 3: Convert to numpy array
        img_array = np.array(img)

        # STEP 4: Crop a 400x400 square from center
        height, width, channels = img_array.shape

        start_x = (width - 400) // 2
        start_y = (height - 400) // 2
        end_x = start_x + 400
        end_y = start_y + 400

        cropped = img_array[start_y:end_y, start_x:end_x]

        # STEP 5: Convert to grayscale
        cropped_float = cropped.astype(float)
        grayscale = (0.299 * cropped_float[:, :, 0] +
                     0.587 * cropped_float[:, :, 1] +
                     0.114 * cropped_float[:, :, 2]).astype(np.uint8)

        # Shape can be (400, 400, 1) or (400, 400)
        grayscale_3d = grayscale[:, :, np.newaxis]

        # STEP 6: Print original cropped image info
        print(f"The shape of image is: {grayscale_3d.shape} or {grayscale.shape}")
        print(grayscale_3d)

        # STEP 7: Convert 3D array to 2D for transpose
        grayscale_2d = grayscale  # This is (400, 400)

        # STEP 8: Manually transpose the 2D array
        transposed = manual_transpose(grayscale_2d.tolist())

        # STEP 9: Print transposed image info
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # STEP 10: Display both images
        fig, axes = plt.subplots(1, 1, figsize=(12, 5))

        # Display original grayscale
        #axes[0].imshow(grayscale, cmap='gray')
        #axes[0].set_title("Original (400x400 Grayscale)")
        #axes[0].set_xlabel("X axis")
        #axes[0].set_ylabel("Y axis")

        # Display transposed
        axes.imshow(transposed, cmap='gray')
        axes.set_title("Transposed (400x400)")
        axes.set_xlabel("X axis")
        axes.set_ylabel("Y axis")

        plt.show()

    except FileNotFoundError:
        print(f"Error: File 'animal.jpeg' not found")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
