import numpy as np
import matplotlib.pyplot as plt
import pydicom

def process_dicom_image(file_path='assign.dcm', scale=1.5):

    dicom_image = pydicom.dcmread(file_path)

    image_matrix = dicom_image.pixel_array

    lightened_image = np.clip(image_matrix * scale, 0, 255).astype(np.uint8)

    inverse_image = 255 - lightened_image
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)

    plt.title('Original DICOM Image')

    plt.imshow(image_matrix, cmap='gray')

    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.title('Lightened Image')

    plt.imshow(lightened_image, cmap='gray')

    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.title('Inverse Image')

    plt.imshow(inverse_image, cmap='gray')

    plt.axis('off')
    
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    process_dicom_image('assign.dcm', scale=1.5)
    