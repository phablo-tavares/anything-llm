# -*- coding: utf-8 -*-
from fpdf import FPDF
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "AnythingLLM - Apresentacao.pdf")

FONT_DIR   = "C:/Windows/Fonts"
FONT_R     = os.path.join(FONT_DIR, "arial.ttf")
FONT_B     = os.path.join(FONT_DIR, "arialbd.ttf")
FONT_I     = os.path.join(FONT_DIR, "ariali.ttf")
FONT_BI    = os.path.join(FONT_DIR, "arialbi.ttf")

# Paleta de cores
AZUL_ESCURO  = (15,  40,  80)
AZUL_MEDIO   = (30,  80, 160)
AZUL_CLARO   = (70, 130, 210)
CINZA_CLARO  = (245, 247, 250)
CINZA_MEDIO  = (180, 190, 205)
BRANCO       = (255, 255, 255)
TEXTO_ESCURO = (30,  35,  45)
VERDE        = (30, 140,  80)
VERMELHO     = (180,  40,  40)
LARANJA      = (200, 110,  20)

PAGE_W, PAGE_H = 297, 210  # A4 landscape


class Slide(FPDF):
    def __init__(self):
        super().__init__(orientation="L", unit="mm", format="A4")
        self.set_auto_page_break(False)
        self.set_margins(0, 0, 0)
        self.add_font("Arial",  "",  FONT_R,  uni=True)
        self.add_font("Arial",  "B", FONT_B,  uni=True)
        self.add_font("Arial",  "I", FONT_I,  uni=True)
        self.add_font("Arial",  "BI",FONT_BI, uni=True)

    def sf(self, style="", size=10):
        self.set_font("Arial", style, size)

    def _fill(self, r, g, b):
        self.set_fill_color(r, g, b)
        self.rect(0, 0, PAGE_W, PAGE_H, "F")

    def _title_bar(self, label: str, bar_h=22):
        self.set_fill_color(*AZUL_ESCURO)
        self.rect(0, 0, PAGE_W, bar_h, "F")
        self.set_fill_color(*AZUL_CLARO)
        self.rect(0, bar_h, PAGE_W, 2, "F")
        self.set_xy(12, 4)
        self.sf("B", 14)
        self.set_text_color(*BRANCO)
        self.cell(0, 14, label)
        self.set_text_color(*TEXTO_ESCURO)

    def _footer_bar(self, n: int, total: int, tag="AnythingLLM | Apresentacao Interna"):
        y = PAGE_H - 10
        self.set_fill_color(*AZUL_ESCURO)
        self.rect(0, y, PAGE_W, 10, "F")
        self.set_xy(12, y + 1)
        self.sf("", 7)
        self.set_text_color(*CINZA_MEDIO)
        self.cell(PAGE_W - 30, 7, tag)
        self.set_xy(PAGE_W - 24, y + 1)
        self.cell(20, 7, f"{n} / {total}", align="R")
        self.set_text_color(*TEXTO_ESCURO)

    def _card(self, x, y, w, h, title, items, title_bg, icon=">", fs=9, tfs=10):
        self.set_fill_color(*title_bg)
        self.rect(x, y, w, 10, "F")
        self.set_xy(x + 3, y + 1.5)
        self.sf("B", tfs)
        self.set_text_color(*BRANCO)
        self.cell(w - 6, 7, title)
        self.set_fill_color(*CINZA_CLARO)
        self.rect(x, y + 10, w, h - 10, "F")
        self.set_text_color(*TEXTO_ESCURO)
        cy = y + 13
        for item in items:
            self.set_xy(x + 3, cy)
            self.sf("B", fs)
            self.set_text_color(*title_bg)
            self.cell(5, 5.5, icon)
            self.set_xy(x + 8, cy)
            self.sf("", fs)
            self.set_text_color(*TEXTO_ESCURO)
            self.multi_cell(w - 10, 5.5, item)
            cy += 6.5
            if cy > y + h - 4:
                break


pdf = Slide()
TOTAL = 10


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 – CAPA
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
for i in range(210):
    t = i / 210
    r = int(15 + (30 - 15) * t)
    g = int(40 + (80 - 40) * t)
    b = int(80 + (160 - 80) * t)
    pdf.set_fill_color(r, g, b)
    pdf.rect(0, i, PAGE_W, 1, "F")

pdf.set_fill_color(*AZUL_CLARO)
pdf.rect(0, 0, 6, PAGE_H, "F")
pdf.set_fill_color(100, 160, 230)
pdf.rect(6, 0, 2, PAGE_H, "F")

pdf.set_xy(25, 55)
pdf.sf("B", 38)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 20, "AnythingLLM")

pdf.set_xy(25, 78)
pdf.sf("", 18)
pdf.set_text_color(180, 210, 250)
pdf.cell(0, 10, "Plataforma de IA para Uso Interno")

pdf.set_draw_color(*AZUL_CLARO)
pdf.set_line_width(0.8)
pdf.line(25, 93, 270, 93)

pdf.set_xy(25, 97)
pdf.sf("", 12)
pdf.set_text_color(210, 225, 245)
pdf.cell(0, 8, "Funcionalidades  |  Vantagens  |  Limitacoes  |  Avaliacao de Customizacao")

pdf.set_xy(25, 115)
pdf.sf("I", 10)
pdf.set_text_color(150, 180, 220)
pdf.cell(0, 6, "Apresentacao para Gerencia do Departamento")

pdf.set_xy(25, 190)
pdf.sf("", 9)
pdf.set_text_color(130, 165, 210)
pdf.cell(0, 6, "Maio de 2026")

pdf._footer_bar(1, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 – O QUE É ANYTHINGLLM
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("O Que e o AnythingLLM?")

pdf.set_fill_color(*AZUL_ESCURO)
pdf.rect(12, 28, PAGE_W - 24, 28, "F")
pdf.set_xy(18, 31)
pdf.sf("B", 13)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 8, "Plataforma open-source de IA conversacional para implantacao interna")
pdf.set_xy(18, 41)
pdf.sf("", 10)
pdf.set_text_color(200, 220, 245)
pdf.multi_cell(PAGE_W - 36, 6,
    "Permite criar assistentes de IA privados, conectar documentos corporativos e "
    "automatizar tarefas - tudo hospedado na infraestrutura da propria empresa, "
    "sem enviar dados a terceiros.")

pilares = [
    (AZUL_ESCURO,  "Privacidade",
     "Dados hospedados\ninternamente.\nNenhuma informacao\nenviada a nuvens\nexternas."),
    (AZUL_MEDIO,   "Flexibilidade",
     "Suporta multiplos\nprovedores de IA\n(OpenAI, Claude,\nLLaMA e outros)."),
    (AZUL_CLARO,   "Integracao",
     "Conecta documentos,\nbanco de dados,\nweb e sistemas\nda empresa."),
]
cx = 12
for bg, titulo, desc in pilares:
    pdf.set_fill_color(*bg)
    pdf.rect(cx, 62, 86, 12, "F")
    pdf.set_xy(cx + 4, 64)
    pdf.sf("B", 11)
    pdf.set_text_color(*BRANCO)
    pdf.cell(78, 8, titulo)
    pdf.set_fill_color(*BRANCO)
    pdf.rect(cx, 74, 86, 50, "F")
    pdf.set_xy(cx + 4, 77)
    pdf.sf("", 9.5)
    pdf.set_text_color(*TEXTO_ESCURO)
    pdf.multi_cell(78, 6, desc)
    cx += 91

pdf._footer_bar(2, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 – GESTÃO DE USUÁRIOS
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Funcionalidades - Gestao de Usuarios e Workspaces")

pdf._card(12, 28, 130, 75,
    "Gerenciamento de Usuarios", [
        "Tres niveis de acesso: Membro, Gerente e Admin",
        "Autenticacao por nome de usuario e senha",
        "Cadastro simplificado via painel administrativo",
        "Geracao de links de convite para novos acessos",
        "Exportacao de historico de todas as conversas",
    ], AZUL_ESCURO)

pdf._card(148, 28, 138, 75,
    "Organizacao por Workspaces", [
        "Cada workspace funciona como um ambiente isolado",
        "Um usuario pode participar de multiplos workspaces",
        "Ideal para separar departamentos ou projetos",
        "Cada workspace pode ter seu proprio agente de IA",
        "Personalizacao de documentos e contexto por workspace",
    ], AZUL_MEDIO)

pdf.set_fill_color(255, 245, 200)
pdf.rect(12, 108, PAGE_W - 24, 16, "F")
pdf.set_fill_color(220, 170, 0)
pdf.rect(12, 108, 4, 16, "F")
pdf.set_xy(20, 111)
pdf.sf("B", 9)
pdf.set_text_color(100, 70, 0)
pdf.cell(0, 5, "Observacao:")
pdf.set_xy(20, 117)
pdf.sf("", 9)
pdf.multi_cell(PAGE_W - 36, 5,
    "A separacao por workspaces e o principal mecanismo de controle de acesso. "
    "E recomendavel definir uma politica clara de organizacao antes da implantacao.")

pdf._footer_bar(3, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 – CHAT E MODELOS DE IA
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Funcionalidades - Chat e Integracao com Modelos de IA")

pdf.set_fill_color(*AZUL_ESCURO)
pdf.rect(12, 28, PAGE_W - 24, 12, "F")
pdf.set_xy(16, 30)
pdf.sf("B", 10)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 8,
    "Provedores compativeis:  OpenAI  |  Anthropic Claude  |  Google Gemini  |  LLaMA  |  Mistral  |  ElevenLabs  |  e outros")

items_chat = [
    "Historico de conversas persistente por usuario",
    "Limite configuravel de mensagens por dia",
    "Variaveis personalizadas utilizaveis nos prompts",
    "Integracao com agentes de IA por workspace",
    "Suporte a voz: Speech-to-Text e Text-to-Speech",
    "Aplicativo mobile para acesso via smartphone",
    "Widget para incorporar chat em sites internos",
]

y = 48
pdf.sf("B", 11)
pdf.set_text_color(*AZUL_ESCURO)
pdf.set_xy(12, y - 4)
pdf.cell(0, 6, "Recursos do Chat")

for i, txt in enumerate(items_chat):
    col = i % 2
    row = i // 2
    bx = 12 + col * 142
    by = y + row * 16
    pdf.set_fill_color(*BRANCO)
    pdf.set_draw_color(*AZUL_CLARO)
    pdf.set_line_width(0.5)
    pdf.rect(bx, by, 136, 13, "FD")
    pdf.set_fill_color(*AZUL_CLARO)
    pdf.rect(bx, by, 3, 13, "F")
    pdf.set_xy(bx + 6, by + 3)
    pdf.sf("", 9.5)
    pdf.set_text_color(*TEXTO_ESCURO)
    pdf.cell(126, 6, txt)

pdf._footer_bar(4, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 – AGENTES DE IA
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Funcionalidades - Agentes de IA")

pdf.set_xy(12, 27)
pdf.sf("", 10)
pdf.set_text_color(*TEXTO_ESCURO)
pdf.cell(0, 7,
    "Os agentes de IA sao o nucleo de automacao da plataforma. "
    "Cada workspace pode ter seu proprio agente com capacidades especificas.")

caps = [
    ("Acesso a Informacoes", AZUL_ESCURO, [
        "RAG - Consulta a documentos\ncorporativos",
        "Busca na web em tempo real",
        "Web scraping em sites\nespecificados",
        "Conexao direta a bancos\nde dados SQL",
    ]),
    ("Producao de Conteudo", AZUL_MEDIO, [
        "Criacao de documentos:\nWord, PDF, Excel, PowerPoint",
        "Geracao de graficos e\nvisualizacoes",
        "Leitura, edicao e criacao\nde arquivos no servidor",
        "Conversao de voz para texto\ne texto para voz",
    ]),
    ("Automacao e Integracao", AZUL_CLARO, [
        "Skills: habilidades\npersonalizadas por agente",
        "Flows: fluxos de trabalho\nautomatizados",
        "Servidores MCP: protocolos\nde contexto avancados",
        "Integracao com APIs e\nsistemas externos",
    ]),
]

cx = 12
for titulo, cor, items in caps:
    pdf.set_fill_color(*cor)
    pdf.rect(cx, 40, 88, 11, "F")
    pdf.set_xy(cx + 3, 42)
    pdf.sf("B", 10)
    pdf.set_text_color(*BRANCO)
    pdf.cell(82, 7, titulo)
    pdf.set_fill_color(*BRANCO)
    pdf.rect(cx, 51, 88, 70, "F")
    cy = 54
    for item in items:
        pdf.set_xy(cx + 3, cy)
        pdf.sf("B", 9)
        pdf.set_text_color(*cor)
        pdf.cell(5, 5, ">")
        pdf.set_xy(cx + 8, cy)
        pdf.sf("", 9)
        pdf.set_text_color(*TEXTO_ESCURO)
        pdf.multi_cell(76, 5, item)
        cy += 12
    cx += 93

pdf.set_fill_color(235, 245, 255)
pdf.rect(12, 126, PAGE_W - 24, 14, "F")
pdf.set_fill_color(*AZUL_CLARO)
pdf.rect(12, 126, 4, 14, "F")
pdf.set_xy(20, 129)
pdf.sf("B", 9.5)
pdf.set_text_color(*AZUL_ESCURO)
pdf.cell(0, 5, "Possibilidade de uso imediato:")
pdf.set_xy(20, 135)
pdf.sf("", 9.5)
pdf.set_text_color(*TEXTO_ESCURO)
pdf.cell(0, 5,
    "Consulta automatica a manuais tecnicos, normas regulatorias e "
    "procedimentos internos via RAG + SQL.")

pdf._footer_bar(5, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 – PAINEL ADMINISTRATIVO
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Funcionalidades - Painel Administrativo")

areas = [
    ("Provedores de IA", AZUL_ESCURO, [
        "Configuracao de LLMs (modelos de linguagem)",
        "Gerenciamento de API Keys centralizado",
        "Banco vetorial para embeddings",
        "Configuracao de Speech-to-Text e Text-to-Speech",
    ]),
    ("Identidade Visual", AZUL_MEDIO, [
        "Upload de logo da empresa/departamento",
        "Personalizacao de cores do sistema",
        "Suporte a tema claro e escuro",
        "Interface adaptavel a identidade da organizacao",
    ]),
    ("Gerencia de Usuarios", VERDE, [
        "Criacao e edicao de perfis de usuario",
        "Geracao de links de convite para acesso",
        "Exportacao de todas as conversas do sistema",
        "Controle de permissoes: Membro/Gerente/Admin",
    ]),
]

cx = 12
for titulo, cor, items in areas:
    pdf._card(cx, 28, 88, 100, titulo, items, cor)
    cx += 93

pdf.set_fill_color(230, 245, 235)
pdf.rect(12, 133, PAGE_W - 24, 14, "F")
pdf.set_fill_color(*VERDE)
pdf.rect(12, 133, 4, 14, "F")
pdf.set_xy(20, 136)
pdf.sf("B", 9.5)
pdf.set_text_color(0, 90, 40)
pdf.cell(0, 5, "Governanca centralizada:")
pdf.set_xy(20, 142)
pdf.sf("", 9.5)
pdf.set_text_color(*TEXTO_ESCURO)
pdf.cell(0, 5,
    "O painel admin oferece visibilidade completa sobre usuarios, conversas e "
    "configuracoes - facilitando auditoria e conformidade.")

pdf._footer_bar(6, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 – VANTAGENS
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Vantagens da Plataforma")

vantagens = [
    "Plataforma pronta para uso interno com IA - reduz o tempo de implantacao",
    "Centraliza chat, documentos, agentes e integracoes em um unico ambiente",
    "Suporta multiplos provedores de LLM - flexibilidade e sem lock-in de fornecedor",
    "Permite criar assistentes especializados por workspace (departamento, projeto, etc.)",
    "Facilita RAG com documentos da empresa - respostas baseadas em fontes internas",
    "Permite automacoes avancadas com Skills, Flows e servidores MCP",
    "Painel admin completo para gerenciar usuarios, provedores e customizacoes",
    "Identidade visual personalizavel com logo e cores da empresa",
    "Historico de conversas e controle de limite de mensagens por usuario",
    "Aplicativo mobile e widget para sites - acesso flexivel pelos colaboradores",
]

col1 = vantagens[:5]
col2 = vantagens[5:]

for col_idx, col in enumerate([col1, col2]):
    cx = 12 + col_idx * 143
    cy = 30
    for txt in col:
        pdf.set_fill_color(*BRANCO)
        pdf.rect(cx, cy, 134, 14, "F")
        pdf.set_fill_color(*VERDE)
        pdf.rect(cx, cy, 4, 14, "F")
        pdf.set_xy(cx + 8, cy + 1.5)
        pdf.sf("B", 8.5)
        pdf.set_text_color(*VERDE)
        pdf.cell(4, 5, "+")
        pdf.set_xy(cx + 14, cy + 1.5)
        pdf.sf("", 8.5)
        pdf.set_text_color(*TEXTO_ESCURO)
        pdf.multi_cell(116, 5.5, txt)
        cy += 16

pdf._footer_bar(7, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 – LIMITAÇÕES
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Limitacoes e Pontos de Atencao")

limitacoes = [
    (VERMELHO, "Controle de Acesso Limitado",
     "A separacao de usuarios e feita exclusivamente por workspaces. Nao ha suporte nativo a "
     "permissoes granulares por departamento, cargo ou acao especifica. A organizacao dos "
     "workspaces exige planejamento previo."),
    (LARANJA, "Autenticacao Simples",
     "O sistema utiliza login por nome de usuario e senha. Nao ha suporte nativo a autenticacao "
     "multifator (MFA), login por codigo de verificacao ou integracao com provedores SSO "
     "(ex.: Active Directory, Google Workspace)."),
    (VERMELHO, "Risco com Acesso a Arquivos e Banco de Dados",
     "Quando agentes tem permissao de leitura e escrita em arquivos ou banco de dados, "
     "e essencial configurar permissoes com cuidado. Configuracoes incorretas podem resultar "
     "em alteracoes ou exposicao de dados sensiveis."),
    (LARANJA, "Governanca e Treinamento",
     "A plataforma exige governanca ativa para organizar workspaces, usuarios e documentos. "
     "Usuarios podem precisar de treinamento para uso eficaz de prompts e agentes."),
]

cy = 28
for cor, titulo, desc in limitacoes:
    pdf.set_fill_color(*cor)
    pdf.rect(12, cy, 5, 28, "F")
    pdf.set_fill_color(*BRANCO)
    pdf.rect(17, cy, PAGE_W - 29, 28, "F")
    pdf.set_xy(22, cy + 3)
    pdf.sf("B", 10)
    pdf.set_text_color(*cor)
    pdf.cell(0, 6, titulo)
    pdf.set_xy(22, cy + 10)
    pdf.sf("", 9)
    pdf.set_text_color(*TEXTO_ESCURO)
    pdf.multi_cell(PAGE_W - 34, 5.5, desc)
    cy += 32

pdf._footer_bar(8, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 – FORK
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
pdf._fill(*CINZA_CLARO)
pdf._title_bar("Possibilidade em Avaliacao - Fork do Projeto")

pdf.set_fill_color(*AZUL_ESCURO)
pdf.rect(12, 28, PAGE_W - 24, 20, "F")
pdf.set_xy(18, 31)
pdf.sf("B", 12)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 7, "Proposta: Criar uma versao customizada do AnythingLLM (fork open-source)")
pdf.set_xy(18, 40)
pdf.sf("", 9.5)
pdf.set_text_color(200, 220, 245)
pdf.cell(0, 6,
    "Como o projeto e 100% open-source, e tecnicamente viavel manter uma versao "
    "interna adaptada as necessidades do departamento.")

pdf.set_fill_color(230, 245, 235)
pdf.rect(12, 54, 132, 85, "F")
pdf.set_fill_color(*VERDE)
pdf.rect(12, 54, 132, 11, "F")
pdf.set_xy(16, 56)
pdf.sf("B", 10)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 7, "O que poderiamos fazer")

beneficios = [
    "Adicionar funcionalidades especificas do departamento",
    "Remover recursos desnecessarios para simplificar",
    "Implementar autenticacao mais robusta (MFA, SSO)",
    "Criar permissoes granulares por cargo/departamento",
    "Integrar com sistemas legados internos",
    "Adaptar totalmente a identidade visual da empresa",
]
cy = 68
for b in beneficios:
    pdf.set_xy(16, cy)
    pdf.sf("B", 8.5)
    pdf.set_text_color(*VERDE)
    pdf.cell(5, 5, ">")
    pdf.set_xy(21, cy)
    pdf.sf("", 8.5)
    pdf.set_text_color(*TEXTO_ESCURO)
    pdf.cell(0, 5, b)
    cy += 8

pdf.set_fill_color(255, 240, 235)
pdf.rect(150, 54, PAGE_W - 162, 85, "F")
pdf.set_fill_color(*VERMELHO)
pdf.rect(150, 54, PAGE_W - 162, 11, "F")
pdf.set_xy(154, 56)
pdf.sf("B", 10)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 7, "Desafios e Riscos")

riscos = [
    "Manter o fork sincronizado com novas versoes oficiais exige arquitetura bem planejada",
    "Risco de conflitos entre customizacoes e atualizacoes upstream",
    "Demanda equipe tecnica dedicada para desenvolvimento",
    "Quanto mais customizado, maior o custo de atualizacao",
    "Necessidade de estrategia clara de versionamento",
]
cy = 68
for r in riscos:
    pdf.set_xy(154, cy)
    pdf.sf("B", 8.5)
    pdf.set_text_color(*VERMELHO)
    pdf.cell(5, 5, "!")
    pdf.set_xy(159, cy)
    pdf.sf("", 8.5)
    pdf.set_text_color(*TEXTO_ESCURO)
    pdf.multi_cell(PAGE_W - 170, 5.5, r)
    cy += 11

pdf.set_fill_color(235, 245, 255)
pdf.rect(12, 143, PAGE_W - 24, 14, "F")
pdf.set_fill_color(*AZUL_MEDIO)
pdf.rect(12, 143, 4, 14, "F")
pdf.set_xy(20, 146)
pdf.sf("B", 9.5)
pdf.set_text_color(*AZUL_ESCURO)
pdf.cell(0, 5, "Recomendacao:")
pdf.set_xy(20, 152)
pdf.sf("", 9.5)
pdf.set_text_color(*TEXTO_ESCURO)
pdf.cell(0, 5,
    "Iniciar com a versao padrao para validar adocao e, somente apos, avaliar "
    "customizacoes estrategicas via fork - minimizando risco e maximizando aprendizado.")

pdf._footer_bar(9, TOTAL)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 – CONCLUSÃO
# ══════════════════════════════════════════════════════════════════════════════
pdf.add_page()
for i in range(210):
    t = i / 210
    r = int(15 + (20 - 15) * t)
    g = int(40 + (55 - 40) * t)
    b = int(80 + (100 - 80) * t)
    pdf.set_fill_color(r, g, b)
    pdf.rect(0, i, PAGE_W, 1, "F")

pdf.set_fill_color(*AZUL_CLARO)
pdf.rect(0, 0, 6, PAGE_H, "F")

pdf.set_xy(18, 18)
pdf.sf("B", 18)
pdf.set_text_color(*BRANCO)
pdf.cell(0, 10, "Conclusao e Proximos Passos")

pdf.set_draw_color(*AZUL_CLARO)
pdf.set_line_width(0.6)
pdf.line(18, 31, 280, 31)

pdf.set_xy(18, 35)
pdf.sf("", 10)
pdf.set_text_color(200, 220, 245)
pdf.multi_cell(PAGE_W - 30, 6,
    "O AnythingLLM apresenta-se como uma solucao robusta para centralizar o uso de IA no "
    "departamento, com capacidades avancadas de automacao, acesso a documentos e integracao "
    "com multiplos modelos de linguagem.")

passos = [
    ("1", "Definir politica de workspaces",
     "Mapear departamentos, projetos e fluxos para organizar os workspaces de forma eficiente."),
    ("2", "Configurar ambiente piloto",
     "Implantar versao padrao com grupo reduzido de usuarios para validacao e coleta de feedback."),
    ("3", "Treinar usuarios-chave",
     "Capacitar os primeiros usuarios em prompts, RAG e agentes para maximizar o valor entregue."),
    ("4", "Avaliar expansao ou fork",
     "Com base no piloto, decidir se a versao padrao atende ou se e necessaria customizacao via fork."),
]

cy = 56
for num, titulo, desc in passos:
    pdf.set_fill_color(*AZUL_CLARO)
    pdf.rect(18, cy, 12, 12, "F")
    pdf.set_xy(18, cy + 1)
    pdf.sf("B", 10)
    pdf.set_text_color(*AZUL_ESCURO)
    pdf.cell(12, 10, num, align="C")
    pdf.set_fill_color(30, 55, 105)
    pdf.rect(30, cy, PAGE_W - 42, 12, "F")
    pdf.set_xy(34, cy + 1)
    pdf.sf("B", 10)
    pdf.set_text_color(*BRANCO)
    pdf.cell(80, 5, titulo)
    pdf.set_xy(34, cy + 7)
    pdf.sf("", 8.5)
    pdf.set_text_color(170, 200, 240)
    pdf.cell(0, 5, desc)
    cy += 15

pdf.set_xy(18, 130)
pdf.sf("I", 9)
pdf.set_text_color(120, 160, 210)
pdf.cell(0, 6, "Duvidas e discussoes sao bem-vindas.")

pdf._footer_bar(10, TOTAL)


# ── Salvar ───────────────────────────────────────────────────────────────────
pdf.output(OUTPUT_PATH)
print(f"PDF gerado: {OUTPUT_PATH}")
