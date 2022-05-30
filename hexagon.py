#C:\\Users\\Alunos\\PycharmProjects\\pythonProject6\venv
import cgitb, cgi
import geo_funcs
import math

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

############ logica do script
# recebe o valor do raio do usuario
lado_ = float(form.getvalue('lado_'))

# calcular area
area_hexagono = ( 3 * ( lado_ * lado_ ) * math.sqrt(3) ) / 2

############ HTML
title = "Hexágono"
geo_funcs.print_header(title)
print("<h1>Hexágono</h1><hr>")
print("<p>Lado: {:.1f}".format(lado_))
print("<p>Área do hexágono: {:.1f}".format(area_hexagono))
print("<br><br>Clique <a href=\'../hexagono.html\'>aqui</a> para novo cálculo.")
geo_funcs.print_footer()