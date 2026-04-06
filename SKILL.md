---
name: instagram-prospector
description: "Prospecção de clientes no Instagram através de busca por nicho, interações estratégicas e registro de atividades. Use para: encontrar perfis de nicho, seguir usuários, curtir publicações e comentar estrategicamente."
---

# Instagram Prospector

Este guia orienta o Manus na prospecção ativa de clientes no Instagram, utilizando ferramentas de busca de criadores e navegação direta para interações humanas e autênticas.

## Fluxo de Trabalho de Prospecção

A prospecção deve seguir um ciclo de três etapas: Descoberta, Interação e Registro.

### 1. Descoberta de Perfis de Nicho

Utilize o servidor MCP `meta-creators` para encontrar perfis que correspondam ao nicho solicitado pelo usuário.

- **Ferramenta**: `meta_creators_instagram_search` (server: `meta-creators`).
- **Parâmetros**: Utilize palavras-chave de `/home/ubuntu/skills/instagram-prospector/references/niche-keywords.md`.
- **Filtros**: Priorize contas com engajamento visível e número de seguidores compatível com o público-alvo do usuário.

### 2. Interação Estratégica

Após identificar os perfis, realize interações via navegador para simular um comportamento de usuário real.

- **Ações**: Navegar até o perfil, curtir as 2 ou 3 publicações mais recentes e deixar um comentário relevante.
- **Diretrizes de Comentário**: Utilize os modelos em `/home/ubuntu/skills/instagram-prospector/templates/comment-templates.md` como base, sempre personalizando o texto com algo específico da publicação.
- **Limites de Segurança**: Não realize mais de 10 interações seguidas sem uma pausa de pelo menos 5 minutos para evitar bloqueios da plataforma.

### 3. Registro de Atividades

Para cada perfil interagido, é obrigatório registrar a ação para evitar duplicidade em sessões futuras.

- **Ferramenta**: Execute o script `/home/ubuntu/skills/instagram-prospector/scripts/log_prospect.py`.
- **Comando**: `python3 /home/ubuntu/skills/instagram-prospector/scripts/log_prospect.py <username> <action> <niche>`

## Melhores Práticas

- **Tom de Voz**: Mantenha um tom profissional, porém amigável e curioso. O objetivo é iniciar uma conexão, não vender imediatamente no comentário.
- **Personalização**: Evite comentários genéricos como "Ótimo post!". Mencione detalhes da legenda ou do vídeo.
- **Frequência**: Respeite os limites de taxa do Instagram. Se encontrar muitos perfis, processe-os em lotes pequenos.

## Recursos Disponíveis

- **Scripts**: `scripts/log_prospect.py` para registro de interações.
- **Referências**: `references/niche-keywords.md` para auxílio na busca por nichos.
- **Templates**: `templates/comment-templates.md` para modelos de interação inicial.
