def newsEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "description":item["description"],
        "title":item["title"],
        "url":item["url"],
        "urlToImage":item["urlToImage"],
        "author":item["author"]
    }
def newsEntity(entity) -> list:
    return [newsEntity(item) for item in entity]