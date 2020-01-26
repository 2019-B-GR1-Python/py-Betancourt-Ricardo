import scrapy


def save_file(titulos, precios, links_imagenes):
    path = "C:/Users/Asus/Documents/GitHub/py-Betancourt-Ricardo/arania_basica2/books.txt"
    books = []
    for x in range(0, len(titulos)):
        book = "\tNombreLIbro: " + titulos[x] + "\t" + "Precio: " + precios[x] + "\n" + "ImagenURL: " + links_imagenes[x] + "\n\n\n"
        books.append(book)
    try:
        write_txt = open(path, mode="a")
        write_txt.writelines(books)
        write_txt.close()
    except Exception as error:
        print('Error')


class IntroSpider(scrapy.Spider):
    
    name="introduccion_spider"    
    urls = [
        "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_categories_links) 

    def parse_categories_links(self, response):
        books_urls = response.css("div.side_categories > ul > li > ul > li > a::attr(href)").extract()
        def books_links(book_link):
            if(book_link != 'index.html'):
                book_link = book_link[3:]
            return "http://books.toscrape.com/catalogue/category/books/" + book_link

        books_full_url = list(map(books_links, books_urls))
        for url in books_full_url:
            yield scrapy.Request(url=url, callback=self.parse_books)

    def parse_books(self, response):

        etiqueta = response.css('article.product_pod')
        titulos = etiqueta.css("h3 > a::text").extract()
        precios = etiqueta.css("div.product_price > p.price_color::text").extract()
        imagenes = etiqueta.css("div.image_container > a > img::attr(src)").extract()
        save_file(titulos, precios, imagenes)

    def parse(self, response):
        pass
