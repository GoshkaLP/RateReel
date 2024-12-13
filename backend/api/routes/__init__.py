from api.routes import user, token, movie, file

routers = [user.router, token.router, movie.router, file.router]
