# jacatonlib

Libreria principal para acceder a servicios de NLP durante el Jakatón 

## Etiquetación de categorias gramáticales

        import jakatonlib.pos as pos
        pt=pos.POSTagger(root="URL")
        pt.tag("el jakatón se acerca") 
