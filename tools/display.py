import matplotlib.pyplot as plt
import cv2

def display_images(images, names):
    """
    Display a list of images using matplotlib.
    
    Parameters:
    - images: List of images to display.
    - names: List of names (titles) for each image.
    """
    num_images = len(images)
    
    # Create a figure with subplots
    fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
    
    # If there is only one image, axes is not a list, so we make it a list
    if num_images == 1:
        axes = [axes]
    
    for i in range(num_images):
        ax = axes[i]
        
        # Check if the image is grayscale
        if len(images[i].shape) == 2 or images[i].shape[2] == 1:
            cmap = 'gray'
        else:
            cmap = None
            # If the image has 3 channels, check if it's in BGR format
            if images[i].shape[2] == 3:
                # Convert BGR to RGB
                try:
                    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
                except:
                    pass
        
        ax.imshow(images[i], cmap=cmap)
        ax.set_title(names[i])
        ax.axis('off')  # Hide the axes
    
    plt.tight_layout()
    plt.show()