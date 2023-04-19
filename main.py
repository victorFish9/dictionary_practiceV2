def add_movie(registy: list, name: str, author: str, year: int, length: int):
    movie_dict = {}
    movie_dict["name"] = name
    movie_dict["author"] = author
    movie_dict["year"] = year
    movie_dict["length"] = length
    registy.append(movie_dict)

def search_movie(registy: list, search_str: str):
    r = []
    r2 = registy
    for i in r2:
        for key, val in i.items():
            if key == "name" and search_str in val.lower():
                r.append(i)
            else:
                pass
    return r
if __name__ == "__main__":
    registy = []
    add_movie(registy, "Star Wars IV: A New Hope", "George Lucas", 1977, 223)
    add_movie(registy, "Garfield: The Movie", "Peter Hewitt", 2004, 94)
    print("Added: ", registy)
    lista = search_movie(registy, "field")
    print("Finded: ", lista)
    