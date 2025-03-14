# Book Recommender App 📚✨

Welcome to the **Book Recommender App**! This interactive web app helps you discover your next great read with personalized book recommendations. Using **Collaborative Filtering**, the app provides book suggestions based on user ratings and preferences, making it easier for you to find books that suit your tastes.

## 🚀 Features:
- **Top 50 Books**: A curated list of the **Top 50 Books** displayed in a grid format with details like the author, publisher, average rating, and more.
- **Book Recommendations**: Select a book, and the app will recommend **5 similar books** based on collaborative filtering and **Cosine Similarity**.
- **Contact Us**: Reach out via an easy-to-use form for any inquiries or feedback.

## 🧠 How It Works:
- **Collaborative Filtering**: The app analyzes **user ratings** to find similarities between books using **Cosine Similarity**. Books with similar ratings and themes are recommended.
- **Preprocessed Data**: The app uses preprocessed data stored in **Pickle** files, including a **pivot table**, **similarity scores**, and **book details**.

## 🔧 Technologies Used:
- **Streamlit**: For building the web-based user interface.
- **Pandas**: For data manipulation and handling.
- **Cosine Similarity**: To compute the similarity between books based on user ratings.
- **Pickle**: To store and load preprocessed data like book details, ratings, and similarity scores.
  
## 📦 Project Files:
- `books.pkl`: Contains the dataset of all book details (titles, authors, publisher, ratings).
- `Top50.pkl`: A list of the top 50 books for display and recommendation.
- `Pivottable.pkl`: A pivot table for organizing user ratings for collaborative filtering.
- `similarity.pkl`: Precomputed similarity scores for faster recommendations.

## 🏃‍♂️ How to Run:
1. Clone the repository to your local machine:
   ```git clone https://github.com/your-username/book-recommender-app.git```
2. Install the required dependencies:
```pip install streamlit pandas```
3. Launch the app using Streamlit:
```streamlit run app.py```
4. Open the provided local URL in your browser to start using the app.
## 🌐 Deployed App:
The final deployed application is live and can be accessed via the following link:  
👉 [Book Recommender App](https://book-recommendation-2ly5.onrender.com)
## 📱 Usage:
- Home Tab: Browse the top 50 books, complete with book covers and details.
- Recommend Tab: Select a book from the dropdown and receive 5 personalized recommendations based on collaborative filtering.
- Contact Tab: Use the form to get in touch with the app developers for any inquiries or feedback.
## 💡 Why You'll Love This App:
- Personalized Recommendations: Discover new books based on what others are reading and their preferences.
- Beautiful UI: A user-friendly, visually appealing design for easy navigation and exploration.
- Fast and Accurate: Leveraging precomputed data and Cosine Similarity to provide quick, relevant recommendations.
## 📬 Contact Us:
If you have any feedback, questions, or suggestions, feel free to use the Contact Us form in the app. We're always looking for ways to improve!

