import streamlit as st
from PIL import Image
import io


def resize_image(image, size):
    return image.resize(size, Image.LANCZOS)


st.title("Image Resizer🔄")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    image_width = 150  # Adjust this value as needed

    # Create two columns to center the image
    col1, col2, col3 = st.columns([1, 1, 1])  # You can adjust the column proportions

    #with col2:  # Use the middle column for the image
         #st.image(image, caption="Original Image", width=image_width)


    # Resize options
    width = st.number_input("Width (pixels)", min_value=1, value=image.width)
    height = st.number_input("Height (pixels)", min_value=1, value=image.height)

    if st.button("Resize Image"):
        # Resize the image
        resized_image = resize_image(image, (width, height))

        with col2:  # Use the middle column for the output image
            st.image(resized_image, caption="Resized Image", width=image_width)
        # Convert resized image to bytes

        img_byte_arr = io.BytesIO()
        resized_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Download button
        with col2:
            st.download_button(
                              label="Download Image",
                              data=img_byte_arr,
                              file_name="resized_image.png",
                              mime="image/png"
                              )
