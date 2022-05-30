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
lado1_ = float(form.getvalue("lado1"))
lado2_ = float(form.getvalue("lado2"))
base_ = float(form.getvalue("base_"))
# calcula perimetro
perim_tri = float(lado1_ + lado2_ + base_)
######## HTML
title = "Triângulo"
geo_funcs.print_header(title)
print("<h1>Triângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base_))
print("<p>Lado 1: {:.1f}".format(lado1_))
print("<p>Lado 2: {:.1f}".format(lado2_))
print("<p>Perímetro do Triângulo: {:.1f}".format(perim_tri))
print("<br><br>Clique <a href=\'../triangulo_perim.html\'> aqui</a> para um novo cálculo")
geo_funcs.print_footer()