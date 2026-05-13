from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Load, crop, grayscale, and display a zoomed image."""
    try:
        img_path = "animal.jpeg"
        img = Image.open(img_path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
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
        print(f"New shape after slicing: {grayscale_3d.shape}")
        print(grayscale_3d)
        _, axes = plt.subplots(1, 1, figsize=(15, 6))
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
