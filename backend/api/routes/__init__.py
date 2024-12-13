from api.routes import user, token, movie, file, movie_review

routers = [user.router, token.router, movie.router, file.router, movie_review.router]
