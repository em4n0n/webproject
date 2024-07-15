import web

urls = (
    '/(.*)', 'index' # root connected to an index class
)

app = web.application(urls,globals())

class index:
    def GET(self, name):
        return "<h1>Hello " + name + '.</h1> How are you today?'

if __name__ == "__main__":
    app.run()