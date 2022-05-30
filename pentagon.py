#C:\\Users\\Alunos\\PycharmProjects\\pythonProject6\venv
import cgitb, cgi
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe o valor do raio do usuario
apotema_ = float(form.getvalue('apotema_'))
perimentro_ = float(form.getvalue('perimentro_'))

# calcular area
area_pentagono = ( apotema_ * perimentro_ ) / 2

############ HTML
title = "Pentagono"
geo_funcs.print_header(title)
print("<h1>Pentagono</h1><hr>")
print("<p>Apotema: {:.1f}".format(apotema_))
print("<p>Perimetro: {:.1f}".format(perimentro_))
print("<p>Área do pentagono: {:.1f}".format(area_pentagono))
print("<br><br>Clique <a href=\'../pentagono.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()