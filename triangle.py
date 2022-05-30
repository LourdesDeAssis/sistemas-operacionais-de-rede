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
base_ = float(form.getvalue("base_tri_"))
altura_ = float(form.getvalue("alturaTri_"))
# calcula área
area_tri = float(((base_ * altura_)/2))
######## HTML
title = "Triângulo"
geo_funcs.print_header(title)
print("<h1>Triângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base_))
print("<p>Altura: {:.1f}".format(altura_))
print("<p>Área do Triângulo: {:.1f}".format(area_tri))
print("<br><br>Clique <a href=\'../triangulo.html\'> aqui</a> para um novo cálculo")
geo_funcs.print_footer()