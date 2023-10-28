from flask import Flask,render_template,redirect,url_for, request
import pickle
import pandas as pd

app = Flask(__name__)

movies_list = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_data = pickle.load(open('movies_data.pkl', 'rb'))
movies=pd.DataFrame(movies_list)


def recommend(movie):
    found_movies = movies_data[movies_data['title'] == movie]
    index = found_movies.index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_ids = [movies_data.iloc[i[0]].movie_id for i in distances[1:6]]
    recommended_movies = [movies_data.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movie_ids, recommended_movies



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', movies=movies)

@app.route('/result', methods=['POST', 'GET'])
def result():
    movies_name = request.form.get('movie-dropdown')
    recommended_movie_ids, recommended_movies = recommend(movies_name)
    return render_template('result.html', movies_name=movies_name, recommended_movies=recommended_movies)



# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')

