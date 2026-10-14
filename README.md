# Projeto 2 — Orbito-n

Projeto académico da unidade curricular **Fundamentos da Programação**. O código implementa operações para o jogo Orbito-n, incluindo posições, pedras, tabuleiros quadrados com `2n` linhas e colunas, adjacências, linhas, rotação das órbitas e deteção de sequências vencedoras.

As posições são identificadas por uma letra de coluna e um número de linha (por exemplo, `b3`). As pedras são representadas por `X` (preta), `O` (branca) e um espaço (posição vazia). O tabuleiro suporta entre 2 e 5 órbitas.

## Requisitos

- Python 3
- `pytest` para executar os testes

O módulo `OrbitaN.py` utiliza apenas a biblioteca padrão do Python.

## Utilização

O módulo atual contém as operações de posições, pedras e tabuleiro. Por exemplo, para criar e apresentar um tabuleiro vazio com duas órbitas:

```bash
python3 -c 'import OrbitaN; print(OrbitaN.tabuleiro_para_str(OrbitaN.cria_tabuleiro_vazio(2)))'
```

O controlo completo do jogo, a escolha manual e automática de jogadas e a função principal `orbito` ainda não estão implementados em `OrbitaN.py`; por isso, o jogo completo não pode ser iniciado nesta versão.

## Testes

Instale as dependências de desenvolvimento e execute os testes públicos:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -q
```

No estado atual, 26 dos 38 testes passam. Os outros 12 esperam funções de fim de jogo, seleção de jogadas e execução de partida que ainda não existem no módulo principal.

## Estrutura

| Ficheiro | Descrição |
| --- | --- |
| `OrbitaN.py` | Implementação principal das operações de posição, pedra e tabuleiro. |
| `test_public.py` | Testes públicos das operações e funcionalidades esperadas do projeto. |
| `requirements-dev.txt` | Dependência de desenvolvimento para executar os testes. |
| `FP-2024-P2_V2.pdf` | Enunciado do projeto fornecido para a cadeira. |

A cópia de trabalho com nome de computador é um material local e não faz parte deste repositório.
