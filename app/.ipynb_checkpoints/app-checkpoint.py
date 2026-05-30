import streamlit as st
from recommender import recommend_products

st.set_page_config(
    page_title="AI Product Discovery Engine",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ AI Product Discovery Engine")

st.write(
    """
    Discover products using natural language.
    Describe what you're looking for and the AI
    will recommend similar products.
    """
)

# Sidebar
st.sidebar.header("Example Searches")

st.sidebar.write("""
• Wireless headphones for workouts

• Home gym equipment

• Kitchen organization

• Gaming accessories

• Office desk setup

• Bluetooth speakers
""")

query = st.text_input(
    "Describe the product you're looking for:"
)

if st.button("Get Recommendations"):

    if query.strip() == "":
        st.warning("Please enter a search query.")
    else:

        results = recommend_products(query)

        st.subheader("Recommended Products")

        for product in results:

            st.markdown("---")

            st.subheader(product["title"])

            st.write(
                f"**Match Score:** {product['score']}%"
            )

            st.write(
                f"**Product Type:** {product['product_type']}"
            )

            st.write(
                f"**Description:** {product['description']}"
            )