# -*- coding: utf-8 -*-
from tree import Tree

if __name__ == "__main__" :
    t = Tree()

    # Rotina de visuais rapidos

    # Caso 1: Inserção
    texto = "testando texto teste testa teste tex t"
    lista_texto = texto.split()
    print("vvv Teste de Inserção vvv")
    for idx, palavra in enumerate(lista_texto):
            print("'" + palavra + "' inserido.")
            t.insert(palavra, idx)
    print("^^^ Teste de Inserção ^^^")
    t.print_tree()
    print("size: " + str(t.size))
    print("^^^ Resultado (Inserção) ^^^")

    # Caso 2: Busca
    print("vvv Teste de Busca vvv")
    for idx, palavra in enumerate(lista_texto):
            r = t.search(palavra)
            print("busca por: '" + palavra + "'. Resultado: " + str(r) + " Esperado: " + str(idx))
    print("^^^ Teste de Busca ^^^")

    # Caso 3: Remoção
    print("vvv Teste de Remoção - Meio vvv")
    print("removendo 't'")
    t.remove("t")
    print("removendo 'testa'")
    t.remove("testa")
    print("^^^ Teste de Remoção - Meio ^^^")
    t.print_tree()
    print("size: " + str(t.size))
    print("^^^ Resultado (Remoção - Meio) ^^^")


    # Caso 4: Remoção
    print("vvv Teste de Remoção - Final vvv")
    print("removendo 'texto'")
    t.remove("texto")
    print("^^^ Teste de Remoção - Final ^^^")
    t.print_tree()
    print("size: " + str(t.size))
    print("^^^ Resultado (Remoção - Final) ^^^")

    # Caso 5 - Inserção
    print("vvv Teste de Inserção - Mesma palavra vvv")
    print("Inserindo 'teste'.")
    t.insert("teste", len(lista_texto))
    print("^^^ Teste de Inserção - Mesma palavra^^^")
    print("Valor esperado: " + str(len(lista_texto)) + ". Valor obtido: " + str(t.search("teste")))
    t.print_tree()
    print("size: " + str(t.size))
    print("^^^ Resultado (Inserção - Mesma palavra) ^^^")

    # Caso 6 - Busca
    print("vvv Teste de Busca sem sucesso - palavra incompleta vvv")
    print("Buscado 'testa'.")
    r = t.search("testa")
    print("^^^ Teste de Busca sem sucesso - palavra incompleta ^^^")
    print("Valor esperado: " + 'None' + ". Valor obtido: " + str(t.search("testa")))
    t.print_tree()
    print("^^^ Resultado (Busca sem sucesso - palavra incompleta) ^^^")


    # Caso 7 - Busca
    print("vvv Teste de Busca sem sucesso - palavra extendida vvv")
    print("Buscado 'texto'.")
    r = t.search("texto")
    print("^^^ Teste de Busca sem sucesso - palavra extendida ^^^")
    print("Valor esperado: " + 'None' + ". Valor obtido: " + str(t.search("texto")))
    t.print_tree()
    print("^^^ Resultado (Busca sem sucesso - palavra extendida) ^^^")


