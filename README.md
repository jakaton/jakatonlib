# jacatonlib

Libreria principal para acceder a servicios de NLP durante el Jakatón 

## Etiquetación de categorias gramáticales

        import jakatonlib.pos as pos
        pt=pos.POSTagger(root="URL")
        pt.tag("el jakatón se acerca")

## Obtener score de análisis de sentimiento
        
        import jakatonlib.score as score
        s=score.Scorer(root="URL")
        s.afinn("Este es muy emocionante\nEsto es muy triste")
        s.sentimiento("Este es muy emocionante\nEsto es muy triste")
        s.whissell("Este es muy emocionante\nEsto es muy triste")
        s.sentiwn("Este es muy emocionante\nEsto es muy triste") 

## Obtener idioma de texto a través de MonkeyLearn


        import jakatonlib.monkeylearn as monkeylearn
        ml=monkeylearn.MonkeyLearn()
        ml.language("this is a test\neste es un texto")
