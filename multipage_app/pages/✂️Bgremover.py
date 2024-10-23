import streamlit as st
from rembg import remove
from PIL import Image
import io

# Title of the app
st.title("Background Remover✂️")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Color picker for background
background_color = st.color_picker("Select Background Color", "#FFFFFF")  # Default is white

if uploaded_file is not None:
    # Read the uploaded image
    input_image = Image.open(uploaded_file)

    # Define the desired width for the image
    image_width = 150  # Adjust this value as needed

    # Create two columns to center the image
    col1, col2, col3 = st.columns([1, 1, 1])  # You can adjust the column proportions

    #with col2:  # Use the middle column for the image
        #st.image(input_image, caption="Uploaded Image", width=image_width)

    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    input_image.save(img_byte_arr, format='PNG')
    input_image_bytes = img_byte_arr.getvalue()

    # Remove the background
    output_image_bytes = remove(input_image_bytes)

    # Convert bytes back to image
    output_image = Image.open(io.BytesIO(output_image_bytes))

    # Create a new image with the selected background color
    bg_color = Image.new("RGBA", output_image.size, background_color)
    combined_image = Image.alpha_composite(bg_color, output_image.convert("RGBA"))

    with col2:  # Use the middle column for the output image
        st.image(combined_image, caption="Output Image with Custom Background", width=image_width)

    # Download button for the output image
    buf = io.BytesIO()
    combined_image.save(buf, format='PNG')
    buf.seek(0)

    with col2:
         st.download_button(
         label="Download Image",
         data=buf,
         file_name="output_image.png",
         mime="image/png"
         )


