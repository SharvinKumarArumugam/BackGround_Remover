import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set the Streamlit page configuration
st.set_page_config(
    page_title="Background Remover",
    page_icon="🖼",
    layout="centered"
)

st.title("🖼 Background Remover")
st.write("Upload an image, and this app will remove its background for you!")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    st.subheader("Original Image:")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the image to remove the background
    with st.spinner("Removing background..."):
        result = remove(image)
        result_image = Image.open(io.BytesIO(result))

    # Display the output image
    st.subheader("Image with Background Removed:")
    st.image(result_image, caption="Background Removed", use_column_width=True)

    # Download the processed image
    result_buffer = io.BytesIO()
    result_image.save(result_buffer, format="PNG")
    result_buffer.seek(0)

    st.download_button(
        label="Download Image with Transparent Background",
        data=result_buffer,
        file_name="background_removed.png",
        mime="image/png"
    )

else:
    st.info("Please upload an image to proceed.")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit and rembg")
