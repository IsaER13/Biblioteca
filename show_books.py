from load_book import load_books, save_books

import flet as ft
def show_books(books, show_details):
        list = ft.Column()
        for book in books:
            list.controls.append( 
                ft.ListTile(
                title = ft.Text( book["Titulo"]), 
                subtitle = ft.Text (book["Autor"]),
                on_click =lambda e, l=book: show_details(l,list)
            ))
        return list
    
def add_book(books, messages, page):
        titulo = ft.TextField(label ="Título")
        autor = ft.TextField( label= "Autor")
        comentarios = ft.TextField(label = "comentarios")
        calificacion = ft.TextField(label ="calificación")
        portada = ft.TextField(label = "portada")
        def on_save():
            data = {
            "Titulo" : titulo.value,
            "Autor" : autor.value,
            "Portada" : portada.value,
            "comentarios" : comentarios.value,
            "calificacion" : calificacion.value
            }
            books.append(data)
            save_books(books)
            messages.controls.append(ft.Text("Libro guardado exitosamente!"))
            page.update()
        boton  = ft.Button("Guardar", on_click = lambda e: on_save())
        return ft.Column ([titulo, autor, portada, comentarios, calificacion, boton])
def delete(books,book, messages, page):
    books.remove(book)
    save_books(books)
    messages.controls.append(ft.Text("libro eliminado exitosamente"))
    page.update()
    
def update(books, book, messages, page):
    titulo =  ft.TextField( label = "titulo", value = book ["Titulo"])
    autor =  ft.TextField(label = "Autor", value = book ["Autor"])
    portada = ft.TextField(label = "Portada", value = book ["Portada"])
    comentarios = ft.TextField(label = "comentarios", value = book ["comentarios"])
    calificacion = ft.TextField(label = "calificacion", value = book ["calificacion"])
    def on_save(e):
        data = {
           "Titulo" : titulo.value,
            "Autor" : autor.value,
            "Portada" : portada.value,
            "comentarios" : comentarios.value,
            "calificacion" : calificacion.value
            }
        books.append(data)
        save_books(books)
        messages.controls.append(ft.Text("libro actualizado exitosamente") )
        page.update() 
        buttons = ft.Button("Guardar", on_click =  on_save)
        messages.controls.append(
            ft.Column(
                controls = [titulo, autor, portada, comentarios, calificacion, buttons]
                       
            )
        ) 
        page.update()