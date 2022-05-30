#C:\Users\Alunos\PycharmProjects\Projeto6\venv
import cgitb, cgi
import math
import geo_funcs
#Habilita a visualização de erro
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
################ logica do script
# recebe o valor do raio do usuário
lado_ = float(form.getvalue("lado"))
# calcula perimetro
perim_ = lado_ * 6
######## HTML
title = "Retângulo"
geo_funcs.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Lado: {:.1f}".format(lado_))
print("<p>Perímetro do Pentágono: {:.1f}".format(perim_))
print("<br><br>Clique <a href=\'../"
      "pentagono_perim.html\'> aqui</a> para um novo cálculo")
geo_funcs.print_footer()
