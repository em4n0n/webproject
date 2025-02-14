import web

urls = (
    '/(.*)/(.*)', 'index' # root connected to an index class
)
render = web.template.render("resources/")
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return render.main(name, age)

if __name__ == "__main__":
    app.run()