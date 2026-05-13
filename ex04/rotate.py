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
    """Load, crop, grayscale, transpose, and display an image."""
    try:
        img_path = "animal.jpeg"
        img = Image.open(img_path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        height, width, _ = img_array.shape
        start_x = (width - 400) // 2
        start_y = (height - 400) // 2
        end_x = start_x + 400
        end_y = start_y + 400
        cropped = img_array[start_y:end_y, start_x:end_x]
        cropped_float = cropped.astype(float)
        grayscale = (0.299 * cropped_float[:, :, 0] +
                     0.587 * cropped_float[:, :, 1] +
                     0.114 * cropped_float[:, :, 2]).astype(np.uint8)
        grayscale_3d = grayscale[:, :, np.newaxis]
        print(
            f"The shape of image is: {grayscale_3d.shape} or {grayscale.shape}"
        )
        print(grayscale_3d)
        grayscale_2d = grayscale
        transposed = manual_transpose(grayscale_2d.tolist())
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        _, axes = plt.subplots(1, 1, figsize=(12, 5))
        axes.imshow(transposed, cmap='gray')
        axes.set_title("Transposed (400x400)")
        axes.set_xlabel("X axis")
        axes.set_ylabel("Y axis")
        plt.show()
    except FileNotFoundError:
        print("Error: File 'animal.jpeg' not found")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
