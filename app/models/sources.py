class Sources:

    all_sources = []

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


    def save_sources(self):
        Sources.all_sources.append(self)


    @classmethod
    def clear_sources(cls):
        Sources.all_sources.clear()

    @classmethod
    def get_sources(cls,id):

        response = []

        for sources in cls.all_reviews:
            if sources.id == id:
                response.append sources)

        return response