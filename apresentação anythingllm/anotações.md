Relatório AnythingLLM
 
# Funcionalidades nativas da plataforma

- usuários
    - cadastro de usuários (membro, gerente, admin)
    - login via username e senha (não tem login por código de verificação)
    - separação apenas por workspaces. usuários podem estar em mais de um workspace. avaliar a melhor maneira de usar(assistentes, departamentos, etc)
- chat
    - integração com múltiplas llms (openai, elevenlabs, claude, ...)
    - agentes de ia por workspace
    - variáveis (para a pessoa usar no chat)
    - histórico de mensagens
    - limite de mensagens por dia
- agentes de ia'
    - skills (muitas possibilidades)
    - flows
    - servidores mcp
    - rag
    - busca na web e web scrapping nos sites
    - speach to text e text to speach
    - acesso a pastas do servidor (ler, editar, criar, etc)
    - criação de documentos (texto, powerpoint, pdf, excel, word)
    - gerar gráficos
    - conectar direto a banco de dados sql
- painel admin
    - provedores de ia
        - llms, api Keys, banco vetorial, speach to text e text to speach.
    - customização
        - logos renova
        - cores
        - tema claro e escuro
    - gerência de usuários
        - criar e editar usuários
        - exportar todas as conversas de todos os usuários
        - gerar link de convite de acesso
- Aplicativo de celular
- Widget para embedar em sites


# Limitações

- controle de acesso limitado por workspace
    - não tem separação avançada por departamento, cargo ou permissão granular
- autenticação simples
    - login por usuário e senha
    - não tem login por código de verificação
- risco com acesso a arquivos e banco de dados
    - permissões devem ser bem controladas para evitar alterações indevidas

# Vantagens

- plataforma pronta para uso interno com ia
- centraliza chat, documentos, agentes e integrações
- suporta múltiplos provedores de llm
- permite criar assistentes por workspace
- facilita rag com documentos da empresa
- permite automações com skills, flows e mcp
- tem painel admin para usuários, customização e provedores
- pode ser customizado com identidade visual da empresa
- possui histórico de conversas e controle de limite de mensagens
- tem aplicativo mobile e widget para sites


# Desvantagens

- exige governança para organizar workspaces, usuários e documentos
- permissões mal configuradas podem expor dados sensíveis
- pode exigir treinamento dos usuários para bom uso dos prompts
- baia customização nativa com a identidade visual da empresa




# Possibilidade que está sendo avaliada
O projeto é opensource de código aberto, então surgi a idéia de criar um fork e customizar o projeto da maneira que julgar mais adequado, adicionando features e removendo funcionalidades que não são necessárias. 
Pontos importantes a serem considerados:
- manter o projeto atualizado com as novas versões do anythingllm: isso exige uma customização cuidadosa bem pensada do ponto de vista de arquitetura de software para evitar conflitos de código quando novas versões oficiais do projeto surgirem.