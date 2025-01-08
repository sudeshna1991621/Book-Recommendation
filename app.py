import streamlit as st
import pandas as pd
import pickle

# Set page configuration at the very top
st.set_page_config(page_title="Book Recommender App", layout="wide")
book = pd.read_csv('Books.csv')

# Load the .pkl file containing the book data
@st.cache_data
def load_top_books():
    with open('Top50.pkl', 'rb') as file:
        top_books = pickle.load(file)
    return top_books

# Load top books
top_books = load_top_books()

# Streamlit app
st.title("Book Recommendation App")

# Adding custom CSS to style the page
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7fc;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            color: #4a4a4a;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .recommend-button {
            background-color: #28a745;
            color: white;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 1.2em;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .recommend-button:hover {
            background-color: #218838;
        }
        .book-card {
            padding: 20px;
            background-color: white;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s;
            height: 350px;  /* Ensure each card has the same height */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .book-card:hover {
            transform: translateY(-5px);
        }
        .book-card img {
            max-width: 120px;
            border-radius: 8px;
            margin-bottom: 15px;
            align-self: center;
        }
        .book-card h3 {
            color: #4a4a4a;
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .book-card p {
            color: #555;
            font-size: 0.95em;
            margin-bottom: 8px;
        }
        .book-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .tabs .streamlit-expanderHeader {
            background-color: #0077b6;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 1.2em;
            font-weight: bold;
        }
        .tabs .streamlit-expanderHeader:hover {
            background-color: #00639c;
        }
    </style>
""", unsafe_allow_html=True)

# Create tabs
tabs = st.tabs(["Home", "Recommend", "Contact"])

# Home Tab
with tabs[0]:
    st.header("Top 50 Books")
    if top_books is not None:
        st.write("Here are the top 50 books in a grid format:")

        # Display books in a grid format
        num_columns = 5  # Number of columns in the grid
        for i in range(0, len(top_books.head(50)), num_columns):
            cols = st.columns(num_columns)
            for col, (_, row) in zip(cols, top_books.iloc[i:i + num_columns].iterrows()):
                with col:
                    # Book Card
                    st.markdown(f"""
                        <div class="book-card">
                            <img src="{row['Image-URL-S']}" alt="Book Image">
                            <h3>{row['Book-Title']}</h3>
                            <p><strong>Author:</strong> {row['Book-Author']}</p>
                            <p><strong>Publisher:</strong> {row['Publisher']}</p>
                            <p><strong>Year:</strong> {row['Year-Of-Publication']}</p>
                            <p><strong>Avg. Rating:</strong> {row.get('avg_ratings', 'N/A')}</p>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.write("No data available.")

def recommend(book_name):
    with open('Pivottable.pkl', 'rb') as file:
            pt = pickle.load(file)
    with open('similarity.pkl', 'rb') as file:
            similarity_score = pickle.load(file)
    try:
        # Check if the book exists in the dataset
        if book_name not in pt.index:
            return f"'{book_name}' is not found in the dataset. Please check the title."
        
        # Get the index of the book
        index = pt.index.get_loc(book_name)
        
        # Fetch similarity scores for the book
        scores = similarity_score[index]  # similarity_score is assumed to be precomputed
        
        # Create a DataFrame with book titles and their similarity scores
        similar_books = pd.DataFrame({
            'Book-Title': pt.index,
            'Similarity': scores
        })
        
        # Sort by similarity score in descending order and exclude the input book
        recommendations = similar_books[similar_books['Book-Title'] != book_name]
        recommendations = recommendations.sort_values(by='Similarity', ascending=False)
      
        # Return the top 5 recommendations
        top5 = recommendations.head(5)['Book-Title']
        
        items = []
        for i in top5:
            # Get details for each recommended book
            book_details = book[book['Book-Title'] == i].iloc[0]
            
            # Append details to items
            item = {
                'Book-Title': book_details['Book-Title'],
                'Book-Author': book_details['Book-Author'],
                'Image-URL-M': book_details['Image-URL-M']
            }
            
            items.append(item)
        
        return items
    
    except Exception as e:
        return f"An error occurred: {e}"

# Recommend Tab
with tabs[1]:
    st.header("Book Recommendation")
    book_name = st.text_input("Enter a book name to get recommendations:")
    
    # Recommend Button
    if st.button("Recommend", key="recommend_button"):
        if book_name:
            recommended = recommend(book_name)
            # Display recommended books in grid format
            st.write(f"Recommendations for '{book_name}':")
            
            # Book Grid for Recommendations
            st.markdown('<div class="book-grid">', unsafe_allow_html=True)
            for item in recommended:
                st.markdown(f"""
                    <div class="book-card">
                        <img src="{item['Image-URL-M']}" alt="Book Image">
                        <h3>{item['Book-Title']}</h3>
                        <p><strong>Author:</strong> {item['Book-Author']}</p>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a book name to get recommendations.")

# Contact Tab
with tabs[2]:
    st.header("Contact Us")
    st.write("We would love to hear from you! Please reach out to us using the form below.")
    
    # Contact Form
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    message = st.text_area("Message:")
    
    if st.button("Submit"):
        if name and email and message:
            st.success("Thank you for your message. We'll get back to you shortly!")
        else:
            st.error("Please fill out all fields before submitting.")
