import web

urls = (
    '/(.*)', 'index' # root connected to an index class
)

class index:
    def GET(self, name):
        print("Hello", name, '. How are you today?')